"""
Game Menu [DiamondQuest]

The view for the Game Menu.

Author(s): Wilfrantz Dede, Jason C. McDonald, Stanislav Schmidt
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
# ARE DISCLAIME specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION)D. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE
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

import diamondquest
from diamondquest.common import Color, FontAlign, Resolution
from diamondquest.view.window import Window
from diamondquest.common.mode import ModeType
from diamondquest.model.menu import MenuModel
from diamondquest.model.menu import ButtonType


class MenuView:
    horizontal_margin = 5
    vertical_margin = 5

    @classmethod
    def update_view(cls):
        cls.view = Window.get_view(ModeType.MENU)
        Window.add_shadow_under(ModeType.MENU)  # TEMPORARY ONLY!
        cls.view.surface.fill(Color.WOOD)

        cls.menu = MenuModel.get_menu()
        cls._draw_text(
            row=0,
            text=cls.menu.title.text,
            text_attributes=cls.menu.title.text_attributes,
        )
        for row, item in enumerate(cls.menu.items, start=1):
            if isinstance(item, diamondquest.model.menu.ButtonItem):
                cls._draw_item_background(row)

            cls._draw_text(row, item.text, item.text_attributes)

            if row == cls.menu.selected_item_idx + 1:
                cls._draw_highlight(row)

    @classmethod
    def redraw(cls):
        """Render the view to the screen."""

    @classmethod
    def _draw_text(cls, row, text, text_attributes):
        style = text_attributes.style
        align = text_attributes.align
        color = text_attributes.color
        font = text_attributes._font
        antialias = True

        text_surface = font.render(text, antialias, color)

        item_width, item_height = Resolution.get_primary().menu_item_dim
        if align == FontAlign.LEFT:
            x = cls.horizontal_margin
        elif align == FontAlign.RIGHT:
            text_width, text_height = text_surface.get_size()
            x = item_width - 2 * cls.horizontal_margin - text_width
        elif align == FontAlign.CENTER:
            text_width, text_height = text_surface.get_size()
            x = (item_width - text_width) // 2
        else:
            raise ValueError(f"Unknown font align: {align}")
        y = row * item_height

        # Draw text

        cls.view.surface.blit(text_surface, dest=(x, y))

    @classmethod
    def _draw_item_background(cls, row, color=Color.WOOD_LIGHT):
        item_width, item_height = Resolution.get_primary().menu_item_dim

        left = cls.horizontal_margin
        top = row * item_height + cls.vertical_margin
        width = item_width - 2 * cls.horizontal_margin
        height = item_height - cls.vertical_margin

        bg_rect = pygame.Rect(left, top, width, height)
        pygame.draw.rect(cls.view.surface, color, bg_rect)

    @classmethod
    def _draw_highlight(cls, row):
        item_width, item_height = Resolution.get_primary().menu_item_dim

        top = row * item_height + cls.vertical_margin
        width = cls.horizontal_margin
        height = item_height - cls.vertical_margin

        # Draw background
        for left in [0, item_width - cls.horizontal_margin]:
            bg_rect = pygame.Rect(left, top, width, height)
            pygame.draw.rect(cls.view.surface, (255, 215, 0), bg_rect)
