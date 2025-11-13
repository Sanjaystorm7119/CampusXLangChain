from sklearn.metrics.pairwise import cosine_similarity
from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
load_dotenv()
embedding = OpenAIEmbeddings(model="text-embedding-3-large", dimensions=300)

document=[
    "Sachin Tendulkar, also known as the 'God of Cricket',holds many batting records",
    "Rohith Sharma has record breaking double centuries",
    "Jasprit is known for his unorthodox action and yorkers",
    "Virat kohli is known for his aggressive batting and leadership"
]

query = "tell me about Sanjay"

documentEmbeddings = embedding.embed_documents(document)
queryEmbeddings = embedding.embed_query(query)

scores=(cosine_similarity([queryEmbeddings],documentEmbeddings)[0]) #should be in 2D in cosineSimilarity

index,score=(sorted(list(enumerate(scores)),key=lambda x:x[1])[-1])

print(document[index])
print(f"similarity score is {score}")
