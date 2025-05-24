import os
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain.prompts import ChatPromptTemplate

from template import RULE_TEMPLATE

load_dotenv()

print(F"KEY: {os.getenv('OPENAI_API_KEY')}")

def get_openai_llm(model_name: str = "gpt-4.1",
                   max_tokens: int = None,
                   temperature: int = 1,
                   presence_penalty: float = 0.3,
                   stream: bool = False) -> ChatOpenAI:
    return ChatOpenAI(
        model=model_name,
        max_tokens=max_tokens,
        temperature=temperature,
        presence_penalty=presence_penalty,
        openai_api_key=os.getenv("OPENAI_API_KEY"),
        streaming=stream  # ✅ 여기에 stream 옵션 추가
    )
            
def stream_response_from_llm(user_input: str):
    prompt = ChatPromptTemplate.from_template(RULE_TEMPLATE)
    chain = prompt | get_openai_llm(stream=True)  # ✅ 반드시 stream=True

    for chunk in chain.stream({"question_text": user_input}):
        if hasattr(chunk, "content") and chunk.content:
            yield chunk.content
