import os

from langchain_core.messages import HumanMessage, SystemMessage
from langchain_openai import ChatOpenAI


class EuriRAG:
    def __init__(self, temperature=0):
        self.llm = ChatOpenAI(
            model=os.getenv("EURI_MODEL", "gemini-3.1-pro-preview"),
            base_url=os.getenv("EURI_BASE_URL", "https://api.euron.one/api/v1/euri"),
            api_key=os.getenv("EURI_API_KEY"),
            temperature=temperature,
        )
        self.system_prompt = (
            "You are an assistant for question-answering tasks. "
            "Use the provided image context to answer the question. "
            "If you don't know the answer, say that you don't know. "
            "Use three sentences maximum and keep the answer concise."
        )

    def answer_question(self, question: str, base64_images: list[str]) -> str:
        print("Sending request to EURI LLM...")

        content = [{"type": "text", "text": question}]
        for b64_img in base64_images:
            content.append({
                "type": "image_url",
                "image_url": {"url": f"data:image/jpeg;base64,{b64_img}"},
            })

        messages = [
            SystemMessage(content=self.system_prompt),
            HumanMessage(content=content),
        ]
        response = self.llm.invoke(messages)
        return response.content