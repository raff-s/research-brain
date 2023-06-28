import os
from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI

class OpenAi:
    def __init__(self):
        load_dotenv()
        openai_api_key = os.environ.get("OPENAI_API_KEY")

        if not openai_api_key:
            raise ValueError("API key not found in environment variables.")

    def gpt3_5(self):
        return ChatOpenAI(
                    temperature=0.7,
                    model_name='gpt-3.5-turbo'
                )
