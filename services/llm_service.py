from google import genai
from config import settings
class LLMService:

    def __init__(self):
        self.client = genai.Client(
            api_key=settings.gemini_api_key
        )

    def generate(self, prompt: str):

        response = self.client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        return response.text