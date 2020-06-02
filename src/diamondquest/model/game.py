from .map import MapModel

class GameModel:
    """
    Top-level gamestate
    """
    def __init__(self):
        self.map = MapModel()
