"""
Menu Model [DiamondQuest]

Defines a menu.

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

import abc
import collections
from enum import Enum

import pygame

from diamondquest.common import FontAttributes, FontAttributeDefaults
from diamondquest.model.game import GameModel


class MenuItem(abc.ABC):
    """An abstract base class for menu items.

    Attributes
    ----------
    key_down_listeners : dict
        A dictionary storing key listeners.
    """

    def __init__(self):
        self.key_down_listeners = collections.defaultdict(list)

    @property
    @abc.abstractmethod
    def text(self):
        """The text of the menu item."""

    @property
    @abc.abstractmethod
    def text_attributes(self):
        """The text attributes of the menu item."""

    def add_key_down_listener(self, key, listener):
        """Add a key down listener.

        Parameters
        ----------
        key : int
            The key press that should be handled.
        listener : function
            The handler for the given key press. It should
            take no parameters and not return anything.
        """
        if listener not in self.key_down_listeners[key]:
            self.key_down_listeners[key].append(listener)

    def remove_key_down_listener(self, key, listener):
        """Remove a given key listener.

        Parameters
        ----------
        key : int
            The key press that was handled by the listener.
        listener : function
            The listener to remove.

        Returns
        -------
        status : bool
            If the listener was found and removed then True is
            returned, otherwise False.
        """
        if listener in self.key_down_listeners[key]:
            self.key_down_listeners[key].remove(listener)
            return True
        else:
            return False

    def handle_key_press(self, key):
        """Handle key presses when this item is focused.

        Parameters
        ----------
        key : int
            The key that was pressed.
        """
        for listener in self.key_down_listeners[key]:
            listener()


class TextItem(MenuItem):
    """A menu item that is only static text."""

    def __init__(
            self,
            text,
            attributes=FontAttributeDefaults.MENU,
    ):
        super().__init__()
        self.raw_text = text
        self.attributes = attributes
        # icon

    @property
    def text(self):
        return self.raw_text

    @property
    def text_attributes(self):
        return self.attributes



class ButtonType(Enum):
    STATIC = 0  # text never changes
    SCROLL = 1  # left/right arrows scroll through options
    INPUT = 2  # user can type into button text


class ButtonItem(MenuItem):
    """An interactive menu item."""

    def __init__(
        self,
        text,
        attributes=FontAttributeDefaults.MENU,
        button_type=ButtonType.STATIC,
    ):
        super().__init__()
        self.text_item = TextItem(text, attributes)
        self.button_type = button_type

    @property
    def text(self):
        return self.text_item.text

    @property
    def text_attributes(self):
        return self.text_item.text_attributes


class MenuType(Enum):
    GAME = 0
    DEV = 1


class MenuModel:
    """The model for the menu."""

    menu_items = {}  # a dictionary storing button instances
    menus = {}  # a dictionary storing menu instances
    menu_in_use = MenuType.GAME  # which menu the game is currently using

    @classmethod
    def initialize(cls):
        cls.menu_items["text_existing_miner"] = TextItem(text="Existing Miner")
        cls.menu_items["scroll_existing_miner"] = ButtonItem(text="<none>", button_type=ButtonType.SCROLL)
        cls.menu_items["text_new_miner"] = TextItem(text="New Miner")
        cls.menu_items["input_new_miner"] = ButtonItem(text="Enter Name", button_type=ButtonType.INPUT)
        cls.menu_items["scroll_music_volume"] = ButtonItem(text="Music: 10", button_type=ButtonType.SCROLL)
        cls.menu_items["scroll_sound_volume"] = ButtonItem(text="Sound: 10", button_type=ButtonType.SCROLL)
        cls.menu_items["button_quit"] = ButtonItem(text="QUIT")

        cls.menu_items["button_quit"].add_key_down_listener(
            pygame.K_RETURN,
            lambda: GameModel.stop_game())

        cls.menus[MenuType.GAME] = MenuModel(
            title="DiamondQuest",
            items=[
                cls.menu_items["text_existing_miner"],
                cls.menu_items["scroll_existing_miner"],
                cls.menu_items["text_new_miner"],
                cls.menu_items["input_new_miner"],
                cls.menu_items["scroll_music_volume"],
                cls.menu_items["scroll_sound_volume"],
                cls.menu_items["button_quit"],
            ])
        cls.menus[MenuType.DEV] = MenuModel(title="DevMenu", items=[])

    @classmethod
    def get_menu(cls, menu_type=None):
        """Called by the View to get the contents of the menu."""
        # If no specific menu is requested, get the default.
        if menu_type is None:
            menu_type = cls.menu_in_use

        if menu_type not in cls.menus:
            raise ValueError(f"No such menu type {menu_type}")

        return cls.menus[menu_type]

    @classmethod
    def use_menu(cls, menu_type):
        """Select which menu to use by default."""
        cls.menu_in_use = menu_type

    def __init__(self, title, items):
        self.title = TextItem(title)
        self.items = items
        self.selectable_items = [
            i for i, item in enumerate(items)
            if isinstance(item, ButtonItem)
        ]
        self.which_selected = 0 if len(self.selectable_items) > 0 else -1

    @property
    def selected_item_idx(self):
        if self.which_selected == -1:
            return -1
        return self.selectable_items[self.which_selected]

    def __iter__(self):
        iter(self.items)

    @classmethod
    def select_next_item(cls):
        menu = cls.get_menu()
        n_items = len(menu.selectable_items)
        menu.which_selected = (menu.which_selected + 1) % n_items

    @classmethod
    def select_prev_item(cls):
        menu = cls.get_menu()
        n_items = len(menu.selectable_items)
        menu.which_selected = (menu.which_selected - 1 + n_items) % n_items

    @classmethod
    def get_selected_item(cls):
        menu = cls.get_menu()
        idx = menu.selected_item_idx
        if idx > 0:
            return menu.items[idx]
        else:
            return None
