# Kivy genuinely require this many different import statements. I agree
# that it is confusing. -- Lily Williams
import kivy
import constants

# for window size/to lock resizability
from kivy.core.window import Window
from kivy.config import Config

# WILL NOT CHANGE RESIZE OPTION IF ITS NOT HERE AND ALSO IN THE MAIN APP
kivy.config.Config.set('graphics', 'resizable', constants.RESIZEABLE)
Config.write()

# All other Kivy imports.
from kivy.app import App
from kivy.lang import Builder                           # this allows to import .kv file
from kivy.uix.widget import Widget
from kivy.utils import colormap                         # dict of colors with names
from kivy.uix.floatlayout import FloatLayout

from kivy.properties import (ObjectProperty,            # in order to pass vars between .py
                             ListProperty,              # and .kv file, they have to be property objects
                             NumericProperty,
                             ReferenceListProperty,
                             StringProperty)

# Imports for individual widget types to be used
from kivy.uix.button import Button
from kivy.graphics import Rectangle, Color              # this is for the canvas object, which operates
                                                        # as a graphic background.


##########################################################################
# Widget Classes
##########################################################################

class MainGUI(FloatLayout):
    """
    has to be stated as a class in the main file.

    Note: Kivy has a specific naming scheme for files/classes, that is why the capitalization is not
            consistent.
    """
    pass
class TitleBox(Widget):
    pass

class SettingBox(Widget):
    pass

class WebBox(Widget):
    pass

class StatusBox(Widget):
    pass



##########################################################################
# Main Applicaiton
##########################################################################

class ProjectPeterApp(App):
    # establishes constants as property objects for kivy.
    SIZE = ListProperty(constants.SIZE)
    COLOR = StringProperty(constants.COLOR)
    ACCENT_COLOR = ListProperty(constants.ACCENT_COLOR)

    status_color = ListProperty(constants.STANDBY_COLOR)

    def build(self):
        # window setup, options in constants.py
        Window.size = constants.SIZE
        kivy.config.Config.set('graphics', 'resizable', constants.RESIZEABLE)
        Config.write()

        # establishing layout + frame
        layout = FloatLayout(size=constants.SIZE)
        # background in maingui.kv file
        bg = MainGUI()
        set = SettingBox()
        web = WebBox()
        title = TitleBox()
        stat = StatusBox()

        # adding widgets to layout
        layout.add_widget(bg)
        layout.add_widget(set)
        layout.add_widget(web)
        layout.add_widget(title)
        layout.add_widget(stat)

        return layout


# loading the style from the main file. It is done after the fact because
# otherwise the constants don't exist as objects yet to be used.
mainGUI_style = Builder.load_file("maingui.kv")

g = ProjectPeterApp()
g.run()
