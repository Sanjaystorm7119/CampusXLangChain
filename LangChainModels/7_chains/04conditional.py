from langchain_google_genai import GoogleGenerativeAI
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser, PydanticOutputParser
from langchain.schema.runnable import RunnableBranch , RunnableLambda
from pydantic import BaseModel , Field
from typing import Literal
load_dotenv()

class Feedback(BaseModel):
    sentiment : Literal['positive','negative'] = Field(description="sentiment of feedback")

parser = StrOutputParser()
parser2 = PydanticOutputParser(pydantic_object=Feedback)


template1 = PromptTemplate(template="classify the sentiment of the following feedback into positive or negative \n {feedback} \n {format_instructions}" ,input_variables=['feedback'],partial_variables={'format_instructions':parser2.get_format_instructions()} )

model1 = GoogleGenerativeAI(model="gemini-2.5-flash")
# model2 = ChatOpenAI()


classifier_chain = template1 | model1 | parser2

# res = classifier_chain.invoke({"feedback":"this is a terrible book to read"}).sentiment
# print(res)

template2 = PromptTemplate(template="write an appropriate response to this positive feedback \n{feedback}", input_variables=['feedback'] )

template3 = PromptTemplate(template="write an appropriate response to this negative feedback \n{feedback}", input_variables=['feedback'] )


branch_runnable = RunnableBranch(
    (lambda x:x.sentiment=='positive',template2 | model1 | parser),
    (lambda x:x.sentiment=='negative',template3 | model1 | parser),
    RunnableLambda (lambda  x: "could not find sentiment") #we need to create a chain for default and it is mandatory , so we use runnablelambda to create a runnable lambda)
)

chain = classifier_chain | branch_runnable
print(chain.invoke({'feedback':"it is a terrible phone"}))
chain.get_graph().print_ascii()