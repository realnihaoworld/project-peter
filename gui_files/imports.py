import kivy
import constants
import os.path

# for window size/to lock resizability
from kivy.core.window import Window
from kivy.config import Config

# All other Kivy imports.
from kivy.app import App
from kivy.lang import Builder                           # this allows to import .kv file
from kivy.uix.widget import Widget
from kivy.utils import colormap                         # dict of colors with names
from kivy.uix.floatlayout import FloatLayout

from kivy.properties import (ListProperty,            # in order to pass vars between .py
                             StringProperty,              # and .kv file, they have to be property objects
                             )
from kivy.clock import Clock

# Imports for individual widget types to be used
from kivy.graphics import Rectangle, Color


# playsound
from playsound import *

# TODO: import library to change sound device.

# for opening files
from tkinter.filedialog import askopenfilename