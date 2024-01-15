import tkinter as tk
import customtkinter as ctk

def switch_it():
	ctk.set_appearance_mode(is_dark.get())

window = ctk.CTk()
window.geometry('800x600')
window.bind('<Escape>', lambda event: window.quit())

is_dark = tk.StringVar()
switch = ctk.CTkSwitch(
	window, 
	text = 'testing', 
	variable = is_dark, 
	command = switch_it,
	onvalue = 'light',
	offvalue = 'dark'
)
switch.pack()



window.mainloop()