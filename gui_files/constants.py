from kivy.utils import colormap
from random import randint

DEBUG = False

color_options = ["steelblue","sienna","thistle","olivedrab"]

# frame constants
SIZE = (800, 600)
COLOR = colormap[color_options[randint(0,3)]]
ACCENT_COLOR = colormap["snow"]
RESIZEABLE = True

# setting box
SETTING_POS = (100, 100)

# title box
TITLE_POS = (25, 475)

# status box
STATUS_POS = (10, 10)

# status colors
ON_COLOR = colormap["darkgreen"]
OFF_COLOR = colormap["darkred"]

# web activity
ACTIVITY_POS = (50, 50)


# adding comment for test commit
# everything is going well