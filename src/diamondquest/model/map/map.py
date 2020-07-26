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

from diamondquest.common import Coord, Direction, Depth
from diamondquest.model.map import Locality
from diamondquest.model.map import Block, BlockType


class MapColumn:
    """A single column in the map."""

    def __init__(self, col):
        """Generates a new map column"""
        self.blocks = []

        self.blocks.extend(Block.make_topsoil())

        for row in range(len(self.blocks), Block.MANTLE_START):
            coord = Coord(col, row)
            adjacent = (
                self.blocks[-1].type,
                MapModel.get_block_type(coord.get_adjacent(Direction.LEFT)),
                MapModel.get_block_type(coord.get_adjacent(Direction.RIGHT)),
            )

            self.blocks.append(
                Block.make_stone(
                    depth=Depth.of(row),
                    adjacent_air=adjacent.count(BlockType.AIR),
                    adjacent_dirt=adjacent.count(BlockType.DIRT),
                    adjacent_treasure=adjacent.count(BlockType.TREASURE),
                )
            )

        self.blocks.extend(Block.make_mantle())

    def get_section(self, depth):
        """Retrieves the blocks in part of the column"""
        return [self.blocks[row] for row in depth]

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
    def get_block_type(cls, coord):
        """Get block type at coordinate, but return None if not yet generated.
        Does not attempt to generate missing blocks or columns."""
        try:
            block = cls.columns[coord.col].get_block(coord.row)
            return block.type
        except KeyError:
            return None

    @classmethod
    def get_block_type(cls, coord=None):
        """Get block type at coordinate, but return None if not yet generated.
        Does not attempt to generate missing blocks or columns."""
        try:
            block = cls.columns[coord.col].get_block(coord.row)
            return block.type
        except KeyError:
            return None

    @classmethod
    def get_surface_coord(cls, col_num):
        """Returns the coordinate for the player standing on the surface
        for the given column.
        col - the column the player should be standing in."""
        col = cls.get_column(col_num, depth=Depth(1))

        for row, (block, coord) in enumerate(col):
            if block.type != BlockType.AIR:
                return Coord(col_num, row - 1)

            if block.type != BlockType.AIR:
                return Coord(col_num, row - 1)

    @classmethod
    def get_column(cls, col, depth):
        try:
            column = cls.columns[col]
        except KeyError:
            column = cls.columns[col] = MapColumn(col)

        return [
            (block, Coord(col, row))
            for block, row in zip(column.get_section(depth), depth)
        ]

    @classmethod
    def get_block(cls, coord):
        block = None
        try:
            block = cls.columns[coord.col].get_block(coord.row)
        except KeyError:
            block = cls.columns[coord.col] = MapColumn(coord.col)
        finally:
            return (block, coord)

    @classmethod
    def get_locality(cls, coord):
        return Locality(
            here=cls.get_block(coord),
            below_left=cls.get_block(coord.get_adjacent(Direction.BELOW_LEFT)),
            below=cls.get_block(coord.get_adjacent(Direction.BELOW)),
            below_right=cls.get_block(
                coord.get_adjacent(Direction.BELOW_RIGHT)
            ),
            left=cls.get_block(coord.get_adjacent(Direction.LEFT)),
            above_left=cls.get_block(coord.get_adjacent(Direction.ABOVE_LEFT)),
            above=cls.get_block(coord.get_adjacent(Direction.ABOVE)),
            above_right=cls.get_block(
                coord.get_adjacent(Direction.ABOVE_RIGHT)
            ),
            right=cls.get_block(coord.get_adjacent(Direction.RIGHT)),
        )
