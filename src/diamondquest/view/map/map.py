"""
Map View [DiamondQuest]

Draws the map on the screen.

Author(s): Harley Davis, Jason C. McDonald
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

from diamondquest.common import color

from diamondquest.model.map import MapModel, BlockType
from diamondquest.view.window import Window, ViewType
from diamondquest.view.map import BlockTexture

# TODO: Load images into data structure (i.e. Mineral.png, Stone.png)
# TODO: Load character sprites (data structure as well?)
# TODO: Account for window resizing (rescaling the map to adapt)
# TODO: Queue function (e.g. spot (x,y) has changed, put in the queue -> see redraw())


class MapView:

    # Mostly works for updating blocks
    # Would want to reconsider for character movement
    # As you'll at least want starting block and ending block.
    @classmethod
    def update(cls):
        # Load latest view
        cls.view = Window.get_view(ViewType.MAP)

        if cls.view.empty:
            cls.redraw_map()
        else:
            # Get MapModel update info
            updates = MapModel.get_updates()

            for (x, y) in updates:
                # Passing que into this as so far MapView is just
                # functions, and unsure if que is something that needs
                # be saved between calls.
                MapView.redraw(x, y)

        # TODO: Render sprite next using separate functions

        Window.update()

    # If this same function is going to handle
    # sprite movement as well, might need to change
    # x,y to be part of the que of changes, and have an enum
    # for types of changes. As sprite movement needs to include
    # starting location not just ending location.
    @classmethod
    def redraw(cls, x, y, block):
        # Multiple keys pressed: queue system
        """Grabs next thing in the queue
        (x, y): specific block at x, y
        (x, -1): entire column at row x
        (-1, y): entire row at column y
        (-1, -1): whole map
        """
        if x == -1 and y == -1:
            # Redraw the entire map
            cls.redraw_map()
        elif x != -1 and y == -1:
            # Redraw an entire column
            cls.redraw_col(x)
            pass
        elif x == -1 and y != -1:
            # Redraw an entire row
            cls.redraw_row(x)
            pass
        else:
            # Change specific block at x, y
            MapView.draw_block(block, x, y)

        # TODO" Player movement redraw (offset for smooth movement)
        # Use percentage for offset (target pos +or- new pos * offset)

    @classmethod
    def draw_block(cls, x, y):
        """Draw a single block on the screen.
        x - the x block position
        """
        block = MapModel.get_block(x, y)

        # Don't draw air/air blocks
        if block.type == BlockType.AIR and block.variant == BlockType.AIR:
            return

        block_size = Window.get_block_height()
        block_surface = BlockTexture.load_texture(block.type, block.variant)
        cls.view.surface.blit(block_surface, (x * block_size, y * block_size))

    # where the anchor is, current state, x location, y location
    @classmethod
    def redraw_avatar(cls, x, y):
        """Redraws the avatar as they move"""

    @classmethod
    def redraw_map(cls):
        """Walking off-screen:
        Miner walks off of the screen, whole screen shifts
        """
        cls.view.surface.fill(color.SKY)

        # HACK
        for i in range(8):
            cls.redraw_col(i)

    @classmethod
    def redraw_col(cls, col):
        """Redraw all blocks in column
        col - the column to redraw
        """
        # TODO: Fill rectangle

        # TODO: Draw blocks in column
        # HACK
        for row in range(8):
            cls.draw_block(col, row)

    @classmethod
    def redraw_row(cls, row):
        """Redraw all blocks in row
        row - the row to redraw
        """
        # TODO: Fill rectangle
        # TODO: Draw blocks in row
