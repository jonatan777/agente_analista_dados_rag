from langchain_ollama import ChatOllama
from dotenv import load_dotenv
load_dotenv()

def get_llm():
    return ChatOllama(
        model="llama3.2:1b",
        temperature=0.2
    )