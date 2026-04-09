from langchain_groq import ChatGroq

import os
from dotenv import load_dotenv

load_dotenv()  # loads variables from .env

api_key = os.getenv("GROQ_API_KEY")

llm = ChatGroq(
    model="llama3-8b-8192"
)
response = llm.invoke("What is machine learning?")
print(response.content)