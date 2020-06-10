import math
from enum import Enum

import pygame

from diamondquest.common import color
from diamondquest.common.constants import BLOCK_COUNT


class Views(Enum):
    MAP = 1
    MENU = 2
    MATH = 3


class Window:
    shadowed = False
    views = Views.MAP
    resolution = (800, 600)

    # contains cached versions of the surfaces
    surface_cache = [None, None, None]

    @classmethod
    def draw_window(
        cls, caption="DiamondQuest", color=color.sky
    ):
        # TODO: Can we resize the window dynamically, or does the code need to handle that?
        screen = pygame.display.set_mode(cls.resolution)

        pygame.display.set_caption(caption)
        screen.fill(color)

        pygame.display.flip()

    @classmethod
    def set_resolution(cls, width, height):
        cls.resolution = (width, height)
        
    @classmethod
    def get_block_height(cls):
        # TODO: Must eventually be guaranteed as a multiple of 16
        return math.floor(cls.resolution[1] / BLOCK_COUNT)

    @classmethod
    def draw_shadow(cls):
        """Draw a semi-transparent box over the entire screen"""
        # Should be safe to call multiple times; if already shadowed, does nothing.
        # Copy map surface

        # Draw to screen

    @classmethod
    def get_surface(cls, view):
        """Return the current surface for drawing on."""
        return cls.surface_cache[view]

    @classmethod
    def redraw_window(cls):
        """Force the entire window to redraw."""
        pygame.display.flip()
