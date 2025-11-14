from langchain_openai import ChatOpenAI
from langchain_google_genai import ChatGoogleGenerativeAI
from google.generativeai import generative_models 
from typing import TypedDict , Annotated , Literal
from pydantic import BaseModel , Field 
from dotenv import load_dotenv
load_dotenv()

# model = ChatOpenAI()
# class Review(TypedDict):
#     summary: Annotated[str,"a brief summary of review"]
#     sentiment: Annotated[str,"overall sentiment of review , either pos/neg/neutral"]


# structured_model =model.with_structured_output(Review)

# result = structured_model.invoke("""the hardware is great, but the software is terrible.
#                           there is no way to use it without a phone app, which is very buggy.
#                         I would not recommend this product to anyone.""")


model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")
class Review(BaseModel):
    summary: str = Field(description="overall description")
    sentiment: Literal["pos", "neg", "neutral"] = Field(description="The sentiment of the review, e.g., positive, negative, neutral")


structured_model =model.with_structured_output(Review)

result = structured_model.invoke("""the hardware is great, but the software is terrible.
                          there is no way to use it without a phone app, which is very buggy.
                        I would not recommend this product to anyone.""")
result=result.model_dump()
# print(result.model_dump())
print(f"sentiment :{result['sentiment']}\nsummary : {result['summary']}")