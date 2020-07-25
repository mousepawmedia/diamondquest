"""
Menu Model [DiamondQuest]

Defines a menu.

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

from diamondquest.common import FontAttributes, FontAttributeDefaults


class TextItem:
    """A menu item that is only static text."""
    def __init__(self, text, attributes=FontAttributeDefaults.MENU):
        self.text = text
        self.attributes = attributes
        # icon


class ButtonType(Enum):
    STATIC = 0  # text never changes
    SCROLL = 1  # left/right arrows scroll through options
    INPUT = 2  # user can type into button text


class ButtonItem:
    """An interactive menu item."""

    def __init__(
        self,
        text,
        attributes=FontAttributeDefaults.MENU,
        button_type=ButtonType.STATIC
    ):
        self.text_item = TextItem(text, attributes)
        self.button_type = button_type


class MenuType(Enum):
    GAME = 0
    DEV = 1


class MenuModel:
    """The model for the menu."""

    menus = {}  # a dictionary storing menu instances
    menu_in_use = MenuType.GAME  # which menu the game is currently using

    @classmethod
    def get_menu(cls, menu_type=None):
        """Called by the View to get the contents of the menu."""
        # If no specific menu is requested, get the default.
        if menu_type is None:
            menu_type = cls.menu_in_use
        # Attempt to access a cached menu by its type.
        try:
            menu = cls.menus[cls.menu_in_use]
        # If there is no cached menu for that type...
        except KeyError:
            # Create and cache a new instance of the desired menu type.
            menu = cls.menus[menu_type] = cls._build(menu_type)
            if menu is None:
                raise KeyError(f"No such menu type {menu_type}")
        return menu

    @classmethod
    def use_menu(cls, menu_type):
        """Select which menu to use by default."""
        cls.menu_in_use = menu_type

    @classmethod
    def _build(cls, menu_type):
        """Builds and returns the specified menu."""
        if menu_type == MenuType.GAME:
            """Build the game menu here"""
            return MenuModel(
                "DiamondQuest",
                TextItem("Existing Miner"),
                ButtonItem("", button_type=ButtonType.SCROLL),
                TextItem("New Miner"),
                ButtonItem("Enter Name", button_type=ButtonType.INPUT),
                ButtonItem("Music: 10", button_type=ButtonType.SCROLL),
                ButtonItem("Sound: 10", button_type=ButtonType.SCROLL),
                ButtonItem("QUIT")
            )
        elif menu_type == MenuType.DEV:
            """Build the dev menu here"""
        else:
            return None

    def __init__(self, title, *items):
        self.items = [TextItem(title)]
        self.items.extend(items)

    def __iter__(self):
        iter(self.items)
