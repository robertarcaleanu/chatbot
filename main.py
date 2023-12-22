from ui import create_ui

from dotenv import load_dotenv

def main():
    load_dotenv()
    # openai_api_key = os.getenv("OPENAI_API_KEY")
    openai_api_key = "sk-"
    create_ui(openai_api_key)

if __name__ == "__main__":
    main()