from dotenv import load_dotenv
import os

from llm import create_vectorstore, initiate_chat

load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")
FILE_PATH = os.getenv('FILE_PATH')
DB_PATH = os.getenv('DB_PATH')

question = 'What is the recommended longitudinal slope on a runway for code number 4?'
db = create_vectorstore.create_vectorstore(openai_api_key, FILE_PATH, DB_PATH)

context = create_vectorstore.find_similarities(db, question)
chat_instance = initiate_chat.define_chat(question, openai_api_key, context)

print(chat_instance.content)