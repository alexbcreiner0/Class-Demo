# size
APP_SIZE = (400,700)
MAIN_ROWS = 7
MAIN_COLUMNS = 4

# text
FONT = 'Helvetica'
OUTPUT_FONT_SIZE = 70
NORMAL_FONT_SIZE = 32

STYLING = {
	'gap': 0.5,
	'corner-radius': 0
}

NUM_POSITIONS = {
	'.': {'col': 2, 'row': 6, 'span': 1},
	0: {'col': 0, 'row': 6, 'span': 2},
	1: {'col': 0, 'row': 5, 'span': 1},
	2: {'col': 1, 'row': 5, 'span': 1},
	3: {'col': 2, 'row': 5, 'span': 1},
	4: {'col': 0, 'row': 4, 'span': 1},
	5: {'col': 1, 'row': 4, 'span': 1},
	6: {'col': 2, 'row': 4, 'span': 1},
	7: {'col': 0, 'row': 3, 'span': 1},
	8: {'col': 1, 'row': 3, 'span': 1},
	9: {'col': 2, 'row': 3, 'span': 1}
}

MATH_POSITIONS = {
	'$\\div$': {'col': 3, 'row': 2, 'operator':'/', 'image_path': 'div'},
	'$\\times$': {'col': 3, 'row': 3, 'operator':'*', 'image_path': 'times'},
	'$-$': {'col': 3, 'row': 4, 'operator':'-', 'image_path': 'minus'},
	'$=$': {'col': 3, 'row': 6, 'operator':'=', 'image_path': 'equals'},
	'$+$': {'col': 3, 'row': 5, 'operator':'+', 'image_path': 'plus'}
}

OPERATORS = {
	'clear': {'col': 0, 'row': 2, 'text': 'AC', 'image_path': None},
	'invert': {'col': 1, 'row': 2, 'text': '', 'image_path': 'plus_minus'},
	'percent': {'col': 2, 'row': 2, 'text': '%', 'image_path': None}
}

# Each color is a tuple of hex codes; one for light mode, one for dark mode.
COLORS = {
	'light-gray': {'fg': ('#505050', '#D4D4D2'), 'hover': ('#686868','#EFEFED'), 'text': ('white','black')},
	'dark-gray': {'fg': ('#D4D4D2', '#505050'), 'hover': ('#EFEFED','#686868'), 'text': ('black','white')},
	'orange': {'fg': '#FF9500', 'hover': ('#EFEFED','#686868'), 'text': ('black', 'white')},
	'orange-highlight': {'fg': 'white', 'hover': 'white', 'text': ('black', '#FF9500')}
}

TITLE_BAR_HEX_COLORS = {
	'dark': 0x00000000,
	'light': 0x00EEEEEE
}

BLACK = '#000000'
WHITE = '#EEEEEE'