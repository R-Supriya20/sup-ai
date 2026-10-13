
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
                model = "gemini-3.5-flash-lite",
                contents=prompt
            )

            return response.text

        except errors.APIError as exc:
            if exc.code == 429:
                raise HTTPException(
                    status_code=503,
                    detail=(
                        "AI service quota is exhausted. "
                        "Please try again after the quota resets."
                    )
                ) from exc

            raise HTTPException(
                status_code=502,
                detail="The AI service request failed."
            ) from exc
