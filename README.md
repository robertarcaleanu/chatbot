# Chatbot

This project consists of creating a chatbot using the following tools and concepts:
* **Tools**
  * Streamlit
  * Langchain
  * OpeanAI API (free tier)
* **Concepts**
  * RAG
  * LLM
  * Vector Database

## Tools

See below the description of the tools that have been used for this personal project.

### Streamlit

Streamlit is an open-source Python library that makes it easy to create and share beautiful, custom web apps for machine learning and data science. It's designed to be easy to use for anyone with basic Python knowledge, without requiring prior experience with web development or front-end frameworks.

In this case, we are going to use Streamlit to create the chatbot interface.


### LangChain

LangChain is an open-source Python framework designed to simplify the development of applications powered by large language models (LLMs). It provides a modular and declarative approach to building applications that leverage LLMs for various purposes.

### OpenAI API

For this project, we are using the OpenAI API (free tier). In this case, we can obtain the API key visiting [this](https://platform.openai.com/docs/overview) page. Be aware that the free tier might be limited.

## Step-by-step develoment

This section includes a step-by-step overview how this project has been developed.

### User interface

As mentioned before, the UI has been created using streanlit. It consists of a form element that allows asking a question, then you need to click on ˋsubmitˋ to get the answer.

### Chat model

For the chat model, we are using ˋchatgpt-3.5-turboˋ, which can be easiy integrated with LangChain. It only requires an API key.

### Adding additioanal knowledge using RAG

RAG stands for Retrieval-Augmented-Generaion. According to [IBM](https://research.ibm.com/blog/retrieval-augmented-generation-RAG), RAG is an AI framework for improving the quality of LLM-generated responses by grounding the model on external sources of knowledge to supplement the LLM’s internal representation of information.

With this project, we aim to use the LLM to help us to understand the requirements and recommendations when designing an airport. Therefore, RAG is used to feed the LLM with the [Annex 14 - Aerodromes - Volume I - Aerodromes Design and Operations](https://store.icao.int/en/annex-14-aerodromes). 

To do so, we can follow these steps:

1. **Load the document**: LangChain allows importing different document types, such as PDF, TXT, HTML, etc.
2. **Store the document**: the document will be stored in a [vector database](https://www.ibm.com/topics/vector-database). There are different options, but in this case, FAISS has been used. Note that we need an embedding model for this. OpenAI provides their option, but we can use open-source embedding models (visit the https://huggingface.co/models?other=embeddings for more details).
3. **Check for similarities**: this last steps allows obtaining the context that will be passed to the LLM to answer the question. This is possible by using the vector database.


Finally, we can create a chain using the LangChain to anwser the question.
