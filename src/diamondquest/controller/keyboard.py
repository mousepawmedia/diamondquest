"""
KeyboardController [DiamondQuest]

The KeyboardController handles keyboard input events

Author(s): Harley Davis, Mohaned Mashaly, Jason C. McDonald
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

from datetime import datetime, timedelta

import pygame
from diamondquest.common.keys import Key
from diamondquest.common.constants import KEY_REPEAT_RATE
from diamondquest.eventmanager.event import TickEvent

KNOWN_KEYS = [KEYS.K_UP, KEYS.K_DOWN, KEYS.K_LEFT, KEYS.K_RIGHT, KEYS.K_ESCAPE, KEYS.K_j]

class KeyboardController:
    """Enqueues action events on keydown, deques on key up."""

    action_que = deque()

    last_key = None
    active_key = None
    last_update = datetime.utcnow() - timedelta(milliseconds=KEY_REPEAT_RATE)

    @classmethod
    def handle_input(cls):
        # first general events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
        # now special processing for keys
        keyscan = pygame.key.get_pressed()
        keys = {k: keyscan[k] for k in KNOWN_KEYS}
        if sum(keys.values()) == 0:
            # no keys depressed, reset
            cls.active_key = None
            cls.last_key = None
            cls.last_update = None
        elif sum(keys.values()) != 1:
            # otherwise only process if one and only one key is pressed
            # python bools are 0/1 so can use sum
            return True
        for key, pressed in keys.items():
            if pressed:
                now = datetime.utcnow()
                if Key.in_arrows(key) and cls.last_update:
                    interval = now - cls.last_update
                    update = interval > timedelta(milliseconds=KEY_REPEAT_RATE)
                elif Key.in_arrows(key) or key != cls.last_key:
                    update = True
                else:
                    update = False
                if update:
                    cls.last_key = key
                    cls.active_key  = key
                    cls.last_update = now
        return True

    @classmethod
    def grab(cls):
        if cls.active_key:
            key = cls.active_key
            cls.active_key = None
            return key

    @classmethod
    def pending(cls):
        return cls.active_key is not None

    @classmethod
    def notify(cls, event):
        if isinstance(event, TickEvent):
            # Handle Input Events
            for event in pygame.event.get():
                pass
