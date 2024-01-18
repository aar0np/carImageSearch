from astraConn import get_by_vector
from sentence_transformers import SentenceTransformer

IMAGE_DIR = "/static/images/"
COLLECTION_NAME = "car_images"
model = None

async def get_car_by_text(search_text):
    global model

    if model is None:
        model = SentenceTransformer('clip-ViT-B-32')

    text_emb = model.encode(search_text)
    results = await get_by_vector(COLLECTION_NAME,text_emb,1)

    #should only be one result returned
    return IMAGE_DIR + results[0]["text"]
