from langchain_openai import ChatOpenAI
from typing import TypedDict, Annotated, Optional, Literal
from dotenv import load_dotenv
load_dotenv()

model = ChatOpenAI()
class Review(TypedDict):
    summary: Annotated[str, "A brief summary of the review"]
    sentiment: Annotated[Literal["pos","neg"], "The sentiment of the review, e.g., positive, negative, neutral"]
    pros: Annotated[Optional[list[str]], "Pros of the product"]
    cons: Annotated[Optional[list[str]], "Cons of the product"]


structured_model =model.with_structured_output(Review)

result = structured_model.invoke("""the hardware is great, but the software is terrible.
                          there is no way to use it without a phone app, which is very buggy.
                        I would not recommend this product to anyone.""")

print(result)
print(result['summary'])
print(result['sentiment'])  