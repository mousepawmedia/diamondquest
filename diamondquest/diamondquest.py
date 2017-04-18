"""
DiamondQuest 2.0
Main module.

Author(s): Jason C. McDonald
"""

# For this application, I'll be using ncurses.
# https://docs.python.org/3/howto/curses.html
import curses

def title():
    """
    Display the game title.
    """
    print("      __________________        ")
    print("    .-'  \\ _.-''-._ /  '-.     ")
    print("  .-/\\   .'.      .'.   /\\-.  ")
    print(" _'/  \\.'   '.  .'   './  \\'_ ")
    print(":======:======::======:======:  ")
    print(" '. '.  \\     ''     /  .' .'  ")
    print("   '. .  \\   :  :   /  . .'    ")
    print("     '.'  \\  '  '  /  '.'      ")
    print("       ':  \\:    :/  :'        ")
    print("         '. \\    / .'          ")
    print("           '.\\  /.'            ")
    print("             '\\/'              ")
    print("")
    print("DIAMONDQUEST 2.0")
    print("MousePaw Games")
    print("www.mousepawgames.com")
    print("----------------------------")
    print("Diamond ASCII art by miK")
    print("Most Additional ASCII art by Joan G Stark")
    print("----------------------------")


def newgame():
    """
    Display the menu for starting a new game.
    """
    print("New game!")

def highscores():
    """
    Display the high scores.
    """
    print("High scores!")

def menu():
    """
    Display the game menu.
    Returns false for quit, true for normal execution.
    """
    print("Select an option:")
    print("1) New Game")
    print("2) High Scores")
    print("3) Quit")
    option = input("Your Choice: ")
    if int(option) == 1:
        print("")
        newgame()
        return True
    elif int(option) == 2:
        print("")
        return True
    elif int(option) == 3:
        return False
    else:
        print("Invalid option.\n")
        return True

def main():
    """
    The main function for DiamondQuest, which will be used to call everything
    else and manage overall program execution.
    """
    ##title()
    ##doexit = menu()
    ##while doexit is True:
    ##    doexit = menu()

    # Create a curses screen.
    stdscr = curses.initscr()
    # Turn off automatic echoing of keys to the screen
    curses.noecho()
    # React to keys immediately instead of waiting for ENTER
    curses.cbreak()
    # Use the curses special key processing.
    stdscr.keypad(True)
    # Exit application.
    curses.endwin()

if __name__ == "__main__":
    main()
