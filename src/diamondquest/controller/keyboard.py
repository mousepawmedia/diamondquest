"""
KeyboardController [DiamondQuest]

The KeyboardController handles keyboard input events

Author(s): Harley Davis, Jason C. McDonald
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

from collections import deque

import pygame.locals as KEYS
import pygame

from diamondquest.eventmanager.event import TickEvent


class KeyboardController:
    """Enqueues action events on keydown, deques on key up."""

    action_que = deque()

    @classmethod
    def handle_input(cls):
        # NOTE: I'm sure there is a cleaner way to handle the if statements. (-HD)
        for event in pygame.event.get():
            # Handle closure of window, may need a key
            # for accessability.
            if event.type == pygame.QUIT:
                return False
            if event.type == KEYS.KEYDOWN:
                cls.action_que.append(event.key)

            if event.type == KEYS.KEYUP:
                # Arrow keys
                if event.key == KEYS.K_UP:
                    cls.action_que.remove(event.key)
                if event.key == KEYS.K_DOWN:
                    cls.action_que.remove(event.key)
                if event.key == KEYS.K_LEFT:
                    cls.action_que.remove(event.key)
                if event.key == KEYS.K_RIGHT:
                    cls.action_que.remove(event.key)

            # Other items from above, tools, movement mode etc,
            # May not be needed if they aren't "repeatable"

            # print(actionQue)

        return True

    @classmethod
    def restore(cls, key):
        cls.action_que.appendleft(key)

    @classmethod
    def grab(cls):
        return cls.action_que.pop()

    @classmethod
    def pending(cls):
        return len(cls.action_que) > 0

    @classmethod
    def notify(cls, event):
        if isinstance(event, TickEvent):
            # Handle Input Events
            for event in pygame.event.get():
                pass
