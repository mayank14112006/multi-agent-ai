# search_agent.py

from langchain.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import Chroma
from langchain.schema import Document
from pathlib import Path
import os

# 1. Load your document(s)
def load_documents(file_path: str):
    loader = TextLoader(file_path)
    return loader.load()

# 2. Split text into chunks (for vector search)
def split_documents(documents: list[Document], chunk_size: int = 300, chunk_overlap: int = 50):
    splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
    return splitter.split_documents(documents)

# 3. Create or load vector DB
def create_vector_db(docs, persist_directory="chroma_db"):
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    vectordb = Chroma.from_documents(docs, embedding=embeddings, persist_directory=persist_directory)
    vectordb.persist()
    return vectordb

# 4. Search the vector DB for relevant chunks
def search(query: str, k: int = 3, persist_directory="chroma_db"):
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    vectordb = Chroma(persist_directory=persist_directory, embedding_function=embeddings)
    results = vectordb.similarity_search(query, k=k)
    chunks = [doc.page_content for doc in results]
    return chunks

# 🧪 Test it locally
if __name__ == "__main__":
    file_path = "app/data/sample.txt"

    if not os.path.exists("chroma_db"):
        print("Loading and indexing sample.txt...")
        raw_docs = load_documents(file_path)
        docs = split_documents(raw_docs)
        create_vector_db(docs)
        print("Indexing complete!")

    print("Searching the vector DB...")
    query = input("Enter your question: ")
    top_chunks = search(query)

    print("\nTop results:\n")
    for i, chunk in enumerate(top_chunks):
        print(f"{i+1}. {chunk}\n")
