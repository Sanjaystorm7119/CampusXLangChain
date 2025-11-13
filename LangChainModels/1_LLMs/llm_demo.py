from langchain_openai import OpenAI
# from langchain_google_genai import GoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

llm = OpenAI(model="gpt-3.5-turbo-instruct")
# llm = GoogleGenerativeAI(model="gemini-2.5-flash")
 
inputstr = input("enter prompt: ")
while inputstr not in ["exit","bye"]:
    result = llm.invoke(inputstr)
    print(f"result : {result}")
    inputstr = input("enter prompt: ")
