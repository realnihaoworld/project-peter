"""
Description: Main file to run for GUI
"""

# the imports are all in a seperate file to declutter
from imports import *
from widget_classes import *

##########################################################################
# Main Applicaiton
##########################################################################

class ProtoypeGUIApp(App):
    # establishes constants as property objects for kivy.
    SIZE = ListProperty(constants.SIZE)
    COLOR = StringProperty(constants.COLOR)
    ACCENT_COLOR = ListProperty(constants.ACCENT_COLOR)
    status_color = ListProperty(constants.STANDBY_COLOR)
    status = StringProperty("STANDBY")

    def build(self):
        # window setup, options in constants.py
        Window.size = constants.SIZE

        # establishing layout + frame
        layout = FloatLayout(size=constants.SIZE)
        # background in maingui.kv file
        bg = MainGUI()
        set = SettingBox()
        web = WebBox()
        title = TitleBox()
        stat = StatusBox()

        # adding setting buttons/inputs
        setting_commands = SettingButtons()

        # adding widgets to layout
        layout.add_widget(bg)
        layout.add_widget(set)
        layout.add_widget(web)
        layout.add_widget(title)
        layout.add_widget(stat)
        layout.add_widget(setting_commands)

        return layout

    def dock_toggle(self):
        if self.status_color == constants.ON_COLOR:
            self.status_color = constants.OFF_COLOR
            self.status = "OFF"
        else:
            self.status_color = constants.ON_COLOR
            self.status = "ON"

# loading the style from the main file. It is done after the fact because
# otherwise the constants don't exist as objects yet to be used.
mainGUI_style = Builder.load_file("maingui.kv")

g = ProtoypeGUIApp()
g.run()
