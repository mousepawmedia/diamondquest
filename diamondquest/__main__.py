"""
DiamondQuest 2.0
Main module.

Author(s): Jason C. McDonald
"""

# For this application, I'll be using ncurses.
# https://docs.python.org/3/howto/curses.html
import curses
from diamondquest.interactive import menus

def startup(screen):
    """
    The main function for DiamondQuest, which will be used to call everything
    else and manage overall program execution. This must be started via
    'curses.wrapper(main)' to work correctly.
    """

    # Hide the blinking cursor by default.
    curses.curs_set(False)

    menus.title(screen)

    # Wait for a key press.
    screen.getch()
    # The wrapper handles exiting correctly.


if __name__ == "__main__":
    # Start curses in the wrapper. This will turn on noecho() and cbreak(),
    # generate a keypad, and turn on formatting. A curses screen is created
    # and passed to main.
    curses.wrapper(startup)
