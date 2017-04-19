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

        Parameters
        -------------------
        screen : curses window
            The curses window to display on.
        """
        # Store the screen instance we're working on.
        self.screen = screen
        # Start our row incrementer.
        self.row = 0
        # Store the width, used in calcuating how to center the text.
        self.cols = screen.getmaxyx()[1]

    def _centerplaceline(self, text, attr=None):
        """
        Add the line of text to the screen.

        Parameters
        -------------------
        text : str
            The text to display.
        attr : curses attributes, optional
            The attributes to apply to the text.
        """
        if attr is None:
            self.screen.addstr(self.row, self.cols // 2 - len(text) // 2, \
                               text + "\n")
        else:
            self.screen.addstr(self.row, self.cols // 2 - len(text) // 2, \
                               text + "\n", attr)
        self.screen.refresh()

    def addline(self, text, timeout=0, attr=None):
        """
        Add a line of text to the current credit reel, with an optional
        display delay (timeout). A newline is automatically appended.

        Parameters
        -------------------
        text : str
            The text to be displayed. Be sure to OMIT the newline!
        timeout : int, optional
            How many seconds to pause before displaying the next line. Default 0.
        attr : curses attributes, optional
            The attributes to apply to the text.
        """
        # Display the line of text.
        self._centerplaceline(text, attr)

        # Increment row counter.
        self.row = self.row + 1

        # Sleep, if requested.
        if timeout > 0:
            time.sleep(timeout)

    def addwaitline(self, text, blink, attr=None):
        """
        Display the last line of text for the credit reel. Simulates blinking,
        since the A_BLINK attribute doesn't work on some terminals (due to
        an unresolved 2010 bug in VTE: https://bugs.launchpad.net/ubuntu/+source/vte/+bug/590735)

        Parameters
        -------------------
        text : str
            The text to be displayed. Be sure to OMIT the newline!
        blink : bool
            Whether to cause the line to blink.
        attr : curses attributes, optional
            The attributes to apply to the text.

        Return
        --------------------
        The keypress returned by screen.getch().
        """

        # Display the line of text initially.
        self._centerplaceline(text, attr)

        if blink:
            # Don't pause waiting for keypress.
            self.screen.nodelay(True)
            key = -1
            while key == -1:
                # Display the line of text.
                self._centerplaceline(text, attr)

                # Check for keypress before first pause.
                key = self.screen.getch()
                if key != -1:
                    break
                time.sleep(0.5)

                # Clear the line of text.
                self.screen.move(self.row, 0)
                self.screen.clrtoeol()
                self.screen.refresh()

                # Check for keypress before second pause.
                key = self.screen.getch()
                if key != -1:
                    break
                time.sleep(0.5)
        else:
            # No blinking effect, just wait for keypress.
            key = self.screen.getch()

        return key

    def reset(self):
        """
        Reset the row count.
        """
        self.row = 0
