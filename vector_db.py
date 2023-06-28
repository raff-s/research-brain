import os
from langchain.embeddings import OpenAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import Chroma

class VectorDb:
    def __init__(self):
        module_path = os.path.abspath(__file__)
        module_directory = os.path.dirname(module_path)
        self.persist_directory = os.path.join(module_directory, 'db')
        self.embedding = OpenAIEmbeddings()

    def load_page_to_db(self, content):
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
        texts = text_splitter.split_documents(content)
        vector_db = Chroma.from_documents(documents=texts, 
                                         embedding=self.embedding,
                                         persist_directory=self.persist_directory)

        vector_db.persist()
        vector_db = None

    def db_retriever(self):
        vector_db = Chroma(persist_directory=self.persist_directory, 
                  embedding_function=self.embedding)

        return vector_db.as_retriever()