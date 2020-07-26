#!/usr/bin/env python3
import pygame
from pygame.locals import *

pygame.init()  # MUST BE HERE, called before any imports

from diamondquest.view.window import Window  # noqa: E402
from diamondquest.controller import (  # noqa: E402
    KeyboardController,
    MenuController,
    PlayerController,
    JournalController,
)

from diamondquest.common.constants import FPS  # noqa: E402
from diamondquest.view.map import MapView, PlayerView  # noqa: E402
from diamondquest.view.puzzle import PuzzleView  # noqa: E402
from diamondquest.view.journal import JournalView  # noqa: E402
from diamondquest.view.menu import MenuView  # noqa: E402
from diamondquest.model.menu import MenuModel  # noqa: E402
from diamondquest.model.game import GameModel  # noqa: E402
from diamondquest.common.mode import ModeType  # noqa: E402

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
    clock = pygame.time.Clock()

    # model = GameModel()
    window = Window()
    window.draw(fullscreen=False)

    GameModel.on_start()
    MenuModel.initialize()
    MapView.update_view()
    window.show_view(ModeType.MAP)
    window.show_view(ModeType.MENU)

    print("1 to hide initial menu")
    print("Esc to toggle menu")
    print("J to toggle Journal")

    while GameModel.running:
        # Keep the loop running at roughly 16 FPS.
        # TODO: Is there a better way to handle this?
        clock.tick(FPS)

        # Controller Tick - Handle Input
        GameModel.running = KeyboardController.handle_input()

        if GameModel.running:
            # System Tick - Update Model
            update_controllers()
            # View Tick - Update View
            update_views()


def update_controllers():
    MenuController.process_action()
    PlayerController.process_action()
    JournalController.process_action()


# Called the right update_view depending on state.
def update_views():
    MapView.update_view()
    PlayerView.update_view()
    MenuView.update_view()
    JournalView.update_view()


if __name__ == "__main__":
    main()
    # terrible_test_code_function()
