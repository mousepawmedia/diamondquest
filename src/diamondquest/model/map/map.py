"""
Map Model [DiamondQuest]

The model for the game map.

Author(s): Jason C. McDonald
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

import math

from diamondquest.common import constants
from diamondquest.common.coord import Coord
from diamondquest.model.map import (
    Block,
    BlockType,
    MantleVariant,
    TreasureVariant,
    Decoration
)


class MapColumn:
    """A single column in the map."""

    def __init__(self):
        self.blocks = []
        """Generates a new map column"""
        # Two levels of sky
        for _ in range(2):
            self.blocks.append(Block(type=BlockType.AIR, variant=BlockType.AIR))
        # One level of grass, optional decorations
        self.blocks.append(Block(type=BlockType.GRASS))
        # TODO: Add optional decoration
        # One level of dirt
        self.blocks.append(Block(type=BlockType.DIRT))
        # Stone and treasure until 3 shy of bottom
        for row in range(5, constants.BLOCK_MAX - 3):
            self.blocks.append(Block.make_stone(math.ceil(row / 8)))

        self.blocks.append(Block(type=BlockType.MANTLE, variant=MantleVariant.UPPER))
        self.blocks.append(Block(type=BlockType.MANTLE, variant=MantleVariant.MID))
        self.blocks.append(Block(type=BlockType.MANTLE, variant=MantleVariant.LOWER))


    def get_section(self, from_row, to_row):
        """Retrieves the blocks in part of the column"""

    def get_block(self, row):
        """Returns a single block"""
        return self.blocks[row]


class MapModel:
    """The model for the Map"""

    columns = {}
    updates = []

    @classmethod
    def get_updates(cls):
        try:
            # Provide the current updates list
            return cls.updates
        finally:
            # After returning, clear the updates list
            cls.updates = []


    @classmethod
    def get_column(cls, col, row_top, row_bottom):
        try:
            return cls.columns[col].get_section(row_top, row_bottom)
        except KeyError:
            cls.columns[col] = MapColumn()
            return cls.columns[col].get_section(row_top, row_bottom)

    @classmethod
    def get_block(cls, coord):
        try:
            return cls.columns[coord.col].get_block(coord.row)
        except KeyError:
            cls.columns[coord.col] = MapColumn()
            return cls.columns[coord.col].get_block(coord.row)

    @classmethod
    def get_locality(cls, coord):
        return Locality(
            here = cls.get_block(coord),
            
            below_left = cls.get_block(coord.get_adjacent(Direction.BELOW_LEFT)),
            below = cls.get_block(coord.get_adjacent(Direction.BELOW)),
            below_right = cls.get_block(coord.get_adjacent(Direction.BELOW_RIGHT)),
            
            left = cls.get_block(coord.get_adjacent(Direction.LEFT)),
            
            above_left = cls.get_block(coord.get_adjacent(Direction.ABOVE_LEFT)),
            above = cls.get_block(coord.get_adjacent(Direction.ABOVE)),
            above_right = cls.get_block(coord.get_adjacent(Direction.ABOVE_RIGHT)),

            right = cls.get_block(coord.get_adjacent(Direction.RIGHT))
        )

