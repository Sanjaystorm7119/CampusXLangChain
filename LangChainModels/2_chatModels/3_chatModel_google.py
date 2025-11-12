from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

llm = ChatGoogleGenerativeAI(model="gemini-2.5-pro",temperature=1)
inputstr = input("enter prompt: ")
result = llm.invoke(inputstr)
print(f"result : {result}")

print(f"result : {result.content}")
print(f"result len : {len(result.content)}")
