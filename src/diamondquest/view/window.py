from enum import Enum
import pygame
from .interface import color
from .mapview import MapView

# Reminder from Anne, staff: LOG YOUR HOURS. Thanks :) (This one is E733)


class Views(Enum):
    MAP = 1
    MENU = 2
    MATH = 3


class Window:
    shadowed = False
    views = Views.MAP
    
    # contains cached versions of the surfaces
    surface_cache = [None, None, None]

    @classmethod
    def draw_window(cls, width=640, height=480, caption="DiamondQuest", color=color.black):
        # TODO: Can we resize the window dynamically, or does the code need to handle that?
        screen = pygame.display.set_mode((width, height))

        pygame.display.set_caption(caption)
        screen.fill(color)

        pygame.display.flip()

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
