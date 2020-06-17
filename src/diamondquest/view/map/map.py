"""
Map View [DiamondQuest]

Draws the map on the screen.

Author(s): Harley Davis, Jason C. McDonald
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

from diamondquest.common.coord import Coord, Depth
from diamondquest.model.map import MapModel
from diamondquest.view.window import Window
from diamondquest.common.mode import ModeType
from diamondquest.view.map import BlockTexture


class MapView:

    # Mostly works for updating blocks
    # Would want to reconsider for character movement
    # As you'll at least want starting block and ending block.
    @classmethod
    def update(cls):
        # Load latest view
        cls.view = Window.get_view(ModeType.MAP)

        if cls.view.empty:
            cls.redraw_map()
        else:
            # Get MapModel update info
            updates = MapModel.get_updates()

            for coord in updates:
                # Passing que into this as so far MapView is just
                # functions, and unsure if que is something that needs
                # be saved between calls.
                MapView.redraw(coord)

        # TODO: Render sprite next using separate functions

        Window.update()

    # If this same function is going to handle
    # sprite movement as well, might need to change
    # x,y to be part of the que of changes, and have an enum
    # for types of changes. As sprite movement needs to include
    # starting location not just ending location.
    @classmethod
    def redraw(cls, coord, block):
        # Multiple keys pressed: queue system
        """Grabs next thing in the queue
        (x, y): specific block at x, y
        (x, -1): entire column at row x
        (-1, y): entire row at column y
        (-1, -1): whole map
        """
        if coord.col == -1 and coord.row == -1:
            # Redraw the entire map
            cls.redraw_map()
        elif coord.col != -1 and coord.row == -1:
            # Redraw an entire column
            cls.redraw_col(coord.row)
            pass
        elif coord.col == -1 and coord.row != -1:
            # Redraw an entire row
            cls.redraw_row(coord.col)
            pass
        else:
            # Change specific block
            MapView.draw_block(block, coord)

        # TODO" Player movement redraw (offset for smooth movement)
        # Use percentage for offset (target pos +or- new pos * offset)

    @classmethod
    def draw_block(cls, coord):
        """Draw a single block on the screen.
        x - the block column
        y - the block row
        """
        block, _ = MapModel.get_block(coord)

        block_size = Window.res.block_height
        block_surface = BlockTexture.load_texture(block.type, block.variant)
        cls.view.surface.blit(
            block_surface, (coord.col * block_size, coord.row * block_size)
        )  # TODO: Very broken!

    @classmethod
    def redraw_avatar(cls):
        """Redraws the avatar as they move"""

    @classmethod
    def redraw_map(cls):
        """Walking off-screen:
        Miner walks off of the screen, whole screen shifts
        """
        for col in range(Window.res.blocks_across):
            cls.redraw_col(col)

    @classmethod
    def redraw_col(cls, col):
        """Redraw all blocks in column
        col - the column to redraw
        """
        for block, coord in MapModel.get_column(col, Depth(1)):
            cls.draw_block(coord)

    @classmethod
    def redraw_row(cls, row):
        """Redraw all blocks in row
        row - the row to redraw
        """
        # TODO: Draw blocks in row
