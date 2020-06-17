#!/usr/bin/env python3
import pygame
from pygame.locals import *

from diamondquest.view.window import Window
from diamondquest.controller import keyboardcontroller, menucontroller
from diamondquest.controller import mapcontroller, journalcontroller
from diamondquest.common.constants import FPS
from diamondquest.view.map import MapView
from diamondquest.view.puzzleview import PuzzleView
from diamondquest.view.journal import JournalView
from diamondquest.view.gamemenu import MenuView
from diamondquest.model.game import GameModel
from diamondquest.common.mode import ModeType
# Temporary imports here...
# from diamondquest.model.map.loot import LootTables


def terrible_test_code_function():
    """If you want to test something out instead of starting the game,
    put it in here."""
    # print(LootTables.roll("artifact", 5, 1, "must"))
    # puzzle on terminal
    # puzzleview = PuzzleView()
    # puzzlestring, answer = puzzleview.puzzle_string(1 , 4,1)
    # score = 0
    # print(puzzlestring)
    # score = puzzleview.scorer(answer, score)
    # print(score)


def main():
    pygame.init()
    clock = pygame.time.Clock()

    # model = GameModel()
    window = Window()
    window.draw()
    
    GameModel.on_start()
    MapView.update()
    window.show_view(ModeType.MAP)
    window.show_view(ModeType.MENU)


    running = True
    while running:
        # Keep the loop running at roughly 16 FPS.
        # TODO: Is there a better way to handle this?
        clock.tick(FPS)

        # Controller Tick - Handle Input
        running = keyboardcontroller.inputHandling()
        
        if ( running ):
            # System Tick - Update Model
            update_controllers()
            # View Tick - Update View
            update_views()

def update_controllers():
    menucontroller.processAction()
    mapcontroller.processAction()
    journalcontroller.processAction()

#Called the right update_view depending on state.
def update_views():
    MapView.update()
    MenuView.update()
    JournalView.update()

if __name__ == "__main__":
    main()
    # terrible_test_code_function()
