# Kivy genuinely require this many different import statements. I agree
# that it is confusing. -- Lily Williams

import kivy
from kivy.app import App
from kivy.lang import Builder                           # this allows to import .kv file
from kivy.uix.widget import Widget                      # allows .kv file to be displayed
from kivy.utils import colormap                         # dict of colors with names

from kivy.properties import (ObjectProperty,            # in order to pass vars between .py
                             ListProperty,              # and .kv file, they have to be property objects
                             NumericProperty,
                             ReferenceListProperty,
                             StringProperty)

from kivy.uix.floatlayout import FloatLayout            # this is the style of layout

# Imports for individual widget types to be used
from kivy.uix.button import Button                      # Kivy buttons
from kivy.graphics import Rectangle, Color              # this is for the canvas object, which operates
                                                        # as a graphic background.

import constants                                        # py fule for constants


class MainGUI(Widget):
    """
    has to be stated as a class in the main file.

    Note: Kivy has a specific naming scheme for files/classes, that is why the capitalization is not
            consistent.
    """
    pass


##########################################################################
# MAIN GUI
##########################################################################


class MainApp(App):
    # establishes constants as property objects for kivy.
    SIZE = ListProperty(constants.SIZE)
    SETTING_POS = ListProperty(constants.SETTING_POS)
    TITLE_POS = ListProperty(constants.TITLE_POS)
    STATUS_POS = ListProperty(constants.STATUS_POS)
    ACTIVITY_POS = ListProperty(constants.ACTIVITY_POS)
    COLOR = StringProperty(constants.COLOR)

    def build(self):

        # layout formatting
        layout = FloatLayout(size=constants.SIZE)

        m = MainGUI()

        layout.add_widget(m)

        return layout


# loading the style from the main file. It is done after the fact because
# otherwise the constants don't exist as objects yet to be used.
mainGUI_style = Builder.load_file("maingui.kv")

g = MainApp()
g.run()
