from .map import MapModel
from collections import deque


class GameModel:
    """
    Top-level gamestate
    """

    def __init__(self):
        self.map = MapModel()
        self.actionQue = deque()
