import os
from langchain_openai import ChatOpenAI





OPENAI_BASE_URL = os.environ.get("OPENAI_BASE_URL") or None
OPENAI_MODEL_NAME = os.environ.get("OPENAI_MODEL_NAME") or "gpt-4o-mini"
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")

if not OPENAI_API_KEY:
    raise NotImplementedError("OPENAI API key is required")




def get_openai_llm():
    openai_params = {
        "model": OPENAI_MODEL_NAME,
        "api_key": OPENAI_API_KEY,
        "base_url": OPENAI_BASE_URL,
        "timeout": 120,
        "max_retries": 0,
        "max_tokens": 4096,
        "temperature": 0.1,
        "extra_body": {
            "chat_template_kwargs": {
                "enable_thinking": False
            }
        }
    }
    if OPENAI_BASE_URL:
        openai_params['base_url'] = OPENAI_BASE_URL
    return ChatOpenAI(**openai_params)

