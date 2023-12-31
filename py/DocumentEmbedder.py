from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma

class DocumentEmbedder:
    def __init__(self, documents, openai_api_key):
        self.documents = documents
        self.embeddings = OpenAIEmbeddings(model="text-embedding-ada-002", openai_api_key=openai_api_key)

    def embed(self):
        vectorstore = Chroma.from_documents(
            documents=self.documents, embedding=self.embeddings)
        return vectorstore.as_retriever(search_kwargs={"k": 3})

