import streamlit as st
import requests
import os
from dotenv import load_dotenv

load_dotenv()

##Langsmith tracking
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACKING_V2"] = "true"

def get_openai_response(inout_text):
    response = requests.post("http://localhost:8000/essay/invoke",
                             json={'input':{'topic':input_text}})
    return response.json()['output']['content']


def get_ollama_response(inout_text):
    response = requests.post("http://localhost:8000/poem/invoke",
                             json={'input':{'topic':input_text}})
    return response.json()['output']


##streamlit framework

st.title("Langchain Demo With Openai and LLAMA2 API chains")
input_text = st.text_input("Write an essay on")
input_text1 = st.text_input("What a poem on")

if input_text:
    st.write(get_openai_response(input_text))

if input_text1:
    st.write(get_ollama_response(input_text1))