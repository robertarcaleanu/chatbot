import os
from dotenv import load_dotenv

from ui import create_ui

def main():
    load_dotenv()
    openai_api_key = os.getenv("OPENAI_API_KEY")
    FILE_PATH = os.getenv('FILE_PATH')
    DB_PATH = os.getenv('DB_PATH')
    
    # openai_api_key = "sk-"
    create_ui(openai_api_key, FILE_PATH, DB_PATH)

if __name__ == "__main__":
    main()