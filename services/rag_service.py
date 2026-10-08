from services.embedding_service import EmbeddingService
from services.retrieval_service import RetrievalService
from services.prompt_service import PromptService
from services.llm_service import LLMService


class RAGService:

    def __init__(self):

        self.embedding_service = EmbeddingService()
        self.retrieval_service = RetrievalService()
        self.prompt_service = PromptService()
        self.llm_service = LLMService()

    def answer(
        self,
        question: str,
        user_id: str
    ):

        # 1. Convert question into vector
        query_embedding = (
            self.embedding_service
            .create_embedding(question)
        )

        # 2. Search relevant chunks
        retrieved_chunks = (
            self.retrieval_service.search(
                query_embedding=query_embedding,
                user_id=user_id,
                limit=5
            )
        )

        # 3. Create prompt
        prompt = self.prompt_service.create_prompt(
            question,
            retrieved_chunks
        )

        # 4. Send prompt to Gemini
        answer = self.llm_service.generate(prompt)

        return {
            "answer": answer,
            "sources": retrieved_chunks
        }