"""
Window [DiamondQuest]

Handles the game window and caches primary surfaces.

Author(s): Harley Davis, Wilfrantz Dede, Jason C. McDonald
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

import pygame

from diamondquest.common import color
from diamondquest.common import constants

from diamondquest.view import View, ViewType


class Window:
    resolution = (810, 610)  # NOTE: Change this back when done testing

    # contains cached versions of the surfaces
    view_cache = dict()

    shadow_before = None
    shadow = None  # The cached shadowed surface

    @classmethod
    def set_resolution(cls, width, height):
        """Redraw the window with a new resolution.
        width - the new window width
        height - the new window height
        """
        cls.resolution = (width, height)
        # Clear the cached surfaces, which will need to be
        # recreated for the new window size.
        cls.clear_cache()

        cls.draw()

    @classmethod
    def clear_cache(cls):
        cls.view_cache = dict()

    @classmethod
    def draw(cls):
        """Draw the screen from scratch."""
        screen = pygame.display.set_mode(cls.resolution)

        # Write the caption to the screen.
        pygame.display.set_caption(constants.TITLE)

        # Fill the screen with the frame color.
        screen.fill(color.WOOD)

        # Render to the screen.
        cls.update()

    @classmethod
    def update(cls):
        """Redraw the entire window."""
        main_surface = pygame.display.get_surface()
        for view in cls.view_cache.values():
            if view.type == cls.shadow_before:
                main_surface.blit(cls.shadow, (0, 0))
            main_surface.blit(view.surface, view.registration)
        pygame.display.flip()

    @classmethod
    def get_map_area(cls):
        """Calculate the area for the map surface based on the resolution.
        Each dimension is guaranteed to be a multiple of 16.
        """
        width = 16 * math.floor(cls.resolution[0] / 16)
        height = 16 * math.floor(cls.resolution[1] / 16)
        x = (cls.resolution[0] - width) / 2
        y = (cls.resolution[1] - height) / 2
        return (width, height, x, y)

    @classmethod
    def get_puzzle_area(cls):
        """Calculate the area for the puzzle surface based on the
        resolution. Guaranteed to have exactly 1/2 block padding around the
        edges."""
        width, height, x, y = cls.get_map_area()
        less = cls.get_block_height()
        width -= less
        height -= less
        x += less / 2
        y += less / 2

        return (width, height, x, y)

    @classmethod
    def get_journal_area(cls):
        """Calculate the area for the journal/menu surface based on the
        resolution. Guaranteed to have exactly 1/2 block padding on top
        and bottom, and a width of 5 block."""
        map_width, height, x, y = cls.get_map_area()
        block = cls.get_block_height()
        width = block * 5
        height -= block
        x = (map_width - width) / 2
        y += block / 2

        return (width, height, x, y)

    @classmethod
    def get_block_height(cls):
        """Return the height (and coincidentally, width) of a block at the
        current screen resolution. Guaranteed to be a multiple of 16.
        """
        map_height = cls.get_map_area()[1]
        return math.floor(map_height / constants.BLOCK_COUNT)

    @classmethod
    def _draw_shadow(cls):
        """Return a shadowed version of whole window."""
        if cls.shadow is None:
            width, height, x, y = cls.get_map_area()
            tint = pygame.Surface((width, height))
            tint.fill(color.BLACK)
            tint.set_alpha(200)
            cls.shadow = pygame.display.get_surface().copy()
            cls.shadow.blit(tint, (x, y))

    @classmethod
    def add_shadow_before(cls, view):
        """Add the shadow before (under) one of the views"""
        cls._draw_shadow()
        cls.shadow_before = view

    @classmethod
    def remove_shadow(cls):
        """Removes the shadow."""
        cls.shadow = None
        cls.shadow_before = None

    @classmethod
    def get_view(cls, view):
        """Return the current surface for drawing on.
        view - the view to return the surface for
        """
        try:
            return cls.view_cache[view]
        except KeyError:
            cls.view_cache[view] = cls._create_view(view)
            return cls.view_cache[view]

    @classmethod
    def _create_view(cls, view):
        """Creates and returns an appropriately sized surface for a view.
        view - the purpose of the surface
        """
        if view == ViewType.MAP:
            width, height, x, y = cls.get_map_area()
        elif view == ViewType.PUZZLE:
            width, height, x, y = cls.get_puzzle_area()
        elif view == ViewType.JOURNAL:
            width, height, x, y = cls.get_journal_area()
        return View(view, pygame.Surface((width, height)), (x, y))
