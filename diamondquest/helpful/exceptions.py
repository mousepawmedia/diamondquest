"""
Exceptions [DiamondQuest 2.0]
Special exceptions.

Author(s): Jason C. McDonald
"""

class ConsoleSizeException(Exception):
    """
    The console is the wrong size for the game.
    """
    # See http://stackoverflow.com/a/1319675/472647
    def __init__(self, message=""):
        if message == "":
            message = "The screen is too small! The console must be at least \
80x24. Resize and try again."
        # Call the base class constructor with the parameters it needs
        super().__init__(message)


class EscException(Exception):
    """
    If Esc is pressed, this is thrown.
    """
    def __init__(self, message=""):
        if message == "":
            message = "The escape key was pressed, but not properly handled."
        # Call the base class constructor with the parameters it needs.
        super().__init__(message)
