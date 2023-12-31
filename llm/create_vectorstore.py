from langchain.vectorstores import Chroma, FAISS
from langchain.document_loaders import TextLoader, PyPDFLoader
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter

import os

def create_vectorstore(api_key, FILE_PATH, DB_PATH):
    """
    This function creates the vectorstore if it doesn't exist. Otherwise, it loads it

        - api key: OpenAI API Key
        - FILE_PATH: File with knowledge
        - DB_PATH: Database path
    """
    
    # We create vector store only if we don't have it
    if not (os.path.exists(DB_PATH) and os.path.isdir(DB_PATH)):
        print("==========creating vectorstore==========")
        # Load the data
        loader = TextLoader(FILE_PATH)
        documents = loader.load()

        text_splitter = CharacterTextSplitter.from_tiktoken_encoder(chunk_size=30, chunk_overlap=0)
        docs = text_splitter.split_documents(documents)

        # Embed the documents
        embedding_function = OpenAIEmbeddings(openai_api_key=api_key)
        db = FAISS.from_documents(docs, embedding_function)
        db.save_local(DB_PATH)
        
    else:
        embedding_function = OpenAIEmbeddings(openai_api_key=api_key)
        # db = Chroma(persist_directory=DB_PATH, embedding_function=embedding_function)
        db = FAISS.load_local(DB_PATH, embedding_function)

    return db