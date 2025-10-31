from dotenv import load_dotenv
import os
from langchain_groq import ChatGroq  
load_dotenv()

def create_llm_model(
    model: str = "openai/gpt-oss-20b",
    temperature: float = 0.7,
    max_tokens: int = None,
    timeout: int = None,
    max_retries: int = 2
):
    """
    Creates and returns a configured instance of the model.

    Args:
        explain about the params

    Returns:
        Configured model instance
    """
    groq_api_key = os.getenv("GROQ_API_KEY")
    model = ChatGroq(
        model=model,
        temperature=temperature,
        groq_api_key=groq_api_key,
        max_tokens=max_tokens,
        timeout=timeout,
        max_retries=max_retries,
    )
    return model
