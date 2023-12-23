from llm import chat, create_vectorstore

import streamlit as st
import os

def create_ui(openai_api_key):
    """
    This function creates the chatbot UI using Streamlit
    """
    st.set_page_config(page_title="Aiport Design")
    st.title('LangChain: Airport Design Expert')

    openai_api_key = st.sidebar.text_input('OpenAI API Key')
    # db = create_vectorstore.create_vectorstore(openai_api_key)

    with st.form('my_form'):
        text = st.text_area('Ask a question:', 'I have a letter code F and number code 4, what should I consider when designing the runway?')
        submitted = st.form_submit_button('Submit')
        if not openai_api_key.startswith('sk-'):
            st.warning('Please enter your OpenAI API key!', icon='⚠')
        if submitted and openai_api_key.startswith('sk-'):
            
            # chat = chat.define_chat(submitted, openai_api_key)
            # response = chat.use_retriever(chat, db, submitted)

            st.info('Output text')
