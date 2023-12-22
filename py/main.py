from getpass import getpass
import os

# Importar las clases de los otros archivos
from PDFDownloader import PDFDownloader
from PDFLoader import PDFLoader
from DocumentSplitter import DocumentSplitter
from DocumentEmbedder import DocumentEmbedder
from QAChain import QAChain

# Configuración del API key de OpenAI
OPENAI_API_KEY = getpass("Enter your OpenAI API key: ")
os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY

# Descargar documentos PDF
urls = [
    'https://arxiv.org/pdf/2306.06031v1.pdf',
    'https://arxiv.org/pdf/2306.12156v1.pdf',
    'https://arxiv.org/pdf/2306.14289v1.pdf',
    'https://arxiv.org/pdf/2305.10973v1.pdf',
    'https://arxiv.org/pdf/2306.13643v1.pdf',
]  # Lista de URLs
downloader = PDFDownloader(urls)
ml_papers = downloader.download()

# Cargar documentos PDF
loader = PDFLoader(ml_papers)
documents = loader.load()

# Dividir documentos
splitter = DocumentSplitter(documents)
documents = splitter.split()

# Crear embeddings de documentos
embedder = DocumentEmbedder(documents)
retriever = embedder.embed()

# Consulta y respuesta
chain = QAChain(retriever)
answer = chain.query("qué es fingpt?")
print(answer)
