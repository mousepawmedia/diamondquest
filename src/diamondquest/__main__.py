#!/usr/bin/env python3
import pygame
from pygame.locals import *
from diamondquest.hello import hello
from diamondquest.view.window import Window

# Temporary imports here...
from diamondquest.model.map.loot import LootTables


def terrible_test_code_function():
    """If you want to test something out instead of starting the game,
    put it in here."""
    # print(LootTables.roll("artifact", 5, 1, "must"))


def main():
    pygame.init()

    # model = GameModel()
    window = Window()
    running = True
    while running:
        # ControllerTick()
        # ViewTick()
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
                # Handle Events
        window.draw_window()
        # draw model


if __name__ == "__main__":
    main()
    # terrible_test_code_function()
