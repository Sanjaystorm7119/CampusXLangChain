from langchain_core.prompts import ChatPromptTemplate
# from time import time

# stime = time()
chat_template = ChatPromptTemplate([
    ("system","you are a {domain} expert"),
    ("user","explain in simple terms , what is {topic}")

])

prompt = chat_template.invoke({"domain": "football" , "topic": "offside" })
print(prompt)
# etime = time()
# print(etime-stime)