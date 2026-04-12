from langchain-huggingface import ChatHuggingFace , HuggingFaceEmbeddings

embedding = HuggingFaceEmbeddings(
    model_name = "sentence-transformers/all-MiniLM-L6-v2"

)
texts = [
    "Hello this is Ankit kumar",
    "Hello your name is YouTube",
    "And you all are very beautiful"
]
vector = embedding.embed_documents(texts)

print(vector)