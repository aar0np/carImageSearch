from astraConn import get_by_vector
from sentence_transformers import SentenceTransformer
from PIL import Image

IMAGE_DIR = "images/"
INPUT_IMAGE_DIR = "static/input_images/"
COLLECTION_NAME = "car_images"
model = None

async def get_car_by_text(search_text):
    global model

    if model is None:
        model = SentenceTransformer('clip-ViT-B-32')

    # generate embedding from search_text
    text_emb = model.encode(search_text)

    # execute vector search
    results = await get_by_vector(COLLECTION_NAME,text_emb,1)

    # should only be one result returned
    return IMAGE_DIR + results[0]["text"]

async def get_car_by_image(file_path):
    global model

    if model is None:
        model = SentenceTransformer('clip-ViT-B-32')

    # load image from file_path and generate embedding
    img_emb = model.encode(Image.open(INPUT_IMAGE_DIR + file_path))

    # execute vector search
    results = await get_by_vector(COLLECTION_NAME,img_emb,1)

    # should only be one result returned
    return IMAGE_DIR + results[0]["text"]
