"""
Player Model [DiamondQuest]

Stores current data about the player avatar.

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

from enum import Enum

from diamondquest.common import Direction
from diamondquest.model.map import MapModel
from diamondquest.model.player import ToolType
from diamondquest.common.coord import Coord

class PlayerAction(Enum):
    HOOK_RIGHT = -3
    HOOK_UP = -2
    HOOK_LEFT = -1
    STAND = 0
    WALK = 1
    CLIMB = 2
    TOOL = 3
    COFFEE = 0xC0FFEE

class PlayerModel:

    location = Coord(0, 0)
    anchor = Coord(0, 0)
    tool = None  # current tool
    action = None  # current action/state
    power = 0  # power level

    @classmethod
    def status(cls):
        """This would be called by the View, and should return
        all player data needed for rendering."""
        # Get the locality using x, y
        # TODO: What would we return?

    @classmethod
    def set_anchor(cls, direction):
        locality = MapModel.get_locality(cls.location)
        if locality.can_anchor(direction):
            cls.anchor = Direction.relative_to(cls.col, cls.row, direction)