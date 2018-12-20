"""
Data [DiamondQuest 2.0]
Data structures unique to DiamondQuest.

Author(s): Jason C. McDonald
"""

class MenuStructure:
    """
    A navigable data structure for storing the data that makes up a menu,
    such as in displays.py.
    """

    def __init__(self):
        # Declare our selection markers with invalid defaults.
        self.selected = -1
        self.last_selected = -1
        # We'll store our menu item and their display rows strings in an array.
        self.data = []

    def add_item(self, text, row):
        """
        Add an item with the given text.
        """
        # Store the text and row in a tuple, and add to the data structure.
        self.data.append((text, row))
        # We can now select things.
        self.selected = 0
        self.last_selected = 0

    def nav_prev(self):
        """
        Go back an item, if possible. Returns False if we can't go back
        further, else True.
        """
        if self.selected > 0:
            self.last_selected = self.selected
            self.selected = self.selected - 1
            return True
        else:
            return False

    def nav_next(self):
        """
        Go forward an item, if possible. Returns False if we can't go forward
        further, else True.
        """
        if self.selected < (len(self.data) - 1):
            self.last_selected = self.selected
            self.selected = self.selected + 1
            return True
        else:
            return False

    def nav_select(self):
        """
        Returns the item id.
        """
        return self.selected

    def get_current(self):
        """
        Returns a tuple of the text and display row of the current item, used
        for modifying the display.
        """
        return self.data[self.selected]

    def get_prior(self):
        """
        Returns a tuple of the text and display row of the previous item, used
        for modifying the display.
        """
        return self.data[self.last_selected]
