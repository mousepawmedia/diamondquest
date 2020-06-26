"""
Direction [DiamondQuest]

Values representing relative direction.

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

from enum import IntEnum


class Direction(IntEnum):
    """The current position is always 0. The floor is 2.
    Positions are numbered clockwise.
    Horizontal is divisible by 4, vertical is not; both are even.
    Diagonal is odd.

    5 6 7
    4 0 8
    3 2 1
    """

    HERE = 0
    BELOW_RIGHT = 1
    BELOW = 2
    BELOW_LEFT = 3
    LEFT = 4
    ABOVE_LEFT = 5
    ABOVE = 6
    ABOVE_RIGHT = 7
    RIGHT = 8

    @staticmethod
    def adjacent_cw(direction):
        adj = direction + 1
        if adj > 8:
            adj = 1

    @staticmethod
    def adjacent_ccw(direction):
        adj = direction - 1
        if adj < 1:
            adj = 8

    @staticmethod
    def is_horizontal(direction):
        """Returns whether the direction is horizontal."""
        # Directions 4 and 8 are horizontal
        return direction > 0 and not direction % 4

    @staticmethod
    def is_diagonal(direction):
        """Returns whether the direction is diagonal."""
        # Odd directions are diagonal.
        return direction > 0 and direction % 2

    @staticmethod
    def is_vertical(direction):
        """Returns whether the direction is vertical."""
        # Directions 2 and 6 are vertical
        return direction % 2 == 0 and direction % 4

    @staticmethod
    def is_left(direction):
        """Returns whether the direction is generally left."""
        # Directions 3, 4, and 5 are left.
        return direction > 2 and direction < 6

    @staticmethod
    def is_right(direction):
        """Returns whether the direction is generally right."""
        # Directions 1, 7, 8
        return direction == 1 or direction > 6

    @staticmethod
    def is_above(direction):
        """Returns whether the direction is generally above."""
        # Directions 5, 6, and 7 are above.
        return direction > 4 and direction < 8

    @staticmethod
    def is_below(direction):
        """Returns whether the direction is generally below."""
        # Directions 1, 2, and 3 are above.
        return direction > 0 and direction < 4
