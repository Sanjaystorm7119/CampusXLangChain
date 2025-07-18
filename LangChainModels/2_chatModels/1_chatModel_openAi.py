from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

llm = ChatOpenAI(model="gpt-4",temperature=1,max_completion_tokens=10)
inputstr = input("enter prompt: ")
result = llm.invoke(inputstr)

print(f"result : {result.content}")
print(f"result len : {len(result.content)}")
