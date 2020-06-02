import pygame
from pygame.locals import *
from .mapview import MapView

def draw_map(screen, map_model):
    pygame.draw.rect(screen, BLUE, map_model.playerX, map_model.playerY, 100, 100)

class PyGameView:    """
    Top-level view for the whole game
    """
    def __init__(self):
        self.screen = pygame.display.set_mode((640, 480))

    def draw(self, model):
        draw_map(self.screen, model.map)
        pass # ??
