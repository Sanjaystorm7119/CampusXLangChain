import os
# from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()
# huggingface_api_key = os.getenv("HUGGINGFACEHUB_ACCESS_TOKEN")

# llm = HuggingFaceEndpoint(
#     repo_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
#     task="text-generation",
#     huggingfacehub_api_token=os.getenv("HUGGINGFACEHUB_ACCESS_TOKEN")
# )

# model=ChatHuggingFace(llm=llm)
model = ChatOpenAI(
    model_name="gpt-3.5-turbo",
    temperature=0.7,max_completion_tokens=150,
    openai_api_key=os.getenv("OPENAI_API_KEY")
)
while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit"]:
        print("Exiting chat...")
        break
    result = model.invoke(user_input)
    print(f"Bot: {result.content}")

