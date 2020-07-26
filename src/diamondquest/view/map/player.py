import pygame

from diamondquest.common import Color
from diamondquest.common import Resolution
from diamondquest.common import Direction

from diamondquest.model.player import PlayerModel, SpriteAction, SpriteMode


class PrimarySpriteMap():

    sprite_locations = {
        (SpriteAction.IDLE, SpriteMode.STATIC, Direction.HERE): (0, 0),
        # TODO other sprites
    }


class PlayerView(pygame.sprite.Sprite):

    primary = None

    @classmethod
    def get_primary(cls):
        if not cls.primary:
            cls.primary = pygame.sprite.Group(cls())
        return cls.primary

    @classmethod
    def update_view(cls):
        location = PlayerModel.get_player()._location
        cls.primary.update(location)

    def __init__(self):
        super().__init__()
        # TODO start with actual sprite image
        self.image = pygame.Surface((50, 50))
        self.image.fill(Color.WHITE)
        self.rect = self.image.get_rect()

    def update(self, location):
        # TODO other arguments for animation, setting correct image etc
        # TODO scaling ???
        scale = Resolution.get_primary().block_height  # TODO only valid while display is square
        self.rect.x = location.col * scale
        self.rect.y = location.row * scale
