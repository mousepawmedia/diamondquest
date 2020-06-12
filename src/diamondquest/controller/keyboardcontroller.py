"""
The KeyboardController handles keyboard input events
"""

# Import the pygame module
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    KEYUP,
    QUIT,
)
import pygame
from collections import deque

# This would probably be in state so the actions can be processed
# Unsure how that'll work or how communication works so just
# mocking things up here.
keyboardQueue = deque()

""" 
    Enqueues action events on keydown, deques on key up.
    Sure there is a cleaner way to handle the if statements.
"""


def inputHandling():
    for event in pygame.event.get():
        # Handle closure of window, may need a key
        # for accessability.
        if event.type == pygame.QUIT:
            return False
        if event.type == KEYDOWN:
            # Menu - Escape
            if event.key == K_ESCAPE:
                keyboardQueue.append("OPEN_MENU")

            # Arrow Keys - Action is contectual
            if event.key == K_UP:
                keyboardQueue.append("ARROW_UP")
            if event.key == K_DOWN:
                keyboardQueue.append("ARROW_DOWN")
            if event.key == K_LEFT:
                keyboardQueue.append("ARROW_LEFT")
            if event.key == K_RIGHT:
                keyboardQueue.append("ARROW_RIGHT")

            # Tools - Pickaxe, Drill, Hook, TNT, Scout

            # Movement Mode - Space

            # Power Level - 1 ... 8

            # Miner's Log - G or L

        if event.type == KEYUP:
            # Arrow keys
            if event.key == K_UP:
                keyboardQueue.remove("ARROW_UP")
            if event.key == K_DOWN:
                keyboardQueue.remove("ARROW_DOWN")
            if event.key == K_LEFT:
                keyboardQueue.remove("ARROW_LEFT")
            if event.key == K_RIGHT:
                keyboardQueue.remove("ARROW_RIGHT")

            # Other items from above, tools, movement mode etc,
            # May not be needed if they aren't "repeatable"

    return True


def Notify(self, event):
    if isinstance(event, TickEvent):
        # Handle Input Events
        for event in pygame.event.get():
            pass
