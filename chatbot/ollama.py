# LANGCHAIN_API_KEY = "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"
# OPENAI_API_KEY = "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"
# LANGCHAIN_PROJECT = "First_chatbot"


from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama
import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()


##Langsmith tracking
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACKING_V2"] = "true"

##Creating Chatbot
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant. Please provide response to the user queries"),
        ("user", "Question:{question}")
    ]
)

##streamlit framework
st.title("Langchain Demo With LLama2 API")
input_text = st.text_input("Search the topic you want")

##LLama2 Call
llm = Ollama(model="llama2")
output_parser = StrOutputParser()

##Chain
chain = prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({'question':input_text}))