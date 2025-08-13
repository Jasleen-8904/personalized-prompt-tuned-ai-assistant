from langchain_community.chat_models import ChatOpenAI
from langchain.schema import HumanMessage
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Retrieve API key from environment variable
api_key = os.getenv("OPENAI_API_KEY")

# Initialize the language model
llm = ChatOpenAI(
    model_name="gpt-3.5-turbo",
    temperature=0.7,
    openai_api_key=api_key
)

def generate_response(task_type, user_input):
    if task_type == "Summarize":
        prompt = f"Summarize this text:\n{user_input}"
    elif task_type == "Analytics Insight":
        prompt = f"Give analytical insights from the following:\n{user_input}"
    elif task_type == "Persona-Based":
        prompt = (
            f"You are a cheerful productivity coach. Answer this: {user_input}"
        )
    else:
        prompt = user_input

    response = llm([HumanMessage(content=prompt)])
    return response.content
