"""
Blocks [DiamondQuest]

Individual blocks for the map.

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

from enum import Enum
import random

from diamondquest.common.direction import Direction


class BlockType(Enum):
    """Represents the type of block.
    Breakable blocks can be mined, and can be hooked to, but can be stood on.
    Breakable blocks have positive IDs.

    Unbreakable blocks cannot be mined, and cannot be hooked to.
    How the player interacts with the unbreakable blocks depends on the block.
    Unbreakable blocks have negative IDs.

    Air blocks (0) may be sky, or contain remnants of a removed block.
    """

    MANTLE = -2  # mantlestone
    STRUCTURE = -1  # stalactite/stalagmite, will be added later
    AIR = 0
    GRASS = 1
    DIRT = 2
    STONE = 3  # plain stone
    TREASURE = 4  # treasure blocks


class TreasureVariant(Enum):
    """Represents the different types of treasure block."""

    ARTIFACT = 1
    FOSSIL = 2
    MINERAL = 3


class StructureVariant(Enum):
    """Represents a solid non-block cave structure."""

    STALACTITE = 1
    STALAGMITE = 2
    PILLAR = 3


class MantleVariant(Enum):
    """Represents the different types of mantle block."""

    UPPER = 1
    MID = 2
    LOWER = 3


class Decoration(Enum):
    """Decorations can be rendered in front of a block, but do not collide."""

    NONE = 0
    DAISY = 1
    DANDELION = 2
    SPROUT = 3


class Block:
    """Represents a single block."""

    def __init__(self, type=BlockType.STONE, variant=0):
        self.type = type
        self.variant = variant
        self.decor = Decoration.NONE
        self.decor_offset = 0

    @staticmethod
    def make_stone(depth):
        """Create a random stone or treasure block.
        depth - an integer between 1 and 8; higher depth, more probability
        """
        # TODO: Improve this!
        if random.randint(depth, 10) == 10:
            variant = random.choice(
                [
                    TreasureVariant.ARTIFACT,
                    TreasureVariant.FOSSIL,
                    TreasureVariant.MINERAL,
                ]
            )
            return Block(type=BlockType.TREASURE, variant=variant)
        else:
            return Block(type=BlockType.STONE)

    def add_decor(self, decor, offset=Direction.HERE):
        """Add a decor block to this block.
        decor - the Decoration to add
        offset - which block this should overlap
        """
        self.decor = decor
        self.decor_offset = offset

    def is_solid(self):
        return self.type != BlockType.AIR

    def can_anchor(self):
        """Returns whether a hook can be attached to the block."""
        return self.type > 0

    def can_break(self):
        """Returns whether the block can be mined/broken."""
        return self.type > 0

    def can_stand(self):
        """Returns whether the block can be stood on."""
        return self.type != BlockType.AIR

    def get_removed(self):
        """Return a new block to replace this one when it is removed.
        (Removing isn't the same as mining.)
        """
        # We cannot remove mantlestone or air.
        # Everything else is removable somehow.
        if self.type == BlockType.MANTLE or self.type == BlockType.AIR:
            return self

        # Return an air block with the prior block type as its variant.
        return Block(type=BlockType.AIR, variant=self.type)
