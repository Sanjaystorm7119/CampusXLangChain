from langchain_openai import ChatOpenAI
from langchain_google_genai import ChatGoogleGenerativeAI
from google.generativeai import generative_models 
from typing import TypedDict
from pydantic import BaseModel
from dotenv import load_dotenv
load_dotenv()

# model = ChatOpenAI()
# class Review(TypedDict):
#     summary: str
#     sentiment: str


# structured_model =model.with_structured_output(Review)

# result = structured_model.invoke("""the hardware is great, but the software is terrible.
#                           there is no way to use it without a phone app, which is very buggy.
#                         I would not recommend this product to anyone.""")

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")
class Review(BaseModel):
    summary: str
    sentiment: str


structured_model =model.with_structured_output(Review)

result = structured_model.invoke("""the hardware is great, but the software is terrible.
                          there is no way to use it without a phone app, which is very buggy.
                        I would not recommend this product to anyone.""")

print(result)