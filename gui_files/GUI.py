"""
Description: Main file to run for GUI
"""

# the imports are all in a seperate file to declutter
from imports import *

##########################################################################
# Widget Classes
##########################################################################

# All of the custom widgets/visuals have to be stated as classes
# The only things they contain are widget specific functions and variables.

class MainGUI(FloatLayout):
    """
    main background
    """

class TitleBox(Widget):
    """
    rounded box that contains title
    """

class SettingBox(Widget):
    """
    left box containing setting, just background.
    """

class SettingButtons(Widget):
    """
    buttons/inputs inside settings box
    """

class WebBox(Widget):
    """
    main box that contains list of good/bad websites. lists are pulled
    from websites.txt files
    """

    # i am aware that this is repetetive, it will be better later
    txt = open(os.path.join("websites", "good_websites.txt")).readlines()
    good_web = ""
    for website in txt:
        print(website[0:4])
        if website[:4] == "www.":
            good_web += f"{website[4:]}"
        else:
            good_web += f"{website}"

    txt = open(os.path.join("websites", "bad_websites.txt")).readlines()
    bad_web = ""
    for website in txt:
        print(website[0:4])
        if website[:4] == "www.":
            bad_web += f"{website[4:]}"
        else:
            bad_web += f"{website}"


class StatusBox(Widget):
    """
    bottom box that displays status.
    launches in standby
    """


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
