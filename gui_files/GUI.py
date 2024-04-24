"""
Description: Main file to run for GUI
"""

# the imports are all in a seperate file to declutter
from imports import *
from widget_classes import *

# temp, this var would be from the extension
WEBSITE = "tumblr.com"

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

        self.good_sound = ""
        self.bad_sound = ""

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

        # schedule check event forever
        event = Clock.schedule_interval(self.check_website, 1)

        return layout

    def check_website(self, dt):
        if self.status == "ON":
            if WEBSITE in WebBox.good_web:
                self.play_good_sound()
            elif WEBSITE in WebBox.bad_web:
                self.play_bad_sound()

    def dock_toggle(self):
        if self.status_color == constants.ON_COLOR:
            self.status_color = constants.OFF_COLOR
            self.status = "OFF"
        else:
            self.status_color = constants.ON_COLOR
            self.status = "ON"

    def set_good_sound(self):
        filename = askopenfilename()
        self.good_sound = filename

    def set_bad_sound(self):
        filename = askopenfilename()
        self.bad_sound = filename

    def play_bad_sound(self):
        #playsound(self.bad_sound)
        print("bad sound")

    def play_good_sound(self):
        #playsound(self.good_sound)
        print("good sound")

# loading the style from the main file. It is done after the fact because
# otherwise the constants don't exist as objects yet to be used.
mainGUI_style = Builder.load_file("maingui.kv")

g = ProtoypeGUIApp()
g.run()
