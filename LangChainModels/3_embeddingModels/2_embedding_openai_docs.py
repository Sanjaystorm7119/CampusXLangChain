from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
load_dotenv()

embedding = OpenAIEmbeddings(model="text-embedding-3-large", dimensions=4)
docs=["Delhi is the capital of India",
      "Kolkata is the capital of WestBengal",
      "Chennai is the capital of Tamil Nadu"
      ]

result = embedding.embed_documents(docs)
print(result)