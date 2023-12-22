import streamlit as st
from PDFDownloader import PDFDownloader
from PDFLoader import PDFLoader
from DocumentSplitter import DocumentSplitter
from DocumentEmbedder import DocumentEmbedder
from QAChain import QAChain

# Título de la aplicación
st.title("PDF Document Processor and Query Answering System")

# Entrada de URLs de documentos PDF
st.header("PDF Downloader")
urls = st.text_area("Enter PDF URLs (one per line)").split("\n")
if st.button("Download PDFs"):
    if urls:
        downloader = PDFDownloader(urls)
        ml_papers = downloader.download()
        st.success(f"Downloaded {len(ml_papers)} documents.")
    else:
        st.error("Please enter at least one URL.")

# Procesamiento de documentos
if 'ml_papers' in locals():
    st.header("Process Documents")
    if st.button("Load and Process Documents"):
        # Cargar documentos
        loader = PDFLoader(ml_papers)
        documents = loader.load()

        # Dividir documentos
        splitter = DocumentSplitter(documents)
        documents = splitter.split()

        # Crear embeddings de documentos
        embedder = DocumentEmbedder(documents)
        retriever = embedder.embed()

        st.success("Documents processed successfully.")

# Consulta y respuesta
if 'retriever' in locals():
    st.header("Query Answering System")
    question = st.text_input("Enter your question")
    if st.button("Get Answer"):
        chain = QAChain(retriever)
        answer = chain.query(question)
        st.write(answer)

# Instrucciones para ejecutar
st.sidebar.header("Instructions")
st.sidebar.write("""
1. Enter the URLs of the PDF documents in the text area.
2. Click 'Download PDFs' to download the documents.
3. Click 'Load and Process Documents' to process the downloaded documents.
4. Enter your question in the text input under 'Query Answering System'.
5. Click 'Get Answer' to receive a response based on the processed documents.
""")
