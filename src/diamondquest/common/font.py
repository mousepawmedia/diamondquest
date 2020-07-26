"""
Font Attributes [DiamondQuest]

Reusable and shared font attributes.
,
Author(s): Wilfrantz Dede, Jason C. McDonald
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

from diamondquest.common import Color
from diamondquest.common import loader
from diamondquest.common import Resolution


class Fontfaces:
    DECORATIVE = "Kirsty"
    MATH = "cascadia_code"


class FontStyle(Enum):
    NORMAL = 0
    BOLD = 1
    ITALIC = 2
    UNDERLINE = 3


class FontAlign(Enum):
   CENTER = 0
   LEFT = 1
   RIGHT = 2


class FontAttributes:
    def __init__(self, fontface, size, style=FontStyle.NORMAL, align=FontAlign.CENTER, color=Color.BLACK):
        self.fontface = fontface
        self.size = size
        self.style = style
        self.align = align
        self.color = color

        self._font = loader.load_font(font=self.fontface, size=self.size)


class FontAttributeDefaults:
    menu_item_width, menu_item_height = Resolution.get_primary().menu_item_dim
    MENU = FontAttributes(
        fontface=Fontfaces.DECORATIVE,
        size=menu_item_height,
    )
