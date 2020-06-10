#!/usr/bin/env python3
import pygame
from pygame.locals import *
from diamondquest.hello import hello
from diamondquest.view.window import Window
from diamondquest.controller import keyboardcontroller
from diamondquest.common.constants import FPS

# Temporary imports here...
#from diamondquest.model.map.loot import LootTables
from diamondquest.view.mapview import BlockTexture
from diamondquest.model.map.blocks import BlockType, TreasureVariant
from diamondquest.common.loader import load_texture
from diamondquest.common.constants import TEXTURE_RES


def terrible_test_code_function():
    """If you want to test something out instead of starting the game,
    put it in here."""
    # print(LootTables.roll("artifact", 5, 1, "must"))
    block = BlockTexture.load_texture(BlockType.TREASURE, TreasureVariant.ARTIFACT)
    
    surf = pygame.display.get_surface()
    surf.blit(block, (0, 0))
    pygame.display.flip()


def main():
    pygame.init()
    clock = pygame.time.Clock()


    # model = GameModel()
    window = Window()

    window.draw_window()
    
    terrible_test_code_function()

    running = True
    while running:
            # This keeps the loop running at 16 times a second roughly, might be better way to handle it.
            clock.tick(FPS)

            # Controller Tick - Handle Input
            running = keyboardcontroller.inputHandling()
            # System Tick - Update Model
            # View Tick - Update View


if __name__ == "__main__":
    main()
    #terrible_test_code_function()
