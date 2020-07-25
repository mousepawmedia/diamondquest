"""
Player Model [DiamondQuest]

Stores current data about the player avatar.

Author(s): Elizabeth Larson, Jason C. McDonald
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

from enum import Enum

import pygame

from diamondquest.common import constants
from diamondquest.common import Direction, Resolution
from diamondquest.model.map import MapModel
from diamondquest.model.player import ToolType
from diamondquest.common.color import Color

class PlayerAction(Enum):
    IDLE = 0
    MOVE = 1
    TOOL = 2

class PlayerSprite(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # TODO start with actual sprite imge
        self.image = pygame.Surface((50, 50))
        self.image.fill(Color.WHITE)
        self.rect = self.image.get_rect()

    def update(self, location):
        # TODO other arguments for animation, setting correct image etc
        # TODO scalling ???
        scale = Resolution.get_primary().block_height  # TODO only valid while display is square
        print('scale', scale)
        self.rect.x = location.col * scale
        self.rect.y = location.row *scale




class PlayerModel:

    player = None

    @classmethod
    def get_player(cls):
        if cls.player is None:
            cls.player = PlayerModel()
        return cls.player

    def __init__(self, start_column=0):
        self._location = MapModel.get_surface_coord(col_num=start_column)

        self._locality = MapModel.get_locality(self._location)
        self._anchor = Direction.BELOW
        self.action = PlayerAction.IDLE

        self.tool = ToolType.HAND
        self._power = 1
        self.coffee = False

        self.sprites = pygame.sprite.Group(PlayerSprite())

    def reorient(self):
        """Update action and locality and reset anchor
        after a move.
        """
        self._locality = MapModel.get_locality(self._location)
        if self._locality.can_stand():
            self._anchor = Direction.BELOW
            self.action = PlayerAction.IDLE
        elif self._locality.can_climb():
            self._anchor = Direction.HERE
            self.action = PlayerAction.IDLE

    @property
    def anchor(self):
        return self._anchor

    def reanchor(self, direction):
        """Set the anchor point if possible.
        direction - the direction to place the anchor
        Returns True if able to reanchor, else False
        """
        if self._locality.can_anchor(direction):
            self._anchor = Direction.relative_to(self.col, self.row, direction)
            self.reorient()
            return True
        return False

    def move(self, direction):
        """Move in a particular direction."""
        if self._locality.can_occupy(direction):
            self._location = self._location.get_adjacent(direction)
            self.reorient()
            self.sprites.update(self._location)
            return True
        return False

    @classmethod
    def get_sprite(cls):
        return cls.get_player().sprites

'''
    @property.getter
    def power(self):
        return self._power

    @property.setter
    def power(self, power):
        """Set the power level between 1 and 8 inclusively."""
        if power < 1:
            self._power = 1
        else:
            self._power = min(power, constants.MAX_POWER_LEVEL)



    @property
    def location(self):
        return self._location
'''