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

    main_menu = menus.MainMenu(screen)
    game_credits = menus.GameCredits(screen)

    while True:
        # Display main menu.
        option = main_menu.show()

        # Start the game.
        if option == 0:
            return
        # Display the high scores.
        elif option == 1:
            return
        # Show the credits.
        elif option == 2:
            game_credits.display()
        # Quit the game
        elif option == 3:
            return

    # The wrapper handles exiting correctly.


if __name__ == "__main__":
    # Start curses in the wrapper. This will turn on noecho() and cbreak(),
    # generate a keypad, and turn on formatting. A curses screen is created
    # and passed to main.
    curses.wrapper(startup)
