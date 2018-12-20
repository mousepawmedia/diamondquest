"""
Main module and GUI for DiamondQuest.

Author(s): Jason C. McDonald
"""

import kivy
kivy.require('1.9.1')

from kivy.app import App
#from kivy.compat import PY2
from kivy.config import Config
from kivy.uix.floatlayout import FloatLayout


class DQWindow(FloatLayout):
    """
    Parent class for the app
    """
    pass


class DQApp(App):
    """
    Application-level class, builds the application
    """

    def build_config(self, config):
        """
       Configure the application.
       """

        # Prevent the window from resizing too small. (SDL2 windows only).
        Config.set('graphics', 'minimum_width', '500')
        Config.set('graphics', 'minimum_height', '300')

    def build(self):
        """
       This function starts the application by constructing
       it from widgets and properties.
       """

        # Set the title and icon.
        self.title = "DiamondQuest"
        #self.icon = "icons/app/elements_icon_512.png"

        # Create the window.
        dq_app = DQWindow()
        return dq_app

if __name__ == '__main__':
    DQApp().run()
