from langchain.chat_models import ChatOpenAI
from langchain.prompts import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate
)
from langchain.retrievers import ContextualCompressionRetriever
from langchain.retrievers.document_compressors import LLMChainExtractor 

def define_chat(question, api_key):
    """
    This function creates the chat using the OpenAI API
    
        - question: question that we want to ask the chat
        - api_key: OpenAI API Key
    """

    # System template
    system_template = "As an aerospace engineer, you are tasked with assisting users in addressing inquiries related to airport design"
    system_message_prompt = SystemMessagePromptTemplate.from_template(system_template)

    # Human question
    human_template = "{question_request}"
    human_message_prompt = HumanMessagePromptTemplate.from_template(human_template)

    # Compile to chat
    chat_prompt = ChatPromptTemplate.from_messages([system_message_prompt, human_message_prompt])

    # Insert variables
    request = chat_prompt.format_prompt(question_request=question).to_messages()

    # Chat request
    chat = ChatOpenAI(openai_api_key=api_key,temperature=0)
    return chat

def use_retriever(chat, db, question):
    """
    This function looks for similarities within the vector data base, obtains the similar documents and provides an anwser

        - chat: Chat model
        - db: vector database
        - question: what we want to ask the chat
    """
    compressor = LLMChainExtractor.from_llm(chat)
    compression_retriever = ContextualCompressionRetriever(base_compressor=compressor,
                                                           base_retriever=db.as_retriver())
    
    compressed_docs = compression_retriever.get_relevant_documents(question)
    
    return compressed_docs[0].page_content