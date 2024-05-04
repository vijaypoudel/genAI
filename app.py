from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

import streamlit as st
import os
from decouple import Config

# Specify the path to the .env file
config = Config('C:\\Users\\vpoudel\\PycharmProjects\\langchain_llama_llm\\.env')

# Load environment variables from .env file
os.environ["LANGCHAIN_API_KEY"] = config("LANGCHAIN_API_KEY")
os.environ["OPENAI_API_KEY"] = config("OPENAI_API_KEY")
