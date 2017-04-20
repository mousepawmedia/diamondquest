"""
Menus [DiamondQuest 2.0]
All the different game menus, titles, and whatnot.

Author(s): Jason C. McDonald
"""

import curses
from diamondquest.helpful import displays

class MainMenu:
    """
    DiamondQuest's main menu, including title credits.
    """

    def __init__(self, screen):
        # Store the screen
        self.screen = screen
        # Create new credit reel display.
        self.reel = displays.CreditReel(self.screen)
        # Create new hoverable menu.
        self.hovermenu = displays.HoverMenu(self.screen)
        # Initialize the title as unshown.
        self.is_title_shown = False

    def show(self):
        """
        Display the menu, returning the selected option number.
        """

        # Show the title, if we haven't already.
        if self.is_title_shown is False:
            self._title()

        # Clear the screen.
        self.screen.clear()
        self.screen.refresh()

        # Display the menu, returning the selected option.
        return self._menu()


    def _menu(self):
        """
        Display the menu.
        """
        self.hovermenu.addtitleline("DIAMONDQUEST 2.0", 0, curses.A_BOLD)
        self.hovermenu.addtitleline("---------------------------", 0.1)
        # Option 0
        self.hovermenu.addmenuline("New Game", 0.1)
        # Option 1
        self.hovermenu.addmenuline("High Scores", 0.1)
        # Option 2
        self.hovermenu.addmenuline("Credits", 0.1)
        # Option 3
        self.hovermenu.addmenuline("Quit", 0.1)

        # Give the menu control.
        return self.hovermenu.interactive_mode()

    def _title(self):
        """
        Display the game title.
        """
        # Show opening credits, with delays after each credit line.
        self.reel.addline("      __________________        ")
        self.reel.addline("    .-'  \\ _.-''-._ /  '-.     ")
        self.reel.addline("  .-/\\   .'.      .'.   /\\-.  ")
        self.reel.addline(" _'/  \\.'   '.  .'   './  \\'_ ")
        self.reel.addline(":======:======::======:======:  ")
        self.reel.addline(" '. '.  \\     ''     /  .' .'  ")
        self.reel.addline("   '. .  \\   :  :   /  . .'    ")
        self.reel.addline("     '.'  \\  '  '  /  '.'      ")
        self.reel.addline("       ':  \\:    :/  :'        ")
        self.reel.addline("         '. \\    / .'          ")
        self.reel.addline("           '.\\  /.'            ")
        self.reel.addline("             '\\/'              ")
        self.reel.addline("")
        self.reel.addline("DIAMONDQUEST 2.0", 1, curses.A_BOLD)
        self.reel.addline("by MousePaw Games", 1, curses.A_BOLD)
        self.reel.addline("www.mousepawgames.com", 1)
        self.reel.addline("", 0)

        # This last line waits for keypress.
        self.reel.addwaitline("Press Any Key To Continue...", True)
        # Reset the reel, in case we need to redraw.
        self.reel.reset()
        # Don't repeat the title credits next time we show this menu instance.
        self.is_title_shown = True

    def reset(self, reshow_title=True):
        """
        Reset the menu.

        Parameters
        ------------------
        reshow_title : bool, optional
            If True, will reshow the title credits next time show() is called.
        """
        # If we were asked to reshow the title next time, be sure to
        # reset the title flag AND the title credits object itself.
        if reshow_title:
            self.is_title_shown = False
            self.reel.reset()
        # Reset the menu, so it can be redrawn properly.
        self.hovermenu.reset()

class GameCredits:
    """
    DiamondQuest's full game credits.
    """

    def __init__(self, screen):
        # Store the screen
        self.screen = screen
        # Create new credit reel display.
        self.reel = displays.CreditReel(self.screen)

    def display(self):
        """
        Display the game title.
        """
        # Show game credits.
        self.reel.addline("DiamondQuest, Version 2.0", 1, curses.A_BOLD)
        self.reel.addline("")
        self.reel.addline("Produced by MousePaw Games", 1)
        self.reel.addline("www.mousepawgames.com", 1)
        self.reel.addline("")
        self.reel.addline("Concept by Jason C. McDonald", 1)
        self.reel.addline("")
        self.reel.addline("PROGRAMMING", 1)
        self.reel.addline("Jason C. McDonald", 1)
        self.reel.addline("")
        self.reel.addline("ART AND DESIGN", 1)
        self.reel.addline("Interface Design: Jason C. McDonald", 1)
        self.reel.addline("Diamond ASCII Art: miK", 1)
        self.reel.addline("Additional ASCII Art: Joan G Stark", 1)
        self.reel.addline("")
        self.reel.addline("EDUCATIONAL CONTENT", 1)
        self.reel.addline("Jason C. McDonald", 1)
        self.reel.addline("")
        self.reel.addline("TECHNOLOGY", 1)
        self.reel.addline("Written in Python 3", 1)
        self.reel.addline("Designed Using Curses for Python", 1)
        self.reel.addline("")
        self.reel.addline("Thanks for playing!", 1)
        self.reel.addline("", 0)
        # This last line waits for keypress.
        self.reel.addwaitline("Press Any Key To Continue...", True)
        self.reset()

    def reset(self):
        """
        Reset the game credits.
        """
        self.reel.reset()
