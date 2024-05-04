"""
Layout and build of GUI

NOTE:
    If you are adding stuff to do after you've been on a good or negative site,
    add it to the "good_reaction" or "bad_reaction" functions.

    DANISON -- I have an empty self.website var and a get_website() function empty and set up rn but however
    you need to do your stuff.


other note. in order to test reaction you have to set the reaction sound. i have a sound file with a default
but its not working as a default yet.

"""

# the imports are all in a seperate file to declutter
from imports import *
from widget_classes import *


##########################################################################
# Main Applicaiton
##########################################################################


class ProductivityPalApp(App):

    # establishes constants as property objects for kivy.
    SIZE = ListProperty(constants.SIZE)
    COLOR = StringProperty(constants.COLOR)
    ACCENT_COLOR = ListProperty(constants.ACCENT_COLOR)
    status_color = ListProperty(constants.OFF_COLOR)
    status = StringProperty("OFF")

    def build(self):

        # website
        self.website = "tiktok.com" # PLACEHOLDER FOR TESTING

        # path to sound. THESE DONT WORK RIGHT NOW
        self.good_sound = os.path.join('sounds','positive_reaction_audio.wav')
        self.bad_sound = os.path.join('sounds','negative_reaction_audio.wav')

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
        Clock.schedule_interval(self.get_website, 1)

        return layout

    def get_website(self, dt):
        """
        Calls a function from the flask server that retrieves the current url the user is on
        
        note -- dt is a required input to schedule but it is not used
        """
        # use a get request to grab the url being tracked by the server
        url = requests.get('http://127.0.0.1:5000/get')
        
        self.website = url.text
        print(f"self.website: {self.website}")

    def check_website(self, dt):
        """
        Acts depending on what website you are on and how long you
        have been on it

        note -- dt is a required input to schedule but it is not used
        """
        current_time = time()
        if self.status == "ON" and type(self.website) == str:
            if (self.website in WebBox.good_web):
                # If on a productive website

                if self.started_on_good_website is False:       # if you just got on the site
                    self.good_website_time = time()             # gets the start time
                    self.started_on_good_website = True
                    self.started_on_bad_website = False

                if current_time - self.good_website_time >= (self.good_delay * 60):
                    # if you have been on the good site for the minutes indicated by the delay
                    self.good_reaction()

            elif self.website in WebBox.bad_web:
                # If on an unproductive website

                if self.started_on_bad_website is False:       # just entered the site
                    self.bad_website_time = time()             # start time
                    self.started_on_bad_website = True
                    self.started_on_good_website = False

                if current_time - self.bad_website_time >= (self.bad_delay * 60):
                    self.bad_reaction()

            else:
                # If you are on a site that is on neither list.
                self.started_on_good_website = False
                self.started_on_bad_website = False

    # reactions after delay
    def good_reaction(self):
        if constants.DEBUG: print("GOOD REACTION")
        self.started_on_good_website = False

        """
        This function is the reaction for being on a productive website
        for a given amount of time. any commands relating to how the
        bot itself should react should go in here. 
        """

        playsound(self.good_sound)
        print("good sound")

    def bad_reaction(self):
        if constants.DEBUG: print("BAD REACTION")
        self.started_on_bad_website = False

        """
        This function is the reaction for being on an unproductive website
        for a given amount of time. any commands relating to how the
        bot itself should react should go in here. 
        """

        playsound(self.bad_sound)
        print("bad sound")

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

    # sets the sound paths
    def set_good_sound(self):
        """
        sets the path to the sound file that is positive. there is a
        folder in the project titled "sound" to store these.
        """

        filename = askopenfilename()
        self.good_sound = filename

    def set_bad_sound(self):
        """
        sets the path to the sound file that is negative.
        """

        filename = askopenfilename()
        self.bad_sound = filename

    # toggles on/off
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
