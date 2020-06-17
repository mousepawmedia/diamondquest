from .keyboardcontroller import actionQue
import pygame.locals as KEYS
from diamondquest.model.game import GameModel
from diamondquest.common.mode import ModeType
from diamondquest.view.window import Window

def processAction():
    if ( GameModel.mode == ModeType.MENU):
        if ( actionQue ):
            action = actionQue.pop()

            # Resume Game
            if action == KEYS.K_1 or action == KEYS.K_ESCAPE:
                GameModel.mode = ModeType.MAP
                Window.hide_view(ModeType.MENU)


            # Handling arrows here
            # They are put back in front in case arrows are held down
            elif action == KEYS.K_UP:
               actionQue.appendleft(action)
            elif  action == KEYS.K_DOWN:
               actionQue.appendleft(action)
            elif action == KEYS.K_LEFT:
               actionQue.appendleft(action)
            elif action == KEYS.K_RIGHT:
               actionQue.appendleft(action)