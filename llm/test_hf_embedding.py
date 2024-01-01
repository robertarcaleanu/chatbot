from langchain.vectorstores import FAISS
from langchain.document_loaders import TextLoader
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.embeddings.huggingface import HuggingFaceEmbeddings
from langchain.text_splitter import CharacterTextSplitter

from dotenv import load_dotenv
import os

load_dotenv()
FILE_PATH = os.getenv('FILE_PATH')

loader = TextLoader(FILE_PATH, encoding="utf-8")
documents = loader.load()

# Chunk text
text_splitter = CharacterTextSplitter(chunk_size=100, chunk_overlap=0)

chunked_documents = text_splitter.split_documents(documents)

# Load chunked documents into the FAISS index
embedding_model_name = 'sentence-transformers/all-mpnet-base-v2'
db = FAISS.from_documents(chunked_documents, HuggingFaceEmbeddings(model_name=embedding_model_name))


# Connect query to FAISS index using a retriever
retriever = db.as_retriever(
    search_type="similarity",
    search_kwargs={'k': 4}
)

query = 'What is the recommended longitudinal slope on a runway for code number 3?'
docs = db.similarity_search(query)
print(docs[1].page_content)