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

import pygame

from diamondquest.common import Color
from diamondquest.common import constants
from diamondquest.common import Resolution

from diamondquest.view import View
from diamondquest.common.mode import ModeType


class Window:

    # contains cached versions of the surfaces
    view_cache = dict()

    shadow_before = None
    shadow = None  # The cached shadowed surface

    @classmethod
    def resize(cls, resolution):
        """Redraw the window with a new resolution.
        width - the new window width
        height - the new window height
        """
        Resolution.set_primary(resolution)
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
        screen = pygame.display.set_mode(Resolution.get_primary().resolution)

        # Write the caption to the screen.
        pygame.display.set_caption(constants.TITLE)

        # Fill the screen with the frame color.
        screen.fill(Color.WOOD)

        # Render to the screen.
        cls.update_view()

    @classmethod
    def update_view(cls):
        """Redraw the entire window."""
        # TODO: This is getting convoluted; refactor

        main_surface = pygame.display.get_surface()
        for mode in ModeType.render_order():
            try:
                view = cls.view_cache[mode]
                if view.visible:
                    if view.type == cls.shadow_before:
                        main_surface.blit(cls.shadow, (0, 0))

                    main_surface.blit(view.surface, view.registration)
            except KeyError:
                continue

        pygame.display.flip()

    @classmethod
    def _draw_shadow(cls):
        """Return a shadowed version of whole window."""
        if cls.shadow is None:
            width, height, x, y = Resolution.get_primary().map_area
            tint = pygame.Surface((width, height))
            tint.fill(Color.BLACK)
            tint.set_alpha(200)
            cls.shadow = pygame.display.get_surface().copy()
            cls.shadow.blit(tint, (x, y))

    @classmethod
    def add_shadow_under(cls, view):
        """Add the shadow under one of the views"""
        cls._draw_shadow()
        cls.shadow_before = view

    @classmethod
    def remove_shadow(cls):
        """Removes the shadow."""
        cls.shadow = None
        cls.shadow_before = None

    @classmethod
    def show_view(cls, view):
        if not view in cls.view_cache:
            cls.view_cache[view] = cls._create_view(view)

        cls.view_cache[view].visible = True

    @classmethod
    def hide_view(cls, view):
        if not view in cls.view_cache:
            cls.view_cache[view] = cls._create_view(view)

        cls.view_cache[view].visible = False

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
        if view == ModeType.MAP:
            width, height, x, y = Resolution.get_primary().map_area
        elif view == ModeType.PUZZLE:
            width, height, x, y = Resolution.get_primary().puzzle_area
        elif view == ModeType.JOURNAL:
            width, height, x, y = Resolution.get_primary().journal_area
        elif view == ModeType.MENU:
            width, height, x, y = Resolution.get_primary().journal_area
        return View(view, pygame.Surface((width, height)), (x, y))
