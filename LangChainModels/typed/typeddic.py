from langchain_openai import ChatOpenAI
from typing import TypedDict
from dotenv import load_dotenv
load_dotenv()

model = ChatOpenAI()
class Review(TypedDict):
    summary: str
    sentiment: str


structured_model =model.with_structured_output(Review)

result = structured_model.invoke("""the hardware is great, but the software is terrible.
                          there is no way to use it without a phone app, which is very buggy.
                        I would not recommend this product to anyone.""")

print(result)