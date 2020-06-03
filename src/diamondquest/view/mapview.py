import pygame
from diamondquest.view.window import Window, Views


# TODO: Load images into data structure (i.e. Mineral.png, Stone.png)
# TODO: Load character sprites (data structure as well?)
# TODO: Account for window resizing (rescaling the map to adapt)
# TODO: Queue function (e.g. spot (x,y) has changed, put in the queue -> see redraw())

class MapView:
    def redraw(x, y):
        # Multiple keys pressed: queue system
        """Grabs next thing in the queue
        (x, y): specific block at x, y
        (x, -1): entire column at row x
        (-1, y): entire row at column y
        (-1, -1): whole map
        """
        if x == -1 and y == -1:
            # Change whole map
        else if x != -1 and y == -1:
            # Change entire column at row x
        else if x == -1 and y != -1:
            # Change entire row at column y
        else:
            # Change specific block at x, y
        """Player movement r edraw handled as well (offset for smooth movement)
        Use percentage for offset (target pos +or- new pos * offset)
        """

    def draw_block(block, x, y):
        """Draw a single block on the screen.
        x - the x block position
        y - the y block position
        """

# where the anchor is, current state, x location, y location
    def redraw_avatar(x, y):
        """Redraws the avatar as they move"""

    def redraw_map():
        """Walking off-screen:
        Miner walks off of the screen, whole screen shifts
        """
