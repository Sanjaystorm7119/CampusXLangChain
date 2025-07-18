from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv

load_dotenv()

llm = ChatAnthropic(model="claude-3-5-sonnet-20241022",temperature=1)
inputstr = input("enter prompt: ")
result = llm.invoke(inputstr)

print(f"result : {result.content}")
print(f"result len : {len(result.content)}")
