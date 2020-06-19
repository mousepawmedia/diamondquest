"""
Coordinate [DiamondQuest]

Object representing a single coordinate pair.

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

import math

from diamondquest.common import Resolution
from diamondquest.common.direction import Direction


class Coord:
    def __init__(self, col, row):
        self.col = col
        self.row = row

    def relative(self, depth, section, scale=1):
        return (
            self.relative_col(section, scale),
            self.relative_row(depth, scale),
        )

    def relative_row(self, depth, scale=1):
        return (self.row - depth.top_x) * scale

    def relative_col(self, section, scale=1):
        return (self.col - section.start_row) * scale

    def get_adjacent(self, direction):
        if direction == Direction.HERE:
            return Coord(self.col, self.row)
        elif direction == Direction.BELOW:
            return Coord(self.col, self.row + 1)
        elif direction == Direction.BELOW_LEFT:
            return Coord(self.col - 1, self.row + 1)
        elif direction == Direction.LEFT:
            return Coord(self.col - 1, self.row)
        elif direction == Direction.ABOVE_LEFT:
            return Coord(self.col - 1, self.row - 1)
        elif direction == Direction.ABOVE:
            return Coord(self.col, self.row - 1)
        elif direction == Direction.ABOVE_RIGHT:
            return Coord(self.col + 1, self.row - 1)
        elif direction == Direction.RIGHT:
            return Coord(self.col + 1, self.row)
        elif direction == Direction.BELOW_RIGHT:
            return Coord(self.col + 1, self.row + 1)


class Depth:

    HEIGHT = 8

    def __init__(self, depth):
        self.depth = depth
        self.top_x = (depth - 1) * self.HEIGHT
        self.bottom_x = ((depth) * self.HEIGHT) - 1

    @property
    def row_range(self):
        """Return the upper and lower row coordinates for the depth."""
        return (self.top_x, self.bottom_x)

    def __iter__(self):
        return iter(range(self.top_x, self.bottom_x + 1))

    @classmethod
    def of(cls, row):
        return Depth(math.ceil(row / cls.HEIGHT))


class Section:
    def __init__(self, section, resolution=None):
        if resolution is None:
            resolution = Resolution.get_primary()

        self.res = resolution
        self.start_row = (section - 1) * self.res.blocks_across

    @property
    def end_row(self):
        return self.start_row + self.res.blocks_across

    @property
    def col_range(self):
        """Return the left and right column coordinates for the section."""
        return (self.start_row, self.end_row)

    def __iter__(self):
        return iter(range(self.start_row, self.end_row + 1))

    @classmethod
    def of(cls, col, resolution=None):
        if resolution is None:
            resolution = Resolution.get_primary()
        return Section(math.ceil(col / resolution.blocks_across), resolution)
