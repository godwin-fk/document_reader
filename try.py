from pinecone import Pinecone, ServerlessSpec
import json
pc = Pinecone(api_key="680b0733-5961-41ff-8d25-c620ab8742ad")

index_name = "document-reader"
pc.create_index(
    name=index_name,
    dimension=384, # Replace with your model dimensions
    metric="euclidean", # Replace with your model metric
    spec=ServerlessSpec(
        cloud="aws",
        region="us-east-1"
    ) 
)
index = pc.Index(index_name)

from sentence_transformers import SentenceTransformer

# Initialize the sentence transformer model
model = SentenceTransformer('paraphrase-MiniLM-L6-v2')

# Example JSON data
data = {
    "title": "Booking Confirmation",
    "description": "This is a booking confirmation for JG."
}

# Convert JSON data to a string
data_str = json.dumps(data)

# Encode the string into a vector
vector = model.encode(data_str).tolist()

# Save the vector to Pinecone
metadata = {"original_data": data_str}  # Metadata to store the original JSON data
index.upsert([(data["title"], vector, metadata)])
print(index.describe_index_stats())