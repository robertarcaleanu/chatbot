from langchain.chat_models import ChatOpenAI
from langchain.prompts import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate
)
from langchain.retrievers import ContextualCompressionRetriever
from langchain.retrievers.document_compressors import LLMChainExtractor 

from langchain.llms import CTransformers
from langchain import PromptTemplate, LLMChain
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler

def define_chat(question: str, api_key: str, context: str) -> str:
    """
    This function creates the chat using the OpenAI API
    
        - question: question that we want to ask the chat
        - api_key: OpenAI API Key
    """
    print("========== chat is initialized ==========")
    # System template
    system_template = "As an aerospace engineer, you are tasked with assisting users in addressing inquiries related to airport design"
    system_message_prompt = SystemMessagePromptTemplate.from_template(system_template)

    # Human question
    human_template = "{question_request}, use this extra context:\n{context}"
    human_message_prompt = HumanMessagePromptTemplate.from_template(human_template)

    # Compile to chat
    chat_prompt = ChatPromptTemplate.from_messages([system_message_prompt, human_message_prompt])
    chat_prompt = ChatPromptTemplate.from_messages([ human_message_prompt])

    # Insert variables
    request = chat_prompt.format_prompt(question_request=question, context=context).to_messages()

    # Chat request
    chat = ChatOpenAI(openai_api_key=api_key,temperature=0, model='gpt-3.5-turbo')

    return chat(request)


def define_chat_llama(question: str, context: str) -> str:
    """
    This function creates an instance of the Llama2 GGML (it runs locally on the CPU)
    """
    print("========== chat is initialized ==========")
    llm = CTransformers(model="TheBloke/Llama-2-7B-Chat-GGML",
                        model_file = 'llama-2-7b-chat.ggmlv3.q2_K.bin', 
                        callbacks=[StreamingStdOutCallbackHandler()],
                        config={'temperature': 0})
    
    template = """
    [INST] <<SYS>>
    You are tasked with assisting users in addressing inquiries related to airport design using the additioanl context provided. The answer must be concise.
    <</SYS>>
    {text}[/INST]
    """

    prompt = PromptTemplate(template=template, input_variables=["text"])
    llm_chain = LLMChain(prompt=prompt, llm=llm)

    input = question + f"\n You must use this extra context:\n{context}"
    response = llm_chain.invoke(input)

    return response['text']