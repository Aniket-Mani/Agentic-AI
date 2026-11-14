import os
from langchain_openai import ChatOpenAI
from pydantic import BaseModel, Field

class EmailMessage(BaseModel):
    subject:str
    contents:str
    invalid_request: bool | None = Field(default = False)


OPENAI_BASE_URL = os.environ.get("OPENAI_BASE_URL") or None
OPENAI_MODEL_NAME = os.environ.get("OPENAI_MODEL_NAME") or "gpt-4o-mini"
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")

if not OPENAI_API_KEY:
    raise NotImplementedError("OPENAI API key is required")


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

llm_base = ChatOpenAI(**openai_params)

llm = llm_base.with_structured_output(EmailMessage, method ="json_mode")

messages = [
    (
        "system",
        """You are an assistant that composes emails.

        Return ONLY a valid JSON object.
        Do not include Markdown or text outside the JSON.

        The JSON must contain exactly these fields:
        - subject: email subject
        - contents: complete plaintext email
        - invalid_request: boolean indicating whether the request is invalid
        """
    ),
    (
        "human",
        "Create an email about the benefits of coffee."
    )
]

response = llm.invoke(messages)

print(response)
print(type(response))