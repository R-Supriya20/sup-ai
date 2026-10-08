class PromptService:

    def create_prompt(
        self,
        question: str,
        retrieved_chunks: list
    ):

        context = "\n\n".join(
            chunk["text"]
            for chunk in retrieved_chunks
        )

        prompt = f"""
You are an AI customer support assistant.

Answer the user's question using ONLY the information
provided in the context.

If the answer is not available in the context,
say: "I don't have enough information to answer that."

Do not make up information.

Context:
{context}

User question:
{question}

Answer:
"""

        return prompt