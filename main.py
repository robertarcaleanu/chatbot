from ui import create_ui

import os


def main():
    # openai_api_key = os.getenv("OPENAI_API_KEY")
    openai_api_key = "sk-"
    create_ui(openai_api_key)

if __name__ == "__main__":
    main()