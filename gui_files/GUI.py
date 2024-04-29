"""
Description: Main file to run for GUI
"""
# the imports are all in a seperate file to declutter
from imports import *
from widget_classes import *

# temp, this var would be from the extension
WEBSITE = "tiktok.com"

##########################################################################
# Main Applicaiton
##########################################################################


class ProtoypeGUIApp(App):

    # establishes constants as property objects for kivy.
    SIZE = ListProperty(constants.SIZE)
    COLOR = StringProperty(constants.COLOR)
    ACCENT_COLOR = ListProperty(constants.ACCENT_COLOR)
    status_color = ListProperty(constants.OFF_COLOR)

    def build(self):
        self.status = "OFF"

        # path to sound
        self.good_sound = ""
        self.bad_sound = ""

        # minute delay
        self.good_delay = 1
        self.bad_delay = 1

        # what time you started on that website
        self.good_website_time = 0.0
        self.bad_website_time = 0.0

        # if you are on that website and havent left
        self.started_on_good_website = False
        self.started_on_bad_website = False

        # window setup, options in constants.py
        Window.size = constants.SIZE

        # establishing layout + frame
        layout = FloatLayout(size=constants.SIZE)
        # background in maingui.kv file
        bg = MainGUI()
        setting = SettingBox()
        web = WebBox()
        title = TitleBox()
        stat = StatusBox()

        # adding setting buttons/inputs
        setting_commands = SettingButtons()

        # adding widgets to layout
        layout.add_widget(bg)
        layout.add_widget(setting)
        layout.add_widget(web)
        layout.add_widget(title)
        layout.add_widget(stat)
        layout.add_widget(setting_commands)

        # schedule check event forever
        Clock.schedule_interval(self.check_website, 1)

        return layout

    def check_website(self, dt):
        """
        Acts depending on what website you are on and how long you
        have been on it
        """
        current_time = time()
        if self.status == "ON":
            if (WEBSITE in WebBox.good_web):

                if self.started_on_good_website is False:
                    self.good_website_time = time()
                    self.started_on_good_website = True
                    self.started_on_bad_website = False

                time_since_stated = current_time - self.good_website_time

                if time_since_stated >= (self.good_delay * 60):
                    self.good_reaction()

            elif WEBSITE in WebBox.bad_web:
                if self.started_on_bad_website is False:
                    self.bad_website_time = time()
                    self.started_on_bad_website = True
                    self.started_on_good_website = False


                time_since_stated = current_time - self.bad_website_time

                if time_since_stated >= (self.bad_delay * 60):
                    self.bad_reaction()

            else:
                self.started_on_good_website = False
                self.started_on_bad_website = False

            if constants.DEBUG:
                print(f"current time: {current_time}")
                print(f"Time Started on Good: {self.good_website_time}")
                print(f"started on good? {self.started_on_good_website}")
                print(f"Good Delay: {type(self.good_delay)} : {self.good_delay * 60}")
                print(f"IS DONE?: {time_since_stated >= (self.good_delay * 60)}")
                print(f"Time Since Started: {type(time_since_stated)} : {time_since_stated}")
                print("#" * 50)

    def good_reaction(self):
        if constants.DEBUG: print("GOOD REACTION")
        self.started_on_good_website = False
        self.play_good_sound()

    def bad_reaction(self):
        if constants.DEBUG: print("BAD REACTION")
        self.started_on_bad_website = False
        self.play_bad_sound()

    # sets delay input
    def set_good_delay(self, delay_time):
        try:
            if 0.0 < float(delay_time) <= 60.0:
                self.good_delay = float(delay_time)
            else:
                raise ValueError

        except ValueError:
            print("ValueError: Invalid delay, must be 0-10")
            self.good_delay = 1.0

        finally:
            if constants.DEBUG: print("Good Delay:" + str(self.good_delay))

    def set_bad_delay(self, delay_time):
        try:
            if 0 < float(delay_time) <= 10:
                self.bad_delay = float(delay_time)
            else:
                raise ValueError

        except ValueError:
            print("ValueError: Invalid delay, must be 0-10")
            self.bad_delay = 1.0

        finally:
            if constants.DEBUG: print("Bad Delay:" + str(self.bad_delay))

    def set_good_sound(self):
        filename = askopenfilename()
        self.good_sound = filename

    def set_bad_sound(self):
        filename = askopenfilename()
        self.bad_sound = filename

    def play_bad_sound(self):
        # playsound(self.bad_sound)
        print("bad sound")

    def play_good_sound(self):
        # playsound(self.good_sound)
        print("good sound")

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
