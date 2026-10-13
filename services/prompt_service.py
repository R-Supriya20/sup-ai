class PromptService:

    def create_prompt(
        self,
        question: str,
        retrieved_chunks: list,
        conversation: list
    ):

        context = "\n\n".join(
            chunk["text"]
            for chunk in retrieved_chunks
        )

        history = "\n".join(
            f"{message['role']}: {message['content']}"
            for message in conversation[-6:]
        )

        
def build_prompt(question: str, context: str = "") -> str:
    return f"""
You are a helpful AI customer support assistant.

Instructions:
1. Answer the user's question using your general knowledge.
2. Use the supplied document context when it is relevant.
3. If the context does not contain the answer, answer
   using your general knowledge instead.
4. Never claim that general knowledge is an official company policy.
5. If you are uncertain, clearly say so.

Document context:
{context if context else "No relevant documents found."}

User question:
{question}

Answer:
"""
