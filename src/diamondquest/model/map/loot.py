"""
Loot Tables Model [DiamondQuest]

Generate loot for the different types of treasure block.

Author(s): Jacob Frazier, Jason C. McDonald
"""

# LICENSE (BSD-3-Clause)
# Copyright (c) <YEAR> MousePaw Media.
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

import random

from diamondquest.common import loader


class LootTables:

    tables = {
        "artifact": loader.read_loot_table("artifact"),
        "fossil": loader.read_loot_table("fossil"),
        "mineral": loader.read_loot_table("mineral"),
    }

    @classmethod
    def roll(cls, loot_table, amount, age):
        """
        Rolls a number of loot based on the table provided.
        """

        # Retrieve the desired loot table.
        try:
            table = cls.tables[loot_table]
        except KeyError:
            raise ValueError(f"No loot table {loot_table} exists.")

        # List of collections with repeated elements for rolling
        collections = []
        # List of items with repeated elements for rolling
        items = []

        # Iterate over all collections that match the age passed
        for k, v in table.items().filter(lambda _, b: b.age == age):
            # Add the name of the collection equal to the frequency to the list
            for i in range(v["frequency"]):
                collections.append(k)

        # Iterate over a randomly selected collection
        for name, val in table[LootTables._getItem(collections, 1)].items():
            # Add the name of the item to the list equal to the frequency
            for i in range(val["frequency"]):
                items.append(name)

        return LootTables._getItem(items, amount)

    @staticmethod
    def _getItem(list, amount):
        """
        Shuffles a collection and returns the first amount elements.
        """

        random.shuffle(list)
        return list[0:amount]
