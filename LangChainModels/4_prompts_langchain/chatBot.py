import os
# from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_openai import ChatOpenAI
from langchain_google_genai import GoogleGenerativeAI
from dotenv import load_dotenv
import streamlit as st
load_dotenv()

# huggingface_api_key = os.getenv("HUGGINGFACEHUB_ACCESS_TOKEN")

# llm = HuggingFaceEndpoint(
#     repo_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
#     task="text-generation",
#     huggingfacehub_api_token=os.getenv("HUGGINGFACEHUB_ACCESS_TOKEN")
# )

# model=ChatHuggingFace(llm=llm)
# model = ChatOpenAI(
#     model_name="gpt-3.5-turbo",
#     temperature=0.7,max_completion_tokens=150,
#     openai_api_key=os.getenv("OPENAI_API_KEY")
# )

model = GoogleGenerativeAI(
    model="models/gemini-flash-latest",
    temperature=0.7
    # openai_api_key=os.getenv("OPENAI_API_KEY")
)

if "messages" not in st.session_state:
    st.session_state.messages = []

st.title("Chat with Google Gemini")

user_input = st.text_input("You: ")
if user_input:
    response = model.invoke(user_input)
    st.session_state.messages.append(("You", user_input))
    st.session_state.messages.append(("AI", response))

    st.session_state.input = ""  


# Display chat history
for sender, msg in st.session_state.messages:
    st.write(f"**{sender}:** {msg}")