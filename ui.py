import streamlit as st

from llm import create_vectorstore, initiate_chat

def create_ui(openai_api_key, FILE_PATH, DB_PATH):
    """
    This function creates the chatbot UI using Streamlit
    """
    st.set_page_config(page_title="Aiport Design")
    st.title('LangChain: Airport Design Expert')

    # openai_api_key = st.sidebar.text_input('OpenAI API Key')
    # Retrieve data
    db = create_vectorstore.create_vectorstore(FILE_PATH, DB_PATH)

    with st.form('my_form'):
        question = st.text_area('Ask a question:', 'For code number 3, what is the recommended longitudinal runway slope?')
        submitted = st.form_submit_button('Submit')
        if not openai_api_key.startswith('sk-'):
            st.warning('Please enter your OpenAI API key!', icon='⚠')
        if submitted and openai_api_key.startswith('sk-'):
            
            # Get context
            context = create_vectorstore.find_similarities(db, question)

            # Define chat
            chat_instance = initiate_chat.define_chat_llama(question, context)

            st.info(chat_instance)
