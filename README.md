# 📚 PDF Document Processing and Query Answering Project 🚀
Description 📝
This project 🏗️ facilitates the downloading, loading, processing, and querying of PDF documents 📄. It employs a series of Python 🐍 scripts and a Streamlit application 🌐 to provide an interactive user interface. The key functionalities include downloading PDF documents from URLs 🌍, loading these documents into memory 💾, processing them into manageable segments, creating text embeddings of these segments, and finally performing queries and obtaining answers based on the documents' content. We're utilizing LangChain 🛠️, a Python library, to enhance our interaction with OpenAI language models and other NLP-related tasks.

Project Structure 🏛️
The project is composed of several Python scripts, each focusing on a specific task:

PDFDownloader.py: Downloads PDF files from URLs 📥.
PDFLoader.py: Loads PDF documents into memory 🔄.
DocumentSplitter.py: Splits documents into manageable segments ✂️.
DocumentEmbedder.py: Creates text embeddings of the segments 🧠.
QAChain.py: Performs queries and retrieves answers based on the documents' content 🤖.
main.py: The main script that utilizes all the above classes 🎛️.
streamlit_app.py: Streamlit application for an interactive user interface 💻.
Usage of LangChain 🔗
LangChain is a Python library used in this project to facilitate working with OpenAI's language models and other NLP tasks. It is used at several key points in the project:

PDFLoader: Uses LangChain's PyPDFLoader to load PDF documents 📚.
DocumentSplitter: Employs RecursiveCharacterTextSplitter to split the documents into segments 🧩.
DocumentEmbedder: Utilizes OpenAIEmbeddings to generate text embeddings and Chroma to store these embeddings in a vector database 🗃️.
QAChain: Sets up a query and answer process using ChatOpenAI and RetrievalQA from LangChain, combining OpenAI's chat model with the retriever object based on the processed documents 🗣️🔍.



Requirements 📋
Python 3.x 🐍
LangChain 🛠️
Streamlit (for the Streamlit application) 🌐
Requests (for downloading PDF documents) 🌐
Other dependencies specified in requirements.txt

Installation 💾
To install the necessary dependencies, run:

bash
pip install -r requirements.txt

Execution 🏃
To run the Streamlit application, use:

bash
streamlit run streamlit_app.py

Follow the instructions in the application's sidebar to download and process documents, and then perform queries 🖥️.

Contact 📬
For more information or inquiries about the project, you can contact me through my LinkedIn profile: Adrian Infantes.

Contributions 🤝
Contributions to the project are welcome. If you have ideas or improvements, feel free to open an issue or a pull request.

License 📄
MIT License
