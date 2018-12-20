"""
Displays [DiamondQuest 2.0]
Common ways of displaying information on the screen using curses.

Author(s): Jason C. McDonald
"""

import time
import curses
from diamondquest.helpful import data, exceptions

class DebugText:
    """
    Display a line of text on the bottom of the screen.
    """

    def __init__(self, screen):
        # Store the screen instance we're working on.
        self.screen = screen
        # Store the last row.
        self.row = screen.getmaxyx()[0] - 1

    def output(self, text):
        """
        Print the given line to the debug row.
        """
        self.clear()
        self.screen.addstr(self.row, 0, text)

    def clear(self):
        """
        Clear the debug row.
        """
        self.screen.move(self.row, 0)
        self.screen.clrtoeol()
        self.screen.refresh()

class Teletype:
    """
    Display text with gradual reveal.
    """

    def __init__(self, screen):
        """
        Initialize a new Teletype display on the given curses screen.
        """
        # Store the screen instance we're working on.
        self.screen = screen
        # Start our row incrementer.
        self.row = 0
        # Store the size of the console.
        self.rows = screen.getmaxyx()[0]
        self.cols = screen.getmaxyx()[1]

    def addline(self, text, delay=0.1, attr=None):
        """
        Display the given line of text on the teletype display.

        Parameters
        --------------
        text : str
            The string to display
        delay : float, optional
            The delay in seconds between showing each letter, default 0.1.
        attr : curses attributes, optional
            The attributes to apply to the text.
        """
        # If we're out of space, clear the screen and reset our row count.
        if self.row >= self.rows:
            self.screen.clear()
            self.reset()

        col = 0
        for char in text:
            col = col + 1
            #Loop through and display each, with a delay.
            if attr is None:
                self.screen.addch(self.row, col, char)
            else:
                self.screen.addch(self.row, col, char, attr)
            self.screen.refresh()
            # Sleep, if requested.
            if delay > 0:
                time.sleep(delay)


    def reset(self):
        """
        Reset the teletype display.
        """
        self.row = 0

class HoverMenu:
    """
    A selectable menu.
    """

    def __init__(self, screen):
        """
        Initialize a new HoverMenu on the given curses screen.
        """
        # Store the screen instance we're working on.
        self.screen = screen
        # Start our row incrementer.
        self.row = 0
        # Store the width, used in calcuating how to center the text.
        self.cols = screen.getmaxyx()[1]

        # Define data
        self.data = data.MenuStructure()

    def _centerplaceline(self, text, attr=None, row=-1):
        """
        Add the line of text to the screen.

        Parameters
        -------------------
        text : str
            The text to display.
        attr : curses attributes, optional
            The attributes to apply to the text.
        """
        if row == -1:
            row = self.row

        if attr is None:
            self.screen.addstr(row, self.cols // 2 - len(text) // 2, \
                               text + "\n")
        else:
            self.screen.addstr(row, self.cols // 2 - len(text) // 2, \
                               text + "\n", attr)
        self.screen.refresh()

    def _rewriteline(self, text, row, highlight):
        """
        Rewrite the specified row with the given text.
        """
        # Clear the row. The call to the function to write the text will
        # handle the 'screen.refresh()'.
        self.screen.move(self.row, 0)
        self.screen.clrtoeol()

        # Rewrite the row, using highlighting or no highlighting, depending
        # on what was requested.
        if highlight:
            self._centerplaceline(text, curses.A_STANDOUT, row)
        else:
            self._centerplaceline(text, None, row)


    def addtitleline(self, text, timeout=0, attr=None):
        """
        Add a plain line of text to the current menu, with an optional
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

    def addmenuline(self, text, timeout=0):
        """
        Add a selectable line of text to the current menu, with an optional
        display delay (timeout). A newline is automatically appended.
        Attributes aren't currently supported for this command.

        Parameters
        -------------------
        text : str
            The text to be displayed. Be sure to OMIT the newline!
        timeout : int, optional
            How many seconds to pause before displaying the next line. Default 0.
        """
        # Display the line of text.
        self._centerplaceline(text)

        # Add text to menu data.
        self.data.add_item(text, self.row)

        # Increment row counter.
        self.row = self.row + 1

        # Sleep, if requested.
        if timeout > 0:
            time.sleep(timeout)

    def interactive_mode(self):
        """
        Handoff control to the menu. You MUST have at least one selectable
        item in the menu, added via 'addmenuline()', or an exception will
        be thrown.
        """
        # If there are no menu items and we call this, we did something stupid.
        if self.data.selected == -1:
            raise RuntimeError("You cannot switch to interactive mode on a \
                               menu which has no selectable items.")
        else:
            # We will loop until we exit after selecting an item.
            while True:
                # Highlight current hover.
                self._rewriteline(self.data.get_current()[0], self.data.get_current()[1], True)
                # If we haven't yet selected anything, don't reformat previous item.
                # Otherwise...
                if self.data.selected != self.data.last_selected:
                    # Unhighlight prior hover.
                    self._rewriteline(self.data.get_prior()[0], self.data.get_prior()[1], False)

                # Listen for key presses.
                key = self.screen.getch()

                if key == curses.KEY_UP:
                    self.data.nav_prev()
                elif key == curses.KEY_DOWN:
                    self.data.nav_next()
                # NOTE: WE use '10' (line break) instead of the more unreliable
                # constant 'curses.KEY_ENTER'.
                elif key == 10:
                    # Get the selected option BEFORE destroying the data.
                    option = self.data.nav_select()
                    # We must reset the menu before leaving it,
                    # or it will redraw wrong later.
                    self.reset()
                    return option

    def reset(self):
        """
        Reset the menu, erasing all data and rows. We'll redraw later.
        """
        self.row = 0
        self.data = data.MenuStructure()


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
        # Store the height, so we can clear and keep going when we run out
        # of room.
        self.row_max = screen.getmaxyx()[0] - 1

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
        # If we're out of space, clear the screen and reset our row count.
        if self.row >= self.row_max:
            self.screen.clear()
            self.reset()

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
        # Don't pause waiting for keypress.
        self.screen.nodelay(True)

        # Display the line of text.
        self._centerplaceline(text, attr)

        # Increment row counter.
        self.row = self.row + 1

        # Sleep, if requested.
        if timeout > 0:
            time.sleep(timeout)

        key = self.screen.getch()

        # Restore waiting for keypress
        self.screen.nodelay(False)

        if key == 27:
            raise exceptions.EscException()

    def addwaitline(self, text, blink, attr=None):
        """
        Display a line of text for the credit reel that waits for key input.
        Simulates blinking, since the A_BLINK attribute doesn't work on some
        terminals (due to an unresolved 2010 bug in VTE:
        https://bugs.launchpad.net/ubuntu/+source/vte/+bug/590735)

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

        # Throw away any key presses that were prior to this.
        curses.flushinp()

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

        self.screen.nodelay(False)
        return key

    def reset(self):
        """
        Reset the row count.
        """
        self.row = 0
