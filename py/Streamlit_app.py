import streamlit as st
import os
from PDFDownloader import PDFDownloader
from PDFLoader import PDFLoader
from DocumentSplitter import DocumentSplitter
from DocumentEmbedder import DocumentEmbedder
from QAChain import QAChain

# Configuración inicial: establecer la clave API de OpenAI desde st.secrets
os.environ["OPENAI_API_KEY"] = st.secrets["openai_api_key"]

# Título de la aplicación
st.title("PDF Document Processor and Query Answering System")

# Sección para cargar archivos PDF directamente
st.header("Upload PDF Files")
uploaded_files = st.file_uploader("Choose PDF files", accept_multiple_files=True, type=['pdf'])

# Sección para ingresar URLs de documentos PDF
st.header("Enter PDF URLs")
urls = st.text_area("Or enter PDF URLs (one per line)").split("\n")

# Directorio para guardar archivos cargados
upload_dir = 'uploaded_files'
if not os.path.exists(upload_dir):
    os.makedirs(upload_dir)

# Procesar los documentos cargados y descargados
if st.button("Process Documents"):
    ml_papers = []

    # Descargar archivos de URLs
    if urls and urls[0]:
        try:
            downloader = PDFDownloader(urls)
            url_papers = downloader.download()
            ml_papers.extend(url_papers)
            st.success(f"Downloaded {len(url_papers)} documents from URLs.")
        except Exception as e:
            st.error(f"Error during download from URLs: {e}")

    # Guardar archivos cargados
    for uploaded_file in uploaded_files:
        file_path = os.path.join(upload_dir, uploaded_file.name)
        with open(file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())
        ml_papers.append(file_path)
        st.success(f"Uploaded {len(uploaded_files)} documents.")

    # Procesar documentos
    if ml_papers:
        try:
            loader = PDFLoader(ml_papers)
            documents = loader.load()

            splitter = DocumentSplitter(documents)
            documents = splitter.split()

            embedder = DocumentEmbedder(documents, os.environ["OPENAI_API_KEY"])
            retriever = embedder.embed()

            st.session_state.retriever = retriever
            st.success("Documents processed successfully.")
        except Exception as e:
            st.error(f"Error during processing: {e}")

# Consulta y respuesta
if 'retriever' in st.session_state and st.session_state.retriever:
    st.header("Query Answering System")
    question = st.text_input("Enter your question")
    if st.button("Get Answer"):
        try:
            chain = QAChain(st.session_state.retriever, os.environ["OPENAI_API_KEY"])
            answer = chain.query(question)
            st.write(answer)
        except Exception as e:
            st.error(f"Error during query: {e}")
