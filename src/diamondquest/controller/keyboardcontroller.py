"""
The KeyboardController handles keyboard input events
"""



# Import the pygame module
import pygame.locals as KEYS
import pygame
from diamondquest.model.game import GameModel

from collections import deque

"""
    Enqueues action events on keydown, deques on key up.
    Sure there is a cleaner way to handle the if statements.
"""
actionQue = deque()
def inputHandling():
    for event in pygame.event.get():
        # Handle closure of window, may need a key
        # for accessability.
        if event.type == pygame.QUIT:
            return False
        if event.type == KEYS.KEYDOWN:
            actionQue.append(event.key)


        if event.type == KEYS.KEYUP:
            # Arrow keys
            if event.key == KEYS.K_UP:
                actionQue.remove(event.key)
            if event.key == KEYS.K_DOWN:
                actionQue.remove(event.key)
            if event.key == KEYS.K_LEFT:
                actionQue.remove(event.key)
            if event.key == KEYS.K_RIGHT:
                actionQue.remove(event.key)

        # Other items from above, tools, movement mode etc,
        # May not be needed if they aren't "repeatable"

        #print(actionQue)


    return True


def Notify(self, event):
    if isinstance(event, TickEvent):
        # Handle Input Events
        for event in pygame.event.get():
            pass
