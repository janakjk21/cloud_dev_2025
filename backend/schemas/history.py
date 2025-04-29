from pydantic import BaseModel

class HistoryCreate(BaseModel):
    query: str
    result: str

class HistoryUpdate(BaseModel):
    query: str
    result: str

class HistoryOut(BaseModel):
    id: int
    query: str
    result: str

    class Config:
        from_attributes = True
