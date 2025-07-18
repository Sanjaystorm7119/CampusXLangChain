from langchain_openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

llm = OpenAI(model="gpt-3.5-turbo-instruct")
inputstr = input("enter prompt: ")
result = llm.invoke(inputstr)

print(f"result : {result}")