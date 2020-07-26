"""
Player View [DiamondQuest]

Draws Player Sprite to the screen

Author(s): Stephen J Gallagher, Jason C. McDonald
"""

# LICENSE (BSD-3-Clause)
# Copyright (c) 2020 MousePaw Media.
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
# 1. Redistributions of source code must retain the above copyright notice,
# this list of conditions and the following disclaimer.
#
# 2. Redistributions in binary form must reproduce the above copyright notice,
# this list of conditions and the following disclaimer in the documentation
# and/or other materials provided with the distribution.
#
# 3. Neither the name of the copyright holder nor the names of its contributors
# may be used to endorse or promote products derived from this software without
# specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF
# THE POSSIBILITY OF SUCH DAMAGE.
#
# CONTRIBUTING
# See https://www.mousepawmedia.com/developers for information
# on how to contribute to our projects.

import pygame

from diamondquest.common.constants import TEXTURE_RES_SPRITE
from diamondquest.common import Resolution
from diamondquest.common import Direction
from diamondquest.common.loader import load_player_sprites

from diamondquest.model.player import PlayerModel, SpriteAction, SpriteMode


class PrimarySpriteMap:

    sprite_locations = {
        (SpriteAction.IDLE, SpriteMode.STATIC, Direction.HERE): (0, 0),
        # (SpriteAction.IDLE, SpriteMode.STATIC, Direction.HERE): (1, 1), # TODO incorrect, but demonstrates problems with sprite
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
        self.sheet = load_player_sprites("player_sheet")

        self.image = self._load_sprite(
            PrimarySpriteMap.sprite_locations[
                (SpriteAction.IDLE, SpriteMode.STATIC, Direction.HERE)
            ]
        )

        self.rect = self.image.get_rect()

    def _load_sprite(self, index):
        row, col = index
        # TODO issue with sprite sheet? these should probably be the same as TEXTURE_RES?
        sprite_width = TEXTURE_RES_SPRITE
        sprite_height = TEXTURE_RES_SPRITE
        rect = pygame.Rect(
            col * sprite_width, row * sprite_height, sprite_width, sprite_height
        )
        image = pygame.Surface(rect.size, pygame.SRCALPHA)
        image.blit(self.sheet, (0, 0), rect)
        bh = Resolution.get_primary().block_height
        image = pygame.transform.scale(image, (bh, bh))
        return image

    def update(self, location):
        # TODO other arguments for animation, setting correct image etc
        # TODO scaling ???
        scale = (
            Resolution.get_primary().block_height
        )  # TODO only valid while display is square

        self.rect.x = (
            location.col % Resolution.get_primary().blocks_across
        ) * scale
        self.rect.y = (
            location.row % Resolution.get_primary().blocks_across
        ) * scale  # XXX should be height
