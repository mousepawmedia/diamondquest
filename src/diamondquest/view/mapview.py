"""
Map View [DiamondQuest]

Draws the map on the screen.

Author(s): Jason C. McDonald
"""

# LICENSE (BSD-3-Clause)
# Copyright (c) <YEAR> MousePaw Media.
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
from diamondquest.common.constants import TEXTURE_RES
from diamondquest.common import loader
from diamondquest.model.map import blocks, map
from diamondquest.view.window import Window, Views

# Temporary imports here...
#from diamondquest.model.map.loot import LootTables
from diamondquest.model.map.blocks import Block, BlockType, TreasureVariant
from diamondquest.common.loader import load_texture
from diamondquest.common.constants import TEXTURE_RES
from collections import deque

# TODO: Load images into data structure (i.e. Mineral.png, Stone.png)
# TODO: Load character sprites (data structure as well?)
# TODO: Account for window resizing (rescaling the map to adapt)
# TODO: Queue function (e.g. spot (x,y) has changed, put in the queue -> see redraw())


class BlockTexture():
    """Stores the top-left corner for each texture in blockset.gif.
    Numbers are (X,Y) pairs.
    Numbers are offsets *in blocks* from the top-left corner of the image.
    Block size is defined separately, and must be used with these values.
    """
    texture_locations = {
        (blocks.BlockType.STONE, 0): (0, 4),
        (blocks.BlockType.MANTLE, blocks.MantleVariant.UPPER): (0, 5),
        (blocks.BlockType.MANTLE, blocks.MantleVariant.MID): (0, 6),
        (blocks.BlockType.MANTLE, blocks.MantleVariant.LOWER): (0, 7),
        
        (blocks.BlockType.GRASS, 0): (6, 0),
        (blocks.BlockType.DIRT, 0): (6, 1),
        (blocks.BlockType.AIR, blocks.BlockType.GRASS): (5, 0),
        (blocks.BlockType.AIR, blocks.BlockType.DIRT): (6, 2),
        (blocks.BlockType.AIR, blocks.BlockType.STONE): (6, 3),
        (blocks.BlockType.AIR, blocks.BlockType.TREASURE): (6, 4),
        
        (blocks.BlockType.TREASURE, blocks.TreasureVariant.FOSSIL): (7, 2),
        (blocks.BlockType.TREASURE, blocks.TreasureVariant.ARTIFACT): (7, 3),
        (blocks.BlockType.TREASURE, blocks.TreasureVariant.MINERAL): (7, 4),
        
        (blocks.Decoration.SPROUT): (0, 0),
        (blocks.Decoration.DAISY): (1, 0),
        (blocks.Decoration.DANDELION): (2, 0)
    }
    
    cache = dict()
    
    @classmethod
    def texture_location(cls, block, variant=0):
        x, y = cls.texture_locations[(block, variant)]
        x *= TEXTURE_RES
        y *= TEXTURE_RES
        return (x, y, TEXTURE_RES, TEXTURE_RES)
        
    @classmethod
    def load_texture(cls, block, variant=0):
        """Load a surface containing the texture for a block, scaled to window.
        block - the BlockType or Decoration
        variant - the optional variant of the BlockType, default 0
        """
        try:
            return cls.cache[(block, variant)]
        except KeyError:
            blockset = loader.load_texture("blockset")
        
            texture = pygame.Surface((TEXTURE_RES, TEXTURE_RES))
            texture.blit(
                blockset,
                (0, 0),
                BlockTexture.texture_location(block, variant)
            )
            
            bh = Window.get_block_height()
            texture = pygame.transform.scale(texture, (bh, bh))
            
            cls.cache[(block, variant)] = texture
            return texture


class MapView:

    # Mostly works for updating blocks
    # Would want to reconsider for character movement
    # As you'll at least want starting block and ending block.
    def update():
        # Get MapModel update info
        locations, que = map.MapModel.create_mock_update_info()
        
        
        for (x, y) in locations: 
            # Passing que into this as so far MapView is just
            # functions, and unsure if que is something that needs
            # be saved between calls. 
            MapView.redraw(x, y, que)

    # If this same function is going to handle
    # sprite movement as well, might need to change
    # x,y to be part of the que of changes, and have an enum
    # for types of changes. As sprite movement needs to include
    # starting location not just ending location.
    def redraw(x, y, que):
        # Multiple keys pressed: queue system
        """Grabs next thing in the queue
        (x, y): specific block at x, y
        (x, -1): entire column at row x
        (-1, y): entire row at column y
        (-1, -1): whole map
        """
        if x == -1 and y == -1:
            # Change whole map
            pass
        elif x != -1 and y == -1:
            # Change entire column at row x
            pass
        elif x == -1 and y != -1:
            # Change entire row at column y
            pass
        else:
            # Change specific block at x, y
            MapView.draw_block(que.popleft(), x, y)
        """Player movement redraw handled as well (offset for smooth movement)
        Use percentage for offset (target pos +or- new pos * offset)
        """

    def draw_block(block, x, y):
        """Draw a single block on the screen.
        x - the x block position
        """
        block_size = Window.get_block_height()
        block = BlockTexture.load_texture(block.type, block.variant)
        surf = pygame.display.get_surface()
        surf.blit(block, (x*block_size, y*block_size))
        pygame.display.flip()

    # where the anchor is, current state, x location, y location
    def redraw_avatar(x, y):
        """Redraws the avatar as they move"""

    def redraw_map():
        """Walking off-screen:
        Miner walks off of the screen, whole screen shifts
        """


