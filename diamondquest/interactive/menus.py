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
        Display the menu.
        """

        if self.is_title_shown is False:
            self._title()

        # Clear the screen and reset the reel.
        self.screen.clear()
        self.screen.refresh()

        # Display the menu.
        self._menu()


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
        # Don't repeat the title credits next time we show this menu instance.
        self.is_title_shown = True

class GameCredits:

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
        self.reel.addline("DIAMONDQUEST 2.0", 1, curses.A_BOLD)
        self.reel.addline("by MousePaw Games", 1, curses.A_BOLD)
        self.reel.addline("Concept and Programming by Jason C. McDonald", 1)
        self.reel.addline("Diamond ASCII art by miK", 1)
        self.reel.addline("Most Additional ASCII art by Joan G Stark", 1)
        self.reel.addline("", 0)
        # This last line waits for keypress.
        self.reel.addwaitline("Press Any Key To Continue...", True)
        self.reel.reset()
