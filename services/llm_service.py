
from google import genai
from google.genai import errors
from fastapi import HTTPException

from config.settings import settings


class LLMService:
    def __init__(self):
        self.client = genai.Client(
            api_key=settings.gemini_api_key
        )

    def generate(self, prompt: str):
        try:
            response = self.client.models.generate_content(
                model="gemini-3.8-flash ",
                contents=prompt
            )
            return response.text

        except errors.APIError as exc:
            print("Gemini API error:", exc)
            raise HTTPException(
                status_code=502,
                detail=f"Gemini API error: {exc}"
            ) from exc
