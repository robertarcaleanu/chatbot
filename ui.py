from llm import chat, create_vectorstore

import streamlit as st
import os

def create_ui(openai_api_key, FILE_PATH, DB_PATH):
    """
    This function creates the chatbot UI using Streamlit
    """
    st.set_page_config(page_title="Aiport Design")
    st.title('LangChain: Airport Design Expert')

    # openai_api_key = st.sidebar.text_input('OpenAI API Key')
    # Retrieve data
    db = create_vectorstore.create_vectorstore(openai_api_key, FILE_PATH, DB_PATH)

    with st.form('my_form'):
        text = st.text_area('Ask a question:', 'What is the recommended longitudinal slope for code number 3?')
        submitted = st.form_submit_button('Submit')
        if not openai_api_key.startswith('sk-'):
            st.warning('Please enter your OpenAI API key!', icon='⚠')
        if submitted and openai_api_key.startswith('sk-'):
            
            # Define chat
            chat_instance = chat.define_chat(text, openai_api_key)

            # Get response
            response = chat.use_retriever(chat_instance, db, text)

            st.info(response)
