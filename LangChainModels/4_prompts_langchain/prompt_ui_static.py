# from langchain_openai import ChatOpenAI
from langchain_google_genai import GoogleGenerativeAI
import streamlit as st
from dotenv import load_dotenv
load_dotenv()

st.title("Research tool")
st.header("Summarizer")
# model = ChatOpenAI(model='gpt-4',temperature=1, max_completion_tokens=300)
model = GoogleGenerativeAI(model='gemini-2.5-pro',temperature=1)

userInput = st.text_input("Enter your prompt")

if st.button('Summarize') :
    result = model.invoke(userInput)
    st.write(result)
    # print(result)