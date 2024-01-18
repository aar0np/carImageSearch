import justpy as jp

from carServices import get_car_by_text

webp = jp.WebPage()
input1 = jp.InputChangeOnly(placeholder="enter search text",a=webp)
input1.div = jp.Div(text="Last search appears here",a=webp)
image = jp.Img(classes='m-2 p-2', a=webp)

async def search_handler(self, msg):
	self.div.text = self.value
	response = await get_car_by_text(self.value)
	image.src=response
	self.value = ""

async def search():
	input1.on('change', search_handler)

	return webp

jp.justpy(search)