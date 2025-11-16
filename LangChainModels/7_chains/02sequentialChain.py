from langchain_google_genai import GoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

template = PromptTemplate(template="generate a summary on  {topic}",input_variables=['topic'])
template2 = PromptTemplate(template="generate 5 line summary {text}",input_variables=['text'])

model = GoogleGenerativeAI(model="gemini-2.5-flash")

parser = StrOutputParser()


chain = template | model | parser | template2 | model | parser

res = chain.invoke({"topic":"unemployment in 2025 globally in Tech"})
print(res)
chain .get_graph().print_ascii()