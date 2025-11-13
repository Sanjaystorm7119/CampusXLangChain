import os
from langchain_google_genai import GoogleGenerativeAI
from langchain_core.messages import SystemMessage,HumanMessage,AIMessage
from dotenv import load_dotenv
load_dotenv()

model = GoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0.7
    # openai_api_key=os.getenv("OPENAI_API_KEY")
)
chat_history = [
    SystemMessage(content="You are a helpful assistant."),
]
while True:
    user_input = input("You: ")
    chat_history.append(HumanMessage(content=user_input))
    if user_input.lower() in ["exit", "quit"]:
        print("Exiting chat...")
        break
    result = model.invoke(chat_history)
    chat_history.append(AIMessage(content=result))
    print(f"Bot: {result}")
print(chat_history)

