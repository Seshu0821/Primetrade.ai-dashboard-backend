from pydantic import BaseModel

class TaskCreate(BaseModel):
    title: str
    description: str | None = None
    status: str = "pending"

class TaskOut(TaskCreate):
    id: int

    class Config:
        orm_mode = True
