from openai import OpenAI
from app.services.base_service import BaseService
from app.services.openai_upstream.openai_chat_completion import OpenAIChatCompletion

class OpenAIService(BaseService):
    def __init__(self, query_config):
        self.query_config = query_config
        self.client = OpenAI(api_key=self.query_config.service.api_key)

    def chat_completion(self, message):
        openai_chat = OpenAIChatCompletion(self)
        response = openai_chat.send_response(message)
        return response


