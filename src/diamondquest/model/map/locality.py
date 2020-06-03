"""
Locality [DiamondQuest]

Data structure representing the blocks around a particular point.

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

from diamondquest.model.map.direction import Direction


class Locality:
    """Stores the blocks around a particular point, and abstracts most
    conclusions about surroundings."""

    def __init__(
        self,
        here,
        below,
        belowleft,
        left,
        aboveleft,
        above,
        aboveright,
        right,
        belowright,
    ):
        self.blocks = (
            here,
            belowright,
            below,
            belowleft,
            left,
            aboveleft,
            above,
            aboveright,
            right,
            belowright,
        )

    def is_blocked(self, direction):
        if Direction.is_diagonal(direction):
            if (
                self.blocks(Direction.adjacent_ccw(direction)).is_solid()
                and self.blocks(Direction.adjacent_cw(direction)).is_solid()
            ):
                return True

        return False

    def can_anchor(self, direction):
        """You can only anchor to anchorable blocks to left, right, or above."""
        # If direction is left, right, or above...
        if direction > 2 and direction % 2 == 0:
            # Return whether block is anchorable
            return self.blocks[direction].can_anchor()
        # In all other cases, block is not anchorable
        return False

    def can_break(self, direction, anchored_to):
        """Check if the block can be broken based on the locality and which
        block the player is anchored to."""
        # Cannot break anything while freeclimbing.
        if anchored_to == Direction.HERE:
            return False

        # Determine whether block is blocked from this position.
        if self.is_blocked(direction):
            return False

        # Determine whether target block is breakable.
        if not self.blocks[direction].can_break():
            return

        # If player standing, can break any block except where standing.
        if anchored_to == Direction.BELOW:
            return not Direction.BELOW

        # If player is anchored to a non-floor block, that limits movement.
        if anchored_to == Direction.LEFT:
            return not Direction.is_left(direction)
        elif anchored_to == Direction.RIGHT:
            return not Direction.is_right(direction)
        elif anchored_to == Direction.ABOVE:
            return not Direction.is_above(direction)

    def can_stand(self):
        """Returns whether the player can stand from this position."""
        return self.blocks[Direction.BELOW].can_stand()
