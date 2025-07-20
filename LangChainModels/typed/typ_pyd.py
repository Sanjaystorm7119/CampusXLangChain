from langchain_openai import ChatOpenAI
from typing import TypedDict, Annotated, Optional, Literal
from pydantic import BaseModel, Field
from dotenv import load_dotenv
load_dotenv()

model = ChatOpenAI()
class Review(BaseModel):
    key_theme: str = Field(description="A brief summary of the review")   
    summary: str = Field(description="A brief summary of the review")
    sentiment: Literal["pos", "neg", "neutral"] = Field(description="The sentiment of the review, e.g., positive, negative, neutral")
    pros: Optional[list[str]] = Field(default=None, description="Pros of the product") 
    cons: Optional[list[str]] = Field(default=None, description="Cons of the product")
    name :Optional[str] = Field(default=None, description="Name of the reviewer")

structured_model =model.with_structured_output(Review)

result = structured_model.invoke("""the hardware is great, but the software is terrible.
                          there is no way to use it without a phone app, which is very buggy.
                        I would not recommend this product to anyone.
                                 My name is John Doe.
                                 """)

print(result.name)
# print(result['summary'])
# print(result['sentiment'])  