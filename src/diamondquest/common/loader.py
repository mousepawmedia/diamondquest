"""
Data Loader [DiamondQuest]

Load data and resource files.

Author(s): Stephen J Gallagher, Jason C. McDonald
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

from pathlib import Path
import json

import pygame

resource_path = Path(__file__).resolve().parents[1] / "resources"


def read_json(path):
    load_path = resource_path / path
    data = dict()
    with load_path.open("r") as file:
        data = json.load(file)
    return data


def read_loot_table(table):
    return read_json(f"loot/{table}.json")


def load_font(font, size, subfolder="fonts", extension="ttf"):
    load_path = resource_path / subfolder / font / f"{font}.{extension}"
    return pygame.font.Font(str(load_path), size)


texture_cache = {}


def load_texture(texture, subfolder="textures"):
    """Load texture from resource directory or cache."""
    try:
        surface = texture_cache[texture]
    except KeyError:
        load_path = resource_path / subfolder / f"{texture}.gif"
        with load_path.open("rb") as img:
            surface = texture_cache[texture] = pygame.image.load(
                img
            ).convert_alpha()
    return surface


sprite_cache = {}


def load_player_sprites(sheet_name, subfolder="sprites"):
    try:
        sheet = sprite_cache[sheet_name]
    except KeyError:
        load_path = resource_path / subfolder / f"{sheet_name}.gif"
        with load_path.open("rb") as img:
            sheet = pygame.image.load(img).convert_alpha()
        sprite_cache[sheet_name] = sheet
    return sheet
