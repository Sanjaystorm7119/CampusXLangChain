from langchain_openai import ChatOpenAI
from typing import TypedDict, Annotated, Optional, Literal
from pydantic import BaseModel, Field
from dotenv import load_dotenv
load_dotenv()

# Load the OpenAI model
model = ChatOpenAI()

# Define the schema
schema = {
    "name": "Review",
    "description": "A product review",
    "properties": {
        "summary": {
            "type": "string",
            "description": "A summary of the review"
        },
        "sentiment": {
            "type": "string",
            "enum": ["positive", "negative", "neutral"],
            "description": "The sentiment of the review"
        },
        "name": {
            "type": "string",
            "description": "The name of the reviewer"
        }
    },
    "required": ["summary", "sentiment", "name"]
}

# Use structured model with schema
structured_model = model.with_structured_output(schema)

# Invoke the model with a product review
result = structured_model.invoke("""
the hardware is great, but the software is terrible.
there is no way to use it without a phone app, which is very buggy.
I would not recommend this product to anyone.
My name is John Doe.
""")

# Print the result and each field to see the output
print(result)  # Entire result
print(result.get('summary'))  
print(result.get('sentiment'))  
print(result.get('name'))  
