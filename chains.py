from dotenv import load_dotenv
import os
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from prompts import quiz_generator_prompt
from models import create_llm_model

load_dotenv()

def generate_quiz_chain(topic, num_questions):
    """
    Generate Quiz using basic prompt LLM chain

    Args:
        topic - topic for the quiz
        num_questions - number of questions to generate

    Returns:
        response.content -> str
    """
    # task 1 import llm
    # task 2 import prompt
    # task 3 create chain
    # task 4 invoke chain with topic
    # task 5 return response content
    groq_api_key = os.getenv("GROQ_API_KEY")
    model= create_llm_model()
    prompt = quiz_generator_prompt()
    chain = prompt | model | StrOutputParser()
    response = chain.invoke({
        "topic": topic,
        "num_questions": num_questions
    })
    return response
