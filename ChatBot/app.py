from langchain_google_genai import ChatGoogleGenerativeAI # type: ignore
from langchain_core.prompts import ChatPromptTemplate # type: ignore
from langchain_core.output_parsers import StrOutputParser # type: ignore

import os
import streamlit as st # type: ignore
from dotenv import load_dotenv # type: ignore
load_dotenv()

os.environ["GOOGLE_API_KEY"] ="AIzaSyB2ARWNpH5cZhGu8hkJE0RWPxGYTP3bYY4"
os.environ["LANGCHAIN_TRACING_V2"] ="true"
os.environ["LANGCHAIN_API_KEY"] =os.getenv("LANGCHAIN_API_KEY")

prompt=ChatPromptTemplate.from_messages(
    [
        ("system","You are a helpful assistant that answers questions about the LangChain framework."),
        ("user","Question: {question}")
    ]
)

st.title("Langchain Chatbot")
input_text=st.text_input("Search about the topic that you want")

llm=ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    temperature=0.7
)
output_parser=StrOutputParser()
chain=prompt|llm|output_parser
if input_text:
    st.write(chain.invoke({"question":input_text}))
