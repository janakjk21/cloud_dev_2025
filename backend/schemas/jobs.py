from pydantic import BaseModel
from typing import Optional

class JobCreate(BaseModel):
    task_type: str
    input_data: str

class JobStatus(BaseModel):
    status: str
    output: Optional[str] = None