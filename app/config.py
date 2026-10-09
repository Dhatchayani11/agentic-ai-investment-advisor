import os

from dotenv import load_dotenv

load_dotenv()


LLM_API_KEY = os.getenv("LLM_API_KEY")
LLM_MODEL = os.getenv("LLM_MODEL", "gpt-4o-mini")

if not LLM_API_KEY: raise RuntimeError( 
    "LLM_API_KEY is not configured. " 
    "Set it in your environment or .env file." )