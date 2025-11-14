from langchain_core.prompts import PromptTemplate
from langchain_google_genai import GoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser

from dotenv import load_dotenv
load_dotenv()
# from time import time

template = PromptTemplate(
    template="generate 5 intersting facts about {topic}",input_variables=['topic']
)
model = GoogleGenerativeAI(model="gemini-2.5-flash")
parser = StrOutputParser()

chain = template | model | parser
res = chain.invoke({"topic":"cricket"})
print(res)
chain.get_graph().print_ascii()
