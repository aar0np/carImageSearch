import justpy as jp

from carServices import get_car_by_text
from carServices import get_car_by_file

webp = jp.WebPage()
INPUT_IMAGE_DIR = "/static/input_images/"

async def search_handler(self, msg):
	self.div.text = self.value
	response = await get_car_by_text(self.value)
	image.src=response
	self.value = ""

async def file_input_handler(self, msg):
	self.file_div.delete_components()

	f = msg.files[0]
	file_data_div = jp.Div(text=f"{f.name} | {f.size} | {f.type} | {f.lastModified}", a=self.file_div,
			classes='font-mono m-1 p-2')
	jp.Img(src=INPUT_IMAGE_DIR + f.name, width=100, classes='m-2 p-2', a=file_data_div)
	response = await get_car_by_file(f.name)
	image.src=response
	textInput.div.text = f.name

jp.Img(src="/static/web_images/carsearch_logo.png", a=webp)
textInput = jp.InputChangeOnly(placeholder="enter search text",a=webp)
textInput.div = jp.Div(text="Last search appears here",a=webp)
fileInput = jp.Input(type='file', classes=jp.Styles.input_classes,
					a=webp, multiple=False, change=file_input_handler)
fileInput.file_div = jp.Div(a=webp)
image = jp.Img(classes='m-2 p-2', a=webp, width=600)

async def search():
	textInput.on('change', search_handler)

	return webp

jp.justpy(search)
