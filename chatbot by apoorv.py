# from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama

import streamlit as st
import os
from dotenv import load_dotenv 

load_dotenv()

os.environ["LANGCHAIN_TRACKING_V2"]="true"
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")

##pROMPT tEMPLATE

prompt=ChatPromptTemplate.from_messages(
    {
        ("system","You are a helpful assistant. Please response to the user queries"),
        ("user","Question:{question}")

    }
)

##streamlit framework

st.title('Chatbot by Apoorv Tandon')
input_text=st.text_input("Type your queries: ")

##openAI LLm

llm=Ollama(model="llama2")
output_parser=StrOutputParser()
chain=prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({'question':input_text}))
