"""
Resolution [DiamondQuest]

Window and surface size calculation functions.
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


class Resolution:
    DEFAULT_WIDTH = 810
    DEFAULT_HEIGHT = 610

    primary = None

    @classmethod
    def get_primary(cls):
        if cls.primary is None:
            cls.primary = Resolution(cls.DEFAULT_WIDTH, cls.DEFAULT_HEIGHT)
        return cls.primary

    @classmethod
    def set_primary(cls, resolution):
        cls.primary = resolution

    def __init__(self, width, height):
        self.width = width
        self.height = height

    @property
    def resolution(self):
        return self.width, self.height

    @property
    def block_height(self):
        """Return the height (and coincidentally, width) of a block at the
        current screen resolution. Guaranteed to be a multiple of 16.
        """
        map_height = self.map_area[1]
        return math.floor(map_height / constants.BLOCK_COUNT)

    @property
    def menu_item_dim(self):
        """Dimensions of the menu items.

        The width of the menu items is set to be equal to
        the width of the menu area. The height is set to
        be 2/3 of the block height.

        Returns
        -------
        menu_item_width : int
            The width of a menu item.
        menu_item_height : int
            The height of a menu item.
        """
        menu_width, *_ = self.menu_area
        menu_item_width = menu_width
        menu_item_height = self.block_height * 2 // 3

        return menu_item_width, menu_item_height

    @property
    def map_area(self):
        """Calculate the area for the map surface based on the resolution.
        Each dimension is guaranteed to be a multiple of 16.
        """
        width = constants.TEXTURE_RES * math.floor(
            self.width / constants.TEXTURE_RES
        )
        height = constants.TEXTURE_RES * math.floor(
            self.height / constants.TEXTURE_RES
        )
        x = (self.width - width) / 2
        y = (self.height - height) / 2
        return (width, height, x, y)

    @property
    def puzzle_area(self):
        """Calculate the area for the puzzle surface based on the
        resolution. Guaranteed to have exactly 1/2 block padding around the
        edges."""
        width, height, x, y = self.map_area
        less = self.block_height
        width -= less
        height -= less
        x += less / 2
        y += less / 2

        return (width, height, x, y)

    @property
    def journal_area(self):
        """Calculate the area for the journal/menu surface based on the
        resolution. Guaranteed to have exactly 1/2 block padding on top
        and bottom, and a width of 5 block."""
        map_width, height, x, y = self.map_area
        block = self.block_height
        width = block * 5
        height -= block
        x = (map_width - width) / 2
        y += block / 2

        return width, height, x, y

    @property
    def menu_area(self):
        return self.journal_area

    @property
    def blocks_across(self):
        """Returns the number of blocks that can fit across the map area."""
        return math.floor(self.width / self.block_height)
