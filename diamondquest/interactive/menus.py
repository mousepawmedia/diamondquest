"""
Menus [DiamondQuest 2.0]
All the different game menus, titles, and whatnot.

Author(s): Jason C. McDonald
"""

import curses
from diamondquest.helpful import displays

def title(screen):
    """
    Display the game title.
    """
    # Create new credit reel display.
    reel = displays.CreditReel(screen)

    # Show opening credits.
    reel.addline("      __________________        ")
    reel.addline("    .-'  \\ _.-''-._ /  '-.     ")
    reel.addline("  .-/\\   .'.      .'.   /\\-.  ")
    reel.addline(" _'/  \\.'   '.  .'   './  \\'_ ")
    reel.addline(":======:======::======:======:  ")
    reel.addline(" '. '.  \\     ''     /  .' .'  ")
    reel.addline("   '. .  \\   :  :   /  . .'    ")
    reel.addline("     '.'  \\  '  '  /  '.'      ")
    reel.addline("       ':  \\:    :/  :'        ")
    reel.addline("         '. \\    / .'          ")
    reel.addline("           '.\\  /.'            ")
    reel.addline("             '\\/'              ")
    reel.addline("")
    reel.addline("DIAMONDQUEST 2.0", 1, curses.A_BOLD)
    reel.addline("by MousePaw Games", 1, curses.A_BOLD)
    reel.addline("www.mousepawgames.com", 1)
    reel.addline("", 0)
    reel.addline("Concept and Programming by Jason C. McDonald", 1)
    reel.addline("Diamond ASCII art by miK", 1)
    reel.addline("Most Additional ASCII art by Joan G Stark", 1)
    reel.addline("", 0)
