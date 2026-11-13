from fastapi import APIRouter, Depends
from sqlmodel import Session
from .models import ChatMessagePayload, ChatMessage
from api.db import get_session

router = APIRouter()

@router.get('/')
def chat_health():
    return {"status": "ok"}

# HTTP POST -> payload = {"message" : "Hello world "} -> {"message":"Hello world", "id":1}
# curl -X POST -d '{"message" : "Hello world "}' -H "Content-Type: application/json" http://localhost:8080/api/chats
@router.post("/", response_model = ChatMessage)
def chat_create_message(payload: ChatMessagePayload, session: Session = Depends(get_session)):

    data = payload.model_dump()
    print(data)
    obj = ChatMessage.model_validate(data)
    session.add(obj)
    session.commit()
    session.refresh(obj)

    return obj