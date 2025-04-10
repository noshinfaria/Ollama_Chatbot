import streamlit as st 
import os
from langchain_groq import ChatGroq
from langchain.embeddings import OllamaEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains import create_retrieval_chain
from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import PyPDFDirectoryLoader

from dotenv import load_dotenv

load_dotenv()

## load the GROQ
groq_api_key = os.getenv('GROQ_API_KEY')

st.title("Chatgroq With Llama3 Demo")

llm = ChatGroq(hroq_api_key = groq_api_key,
               model_name = "Llama3-8b-8192")

prompt = ChatPromptTemplate.from_template(
"""
Answer the questions based on the provided context only.
Please provide the most accurate response based on the question
<context>
{context}
<context>
Question:{input}

"""
)

def vector_embedding():
    st.session_state.embeddings = OllamaEmbeddings()
    st.session_state.loader = PyPDFDirectoryLoader("./us_census")
    st.session_state.docs = st.session_state.loader.load()
    st.


prompt1 = st.text_input("Enter Your Question From Documents")

if st.button("Documents Embeddings"):
    vector_embedding()
    st.write("Vector Store DB Is Ready")