import os
import json

from astrapy import DataAPIClient
from astrapy.constants import Environment
from PIL import Image
from sentence_transformers import SentenceTransformer

# Astra connection
ASTRA_DB_APPLICATION_TOKEN = os.environ.get("ASTRA_DB_APPLICATION_TOKEN")
ASTRA_DB_API_ENDPOINT = os.environ.get("ASTRA_DB_API_ENDPOINT")

client = DataAPIClient(token=ASTRA_DB_APPLICATION_TOKEN)
#client = DataAPIClient(token=ASTRA_DB_APPLICATION_TOKEN, environment=Environment.DSE)
db = client.get_database(ASTRA_DB_API_ENDPOINT)

# create "collection" (vector-enabled table)
col = db.create_collection("car_images", dimension=512, metric="cosine")

model = SentenceTransformer('clip-ViT-B-32')

IMAGE_DIR = "static/images/"

for id, imageName in enumerate(os.listdir(IMAGE_DIR)):

    img_emb = model.encode(Image.open(IMAGE_DIR + imageName))

    strJson = '{"_id":"' + str(id) + '","text":"' + imageName + '","$vector":' + str(img_emb.tolist()) + '}'
    doc = json.loads(strJson)
    col.insert_one(doc)
    print(imageName)
