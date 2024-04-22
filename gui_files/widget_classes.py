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

    # TODO: MAKE IT A TXT INPUT THAT GETS WRITTEN

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