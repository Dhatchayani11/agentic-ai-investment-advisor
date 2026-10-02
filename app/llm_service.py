from langchain_groq import ChatGroq

from app.config import LLM_API_KEY, LLM_MODEL


def get_llm():
    """
    Creates and returns the Groq LLM client.

    Centralizing LLM creation allows all agents to use
    the same model configuration consistently.
    """

    if not LLM_API_KEY:
        raise ValueError("LLM_API_KEY is not configured.")

    return ChatGroq(
        model=LLM_MODEL,
        api_key=LLM_API_KEY,
        temperature=0,
    )