"""
Displays [DiamondQuest 2.0]
Common ways of displaying information on the screen using curses.

Author(s): Jason C. McDonald
"""

import time

class CreditReel:
    """
    An instance of a 'credit reel' display, which displays text
    centered on the screen, starting from the top row and moving
    down. I plan to do this style of display somewhat frequently.
    """

    def __init__(self, screen):
        """
        Initialize a new CreditReel on the given curses screen.
        """
        # Store the screen instance we're working on.
        self.screen = screen
        # Start our row incrementer.
        self.row = 0
        # Store the width, used in calcuating how to center the text.
        self.cols = screen.getmaxyx()[1]

    def addline(self, text, timeout=0, attr=None):
        """
        Add a line of text to the current credit reel, with an optional
        display delay (timeout). A newline is automatically appended.
        """
        # Add the line of text to the screen.
        if attr is None:
            self.screen.addstr(self.row, self.cols // 2 - len(text) // 2, \
                               text + "\n")
        else:
            self.screen.addstr(self.row, self.cols // 2 - len(text) // 2, \
                               text + "\n", attr)
        # Display the line of text.
        self.screen.refresh()
        # Increment row counter.
        self.row = self.row + 1
        if timeout > 0:
            time.sleep(timeout)

    def reset(self):
        """
        Reset the row count.
        """
        self.row = 0
