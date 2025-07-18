import os
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()

model = ChatOpenAI(
    model_name="gpt-3.5-turbo",
    temperature=0.7,max_completion_tokens=150,
    openai_api_key=os.getenv("OPENAI_API_KEY")
)
chat_history = []
while True:
    user_input = input("You: ")
    chat_history.append(user_input)
    if user_input.lower() in ["exit", "quit"]:
        print("Exiting chat...")
        break
    result = model.invoke(chat_history)
    chat_history.append(result.content)
    print(f"Bot: {result.content}")
print(chat_history)

