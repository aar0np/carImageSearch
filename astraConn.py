import os

from astrapy import DataAPIClient
from astrapy.constants import Environment

# Astra connection
ASTRA_DB_APPLICATION_TOKEN = os.environ.get("ASTRA_DB_APPLICATION_TOKEN")
ASTRA_DB_API_ENDPOINT= os.environ.get("ASTRA_DB_API_ENDPOINT")

# global cache variables to re-use a single Session
db = None
client = None
collection = None

async def get_by_vector(table_name, vector_embedding, limit=1):
    global db
    global client
    global collection

    if client is None:
        client = DataAPIClient(token=ASTRA_DB_APPLICATION_TOKEN)
        #client = DataAPIClient(token=ASTRA_DB_APPLICATION_TOKEN, environment=Environment.DSE)

    if db is None is None:
        db = client.get_database(ASTRA_DB_API_ENDPOINT)

    if collection is None:
        collection = db.get_collection(table_name)
    
    #print(vector_embedding)
    results = collection.find(
        {},
        sort={"$vector": vector_embedding},
        limit=limit,
        projection={"text": True,"$vector": True})

    return results