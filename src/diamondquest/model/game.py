from enum import Enum
import pygame
from diamondquest.common.mode import ModeType


class GameModel:
    """
    Top-level gamestate
    """

    mode = None
    pause = False

    @classmethod
    def on_start(cls):
        # map = MapModel.menu_map
        cls.mode = ModeType.MENU
