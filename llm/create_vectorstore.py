from langchain.vectorstores import FAISS
from langchain.document_loaders import TextLoader
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
        print("========== vectorstore is loading ==========")
        embedding_function = OpenAIEmbeddings(openai_api_key=api_key)
        # db = Chroma(persist_directory=DB_PATH, embedding_function=embedding_function)
        db = FAISS.load_local(DB_PATH, embedding_function)

    return db


def find_similarities(db, question):
    print("========== context is reviewed ==========")
    print(db)
    similar_docs = db.similarity_search(question)
    context = [doc.page_content for doc in similar_docs]

    return ' '.join(context)