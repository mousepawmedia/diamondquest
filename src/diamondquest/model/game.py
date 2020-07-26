from enum import Enum
import pygame
from diamondquest.common.mode import ModeType


class GameModel:
    """
    Top-level game state
    """

    mode = None
    running = False
    pause = False

    music_volume = 10
    sound_volume = 10

    @classmethod
    def on_start(cls):
        # map = MapModel.menu_map
        cls.mode = ModeType.MENU
        cls.running = True
        cls.pause = False

    @classmethod
    def stop_game(cls):
        print("Bye bye!")
        cls.running = False
