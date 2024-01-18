# carImageSearch

An MVC-patterned Python application which relies on Image data written to [DataStax Astra DB](https://astra.datastax.com) by the [astrapyCLIPLoader.py](https://github.com/aar0np/astrapy-CLIP-demo/blob/main/astrapyCLIPLoader.py) from the [astrapy-CLIP-demo](https://github.com/aar0np/astrapy-CLIP-demo) repository. The application uses the [JustPy](https://justpy.io/) library to build a small front end to allow for searching on the image file data. It ultimately uses the [astrapy](https://github.com/datastax/astrapy) library to access and work with the underlying vector embeddings in Astra DB.

## Requirements

 - A vector-enabled [Astra DB](https://astra.datastax.com) database
 - An Astra DB application token
 - An Astra DB API endpoint
 - Environment variables defined for: `ASTRA_DB_APPLICATION_TOKEN`, and `ASTRA_DB_API_ENDPOINT`:

```
export ASTRA_DB_APPLICATION_TOKEN=AstraCS:GgsdfSnotrealHqKZw:SDGSDDSG6a36d8526BLAHBLAHBLAHc18d40
export ASTRA_DB_API_ENDPOINT=https://b9aff773-also-not-real-d3088ea14425-us-east1.apps.astra.datastax.com
```

 - A local `images/` directory containing JPEGs or PNGs to embed.
 - Python dependencies: sentence-transformers, astrapy, and justpy

```
pip install sentence-transformers
pip install astrapy
pip install justpy
```

## Functionality

Descriptions and examples for each Python file in the project.

### carSearch.py

 - Builds a small web frontend for the application (View).
 - Acts as the main program for the application

Usage:

```
python3 carSearch.py
```

### carServices.py

 - Serves the `get_car_by_text` method (Controller).
 - Handles all interactions with the `clip-ViT-B-32` sentence transformer.

### astraConn.py

 - Handles the connectivity with Astra DB (Model).
 - Interacts with the vector data using astrapy.
