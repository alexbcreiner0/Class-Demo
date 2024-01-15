from customtkinter import CTkButton, CTkImage
from settings import *
from PIL import Image, ImageTk
import matplotlib
from matplotlib import pyplot as plt
from pdf2image import convert_from_path

matplotlib.use('tkagg')

def latex_image(text, color, light_dark, png_path):
	fig = plt.figure()
	plt.axis('off')
	plt.text(
		x = 0.5,
		y = 0.5,
		s = f'{text}',
		fontsize = 'x-large',
		ha = 'center', 
		color = COLORS[color]['text'][light_dark]
	)
	plt.savefig(
		png_path,
		format = 'png', 
	    bbox_inches = 'tight',
	    transparent = True
	    )
	image = Image.open(png_path)
	return image

class Button(CTkButton):
	def __init__(self, parent, text, func, col, row, font, color = 'dark-gray', span = 1):
		super().__init__(
			master = parent,
			command = func,
			text = text,
			corner_radius = STYLING['corner-radius'],
			font = font,
			fg_color = COLORS[color]['fg'],
			hover_color = COLORS[color]['hover'],
			text_color = COLORS[color]['text'],
		)
		self.grid(
			column = col, 
			row = row, 
			sticky = 'NSEW', 
			padx = STYLING['gap'], 
			pady = STYLING['gap'],
			columnspan = span
		)
class NumButton(Button):
	def __init__(self, parent, text, func, col, row, font, color = 'light-gray', span = 1):
		super().__init__(
			parent = parent, 
			text = text, 
			func = lambda: func(text), 
			col = col, 
			row = row, 
			font = font, 
			color = color,
			span = span
		)
class TexButton(CTkButton):
	def __init__(self, parent, latex, func, col, row, path, color = 'dark-gray'):
		light_path = path + '_light.png'
		dark_path = path + '_dark.png'
		label_image_light = latex_image(latex, color, 0, light_path)
		label_image_dark = latex_image(latex, color, 1, dark_path)
		label_image_ctk = CTkImage(
            light_image = label_image_light,
            dark_image = label_image_dark,
            size = (500,500)
        )
		super().__init__(
			master = parent,
			command = func,
			image = label_image_ctk,
			text = '',
			corner_radius = STYLING['corner-radius'],
			fg_color = COLORS[color]['fg'],
			hover_color = COLORS[color]['hover'],
			text_color = COLORS[color]['text']
			)
		self.grid(column = col, row = row, sticky = 'NSEW', padx = STYLING['gap'], pady = STYLING['gap'])
class MathButton(TexButton):
	def __init__(self, parent, latex, func, col, row, path, operator, color):
		super().__init__(
			parent = parent, 
			latex = latex, 
			func = lambda: func(operator), 
			col = col, 
			row = row, 
			path = path, 
			color = color
		)
		