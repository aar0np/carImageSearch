import os

from astrapy import DataAPIClient
from astrapy.constants import Environment
from sentence_transformers import SentenceTransformer
from PIL import Image

# Astra connection
ASTRA_DB_APPLICATION_TOKEN = os.environ.get("ASTRA_DB_APPLICATION_TOKEN")
ASTRA_DB_API_ENDPOINT= os.environ.get("ASTRA_DB_API_ENDPOINT")
COLLECTION_NAME = "car_images"

client = DataAPIClient(token=ASTRA_DB_APPLICATION_TOKEN)
#client = DataAPIClient(token=ASTRA_DB_APPLICATION_TOKEN, environment=Environment.DSE)
db = client.get_database(ASTRA_DB_API_ENDPOINT)

def get_by_vector(table_name, vector_embedding, limit=1):
    #print(vector_embedding)
    collection = db.get_collection(table_name)
    results = collection.find({},
        sort={"$vector": vector_embedding},
        limit=limit,
        projection={"text": True,"$vector": True})
    return results

IMAGE_DIR = "static/images/"
INPUT_IMAGE_DIR = "static/input_images/"
COLLECTION_NAME = "car_images"
search_text = "red tesla"
model = SentenceTransformer('clip-ViT-B-32')

# generate embedding from search_text
text_emb = model.encode(search_text)

print("Searching for \"{search_text}\"...")

# execute vector search
results = get_by_vector(COLLECTION_NAME,text_emb,1)

image = None

# should only be one result returned
for doc in results:
    image = doc["text"]
    break
    
print(IMAGE_DIR + image)
