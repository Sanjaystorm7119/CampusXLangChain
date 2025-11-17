from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableSequence
from dotenv import load_dotenv
load_dotenv()
prompt = PromptTemplate(
    template="write 5 lines about {topic}",
    input_variables=['topic']
)

model = ChatGoogleGenerativeAI(
    model='gemini-2.5-flash',
    temperature = 1,
    disable_streaming= False
)

parser = StrOutputParser()

prompt2 = PromptTemplate(template="make a single joke of it {text}",input_variables=['text'])

sequence = RunnableSequence(prompt,model,parser)
print(sequence.invoke({'topic':'AI'}))
print("\n\n")
sequence1 = RunnableSequence(prompt,model,parser,prompt2,model,parser)
print(sequence1.invoke({'topic':'AI'}))

