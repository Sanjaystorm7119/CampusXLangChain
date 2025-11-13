# from langchain_openai import ChatOpenAI
from langchain_google_genai import GoogleGenerativeAI
from langchain.prompts import load_prompt , PromptTemplate
import streamlit as st
from dotenv import load_dotenv
# from promptGenerator import PromptTemplate
load_dotenv()

st.title("Research tool")
st.header("Summarizer")
# model = ChatOpenAI(model='gpt-4',temperature=1, max_completion_tokens=300)
model = GoogleGenerativeAI(model="models/gemini-flash-latest",temperature=1)


# userInput = st.text_input("Enter your prompt")
paper_input = st.selectbox("Select a research paper",["Attenton is all you need","BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding", "GPT-3: Language Models are Few-Shot Learners"])
style_input = st.selectbox("Select a style",["beginner friendly","intermediate","advanced"])
length_input = st.selectbox("Select length",["short (1-2 paragraphs)","medium (3-5 paragraphs)","long (detailed explanation)"])

# #Template for the prompt
# template = load_prompt("./template.json")
# prompt = template.invoke({
#     "paper_input":paper_input,
#     "style_input":style_input,
#     "length_input":length_input
# })

# if st.button('Summarize') :
#     result = model.invoke(prompt)
#     st.write(result)


#Template for the prompt
template = load_prompt("./template.json")

if st.button('Summarize') :
    chain = template | model
    result = chain.invoke(
        {
    "paper_input":paper_input,
    "style_input":style_input,
    "length_input":length_input
}
    )
    st.write(result)