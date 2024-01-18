import os

from astrapy.db import AstraDB

# Astra connection
ASTRA_DB_APPLICATION_TOKEN = os.environ.get("ASTRA_DB_APPLICATION_TOKEN")
ASTRA_DB_API_ENDPOINT= os.environ.get("ASTRA_DB_API_ENDPOINT")

# global cache variables to re-use a single Session
db = None
collection = None

async def get_by_vector(table_name, vector_embedding, limit=1):
    global db
    global collection

    if collection is None:
        db = AstraDB(
            token=ASTRA_DB_APPLICATION_TOKEN,
            api_endpoint=ASTRA_DB_API_ENDPOINT,
        )
        collection = db.collection(table_name)

    results = collection.vector_find(vector_embedding.tolist(), limit=limit, fields={"text","$vector"})

    return results