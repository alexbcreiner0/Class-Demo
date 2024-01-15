import customtkinter as ctk
import darkdetect
from settings import *
from buttons import Button, TexButton, NumButton, MathButton
# these are windows specific modules, so it's in a try except to not crash for mac-users
try:
	from ctypes import windll, byref, sizeof, c_int
except:
	pass

class Calculator(ctk.CTk):
	def __init__(self, is_dark):
		
		# setup
		super().__init__(fg_color = (WHITE, BLACK))
		
		ctk.set_appearance_mode(f'{"dark" if is_dark else "light"}')
		self.geometry(f'{APP_SIZE[0]}x{APP_SIZE[1]}')
		self.resizable(False, False)
		self.title("")
		self.title_bar_color(is_dark)

		# grid layout
		# 7 rows, 4 columns. Botton 5 rows are the buttons, top 2 are the IO screen
		# Top row of the screen is the input, bottom is the output
		self.rowconfigure(list(range(MAIN_ROWS)), weight = 1, uniform = 'a')
		self.columnconfigure(list(range(MAIN_COLUMNS)), weight = 1, uniform = 'a')

		# data
		self.just_equated = True
		self.result_string = ctk.StringVar(value = '0')
		self.formula_string = ctk.StringVar(value = '')
		self.display_nums = [] # list with every digit on the lower display
		self.full_operation = [] # list which contains the expression displayed on upper display

		# widgets
		self.create_widgets()

		# key bindings
		self.bind('<Key>', self.keyboard_response)
		self.bind('<Return>', lambda event: self.math_press('='))
		self.bind('<Escape>', lambda event: self.quit())

		self.mainloop()

	def create_widgets(self):
		# font
		main_font = ctk.CTkFont(family = FONT, size = NORMAL_FONT_SIZE)
		result_font = ctk.CTkFont(family = FONT, size = OUTPUT_FONT_SIZE)

		# output labels
		OutputLabel(self, 0, 'se', main_font, self.formula_string) # formula
		OutputLabel(self, 1, 'e', result_font, self.result_string) # result

		# clear (AC) button
		Button(
			parent = self,
			func = self.clear, 
			text = OPERATORS['clear']['text'], 
			col = OPERATORS['clear']['col'], 
			row = OPERATORS['clear']['row'],
			font = main_font)

		# +/- ('invert') button
		TexButton(
			parent = self,
			func = self.invert,
			latex = '$+/-$',
			path = OPERATORS['invert']['image_path'],
			col = OPERATORS['invert']['col'],
			row = OPERATORS['invert']['row']
			)

		# percentage button
		Button(
			parent = self,
			func = self.percent,
			text = OPERATORS['percent']['text'],
			col = OPERATORS['percent']['col'],
			row = OPERATORS['percent']['row'],
			font = main_font)

		# number buttons
		for num, data in NUM_POSITIONS.items():
			span = 2 if num == 0 else 1
			NumButton(
				parent = self,
				text = num,
				func = self.num_press,
				col = data['col'],
				row = data['row'],
				font = main_font,
				span = span
			)

		# math buttons
		for key, data in MATH_POSITIONS.items():
			MathButton(
				parent = self,
				latex = key,
				path = MATH_POSITIONS[key]['image_path'],
				color = 'orange',
				func = self.math_press,
				operator = MATH_POSITIONS[key]['operator'],
				col = MATH_POSITIONS[key]['col'],
				row = MATH_POSITIONS[key]['row']
			)

	def keyboard_response(self, event):
		try:
			num = int(event.char)
			self.num_press(event.char)
		except ValueError:
			if event.char in {'/','*','-','+'}: self.math_press(event.char)

	def math_press(self, value, event = None):
		# get the current number-string from the screen and put it in the data list
		current_number = ''.join(self.display_nums)

		if current_number: # there is a number entered
			# add the operation to the data list
			self.full_operation.append(current_number)
			if value != '=':
				# make a list with the current number (joined together from list as a string)
				#  and the operation, as a string
				self.full_operation.append(value)
				# clear the list (not what appears on screen)
				self.display_nums.clear()
				# clear the bottom output bar
				self.result_string.set('')
				# put that number in the bottom output bar in the top output bar along 
				#  with the operation.
				self.formula_string.set(' '.join(self.full_operation))
			else:
				formula = ' '.join(self.full_operation)
				result = eval(formula)

				# format the result
				if isinstance(result, float):
					if result.is_integer():
						result = int(result)
					else:
						result = round(result, 3)

				self.full_operation.clear()
				self.display_nums = [str(result)]

				self.formula_string.set(formula)
				self.result_string.set(result)
				self.just_equated = True

	def num_press(self, value):
		if self.just_equated:
			self.result_string.set('')
			self.display_nums.clear()
			self.just_equated = False

		# add the number to the list, then set the result string to display the number that 
		# is all of the numbers entered but concatenated together
		self.display_nums.append(str(value))
		full_number = ''.join(self.display_nums)
		self.result_string.set(full_number)

	def clear(self):
		self.result_string.set(0)
		self.formula_string.set('')

		self.display_nums.clear()
		self.full_operation.clear()

	def percent(self):
		if self.display_nums:
			current_number = float(''.join(self.display_nums))
			percent_number = current_number / 100

			self.display_nums = list(str(percent_number))
			self.result_string.set(''.join(self.display_nums))

	def invert(self):
		current_number = ''.join(self.display_nums)
		if current_number:
			# positive / negative
			if float(current_number) > 0:
				self.display_nums.insert(0, '-')
			else:
				del self.display_nums[0]
		self.result_string.set(''.join(self.display_nums))
		
	def title_bar_color(self, is_dark):
		# This is a function that hides the titlebar. No clue what's going on here. Doesn't seem to work.
		try:
			HWND = windll.user32.GetParent(self.winfo.id())
			DWMDWA_ATTRIBUTE = 35
			COLOR = TITLE_BAR_HEX_COLORS['dark'] if is_dark else TITLE_BAR_HEX_COLORS['light']
			windll.dwmapi.DwmSetWindowAttribute(HWND, DWMDWA_ATTRIBUTE, byref(c_int(COLOR)), sizeof(c_int))
		except:
			pass

class OutputLabel(ctk.CTkLabel):
	def __init__(self, parent, row, anchor, font, string_var):
		super().__init__(master = parent, font = font, textvariable = string_var)
		self.grid(column = 0, columnspan = 4, row = row, sticky = anchor, padx = 10)

if __name__ == '__main__':
	Calculator(True)

