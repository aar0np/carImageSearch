from flask import Flask, render_template
from webforms import SearchForm
from carServices import get_car_by_text
from carServices import get_car_by_image

import os

app = Flask(__name__)
app.config.from_object('config.ProdConfig')

INPUT_IMAGE_DIR = "static/input_images/"
basedir = os.path.abspath(os.path.dirname(__file__))

@app.route('/')
def index():
    return render_template('main.html')

# Pass stuff to navbar
@app.context_processor
def base():
    form = SearchForm()
    return dict(form=form)

# create search function
@app.route('/search', methods=["POST"])
async def search():
    form = SearchForm()
    if form.searched.data != "":
        # execute vector search in Astra DB
        response = await get_car_by_text(form.searched.data)
        return render_template("search.html", form=form, searched=form.searched.data, image_file=response, search_image_file="noImage.png")
    elif form.search_image.data != "":
        search_image=form.search_image.data
        search_image_file=search_image.filename
        # save locally
        search_image.save(os.path.join(basedir, INPUT_IMAGE_DIR, search_image_file))
        # execute vector search in Astra DB
        response = await get_car_by_image(search_image_file)
        return render_template("search.html", form=form, searched=search_image_file, image_file=response, search_image_file=search_image_file)
