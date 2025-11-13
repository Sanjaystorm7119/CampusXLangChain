from langchain_huggingface import HuggingFaceEmbeddings
embedding = HuggingFaceEmbeddings(model="sentence-transformers/all-MiniLM-L6-v2")
text = "Delhi is the capital of India"
docs=["Delhi is the capital of India",
      "Kolkata is the capital of WestBengal",
      "Chennai is the capital of Tamil Nadu"
      ]
vector = embedding.embed_documents(docs)
print(vector)
print(len(vector))
for lis in vector:
    print(len(lis))