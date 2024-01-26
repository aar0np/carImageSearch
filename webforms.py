from flask_wtf import FlaskForm
from flask_wtf.file import FileField
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

#create a search form
class SearchForm(FlaskForm):
	searched = StringField("Searched")
	search_image = FileField("Search by Image")
	submit = SubmitField("Submit")
