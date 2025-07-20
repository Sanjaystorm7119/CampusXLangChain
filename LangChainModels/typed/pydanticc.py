from pydantic import BaseModel,EmailStr, field
from typing import Optional, List, Literal
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()

class Student(BaseModel):
    name: str = "Default Name"
    age: Optional[int] = None
    email: EmailStr = None
    cgpa: Optional[float] = field(default=None, ge=0.0, le=10.0)
    # age: int
    # email: Optional[str] = None
    # subjects: List[str]
    # grade: Literal['A', 'B', 'C', 'D', 'F']

new_student = {
    "name": "John Doe",
    "age": 20,
    "email": "a@b.com"
    }

student = Student(**new_student)
print(student)
print(type(student))
