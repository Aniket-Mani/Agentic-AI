from sqlmodel import Field, SQLModel


class ChatMessagePayload(SQLModel):
    message:str

class ChatMessage(SQLModel, table = True):
    id: int | None = Field(default=None, primary_key=True)
    # name: str | None = None
    message:str