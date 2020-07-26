"""
Game Menu [DiamondQuest]

The view for the Game Menu.

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
from diamondquest.common import Color, Resolution
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
        cls._draw_text_item(row=0, text_item=cls.menu.title)
        for row, item in enumerate(cls.menu.items, start=1):
            if isinstance(item, diamondquest.model.menu.TextItem):
                cls._draw_text_item(row, item)
            elif isinstance(item, diamondquest.model.menu.ButtonItem):
                cls._draw_button_item(row, item)

    @classmethod
    def redraw(cls):
        """Render the view to the screen."""

    @classmethod
    def _draw_text_item(cls, row, text_item):
        """Render a text item."""
        fontface = text_item.attributes.fontface
        size = text_item.attributes.size
        style = text_item.attributes.style
        align = text_item.attributes.align
        color = text_item.attributes.color

        font = text_item.attributes._font
        if row == cls.menu.selected_item + 1:
            fg_color = Color.WHITE
        else:
            fg_color = text_item.attributes.color

        cls._draw_menu_item(row, text_item.text, font, fg_color)

    @classmethod
    def _draw_button_item(cls, row, button_item):
        """Render a button item."""
        if row == cls.menu.selected_item + 1:
            fg_color = Color.WHITE
        else:
            fg_color = button_item.text_item.attributes.color

        text = button_item.text_item.text
        font = button_item.text_item.attributes._font
        cls._draw_menu_item(row, text, font, fg_color)

    @classmethod
    def _draw_menu_item(cls, row, text, font, fg_color, bg_color=Color.WOOD_LIGHT):
        item_width, item_height = Resolution.get_primary().menu_item_dim
        item_x = cls.horizontal_margin
        item_y = row * item_height

        # Draw background
        left = item_x
        top = item_y + cls.vertical_margin
        width = item_width - 2 * cls.horizontal_margin
        height = item_height - cls.vertical_margin
        bg_rect = pygame.Rect(left, top, width, height)
        pygame.draw.rect(cls.view.surface, bg_color, bg_rect)

        # Draw text
        text_surface = font.render(text, True, fg_color)
        cls.view.surface.blit(text_surface, dest=(item_x, item_y))
