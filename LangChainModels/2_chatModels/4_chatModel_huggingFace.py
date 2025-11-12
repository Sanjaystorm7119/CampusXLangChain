import os
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
HUGGINGFACEHUB_ACCESS_TOKEN = os.getenv("HUGGINGFACEHUB_ACCESS_TOKEN")

llm = HuggingFaceEndpoint(
    repo_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task="text-generation",
    huggingfacehub_api_token=HUGGINGFACEHUB_ACCESS_TOKEN
)
model = ChatHuggingFace(llm=llm)
result = model.invoke("What is the capital of India?")
print(result.content)
