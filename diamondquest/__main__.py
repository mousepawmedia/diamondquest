"""
DiamondQuest 2.0
Main module.

Author(s): Jason C. McDonald
"""

import os
# For this application, I'll be using ncurses.
# https://docs.python.org/3/howto/curses.html
import curses
from diamondquest.interactive import menus
from diamondquest.helpful import displays, exceptions

def startup(screen):
    """
    The main function for DiamondQuest, which will be used to call everything
    else and manage overall program execution. This must be started via
    'curses.wrapper(main)' to work correctly.
    """

    # Start by testing screen size.
    size = screen.getmaxyx()
    if size[0] < 24 or size[1] < 80:
        raise exceptions.ConsoleSizeException()

    # Hide the blinking cursor by default.
    curses.curs_set(False)

    main_menu = menus.MainMenu(screen)
    game_credits = menus.GameCredits(screen)

    debug = displays.DebugText(screen)

    while True:
        # Display main menu.
        option = main_menu.show()

        # Start the game.
        if option == 0:
            debug.output("Game: Not Yet Implemented")
            screen.getch()

        # Display the high scores.
        elif option == 1:
            debug.output("High Scores: Not Yet Implemented")
            screen.getch()

        # Show the credits.
        elif option == 2:
            # Clear the screen.
            screen.clear()
            screen.refresh()
            # Play the game credits.
            game_credits.display()

        # Quit the game
        elif option == 3:
            # Exit the game.
            break

    # The wrapper handles exiting correctly.
    return True


if __name__ == "__main__":
    # Remove delay for pressing Esc.
    os.environ.setdefault('ESCDELAY', '25')

    # Start curses in the wrapper. This will turn on noecho() and cbreak(),
    # generate a keypad, and turn on formatting. A curses screen is created
    # and passed to main.
    try:
        curses.wrapper(startup)
    except exceptions.ConsoleSizeException as error:
        print(error)
