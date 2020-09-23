#!/usr/bin/env python3
import logging
import wasabi2d as w2d
from math import hypot
from pathlib import Path


# import pygame
# from pygame.locals import *

# pygame.init()  # MUST BE HERE, called before any imports

# from diamondquest.view.window import Window  # noqa: E402
# from diamondquest.controller import (  # noqa: E402
#     KeyboardController,
#     MenuController,
#     PlayerController,
#     JournalController,
# )

# from diamondquest.common.constants import FPS  # noqa: E402
# from diamondquest.view.map import MapView, PlayerView  # noqa: E402
# from diamondquest.view.puzzle import PuzzleView  # noqa: E402
# from diamondquest.view.journal import JournalView  # noqa: E402
# from diamondquest.view.menu import MenuView  # noqa: E402
# from diamondquest.model.menu import MenuModel  # noqa: E402
# from diamondquest.model.game import GameModel  # noqa: E402
# from diamondquest.common.mode import ModeType  # noqa: E402
# from diamondquest.model.player import PlayerModel
# from diamondquest.common import Direction
# from diamondquest.common import options

# Temporary imports here...
# from diamondquest.model.map.loot import LootTables

logger = logging.getLogger(__name__)


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

    global circle

    resources = Path(__file__).resolve().parent / Path('resources')

    scene = w2d.Scene(rootdir=resources)

    scene.layers[0].set_effect('bloom', radius=2, intensity=0.10)
    circle = scene.layers[0].add_circle(
        radius=25,
        pos=(scene.width / 2, scene.height / 2),
        color='aquamarine',
        fill=False,
        stroke_width=3
    )

    scene.layers[1].set_effect('bloom', radius=15, intensity=0.25)
    header = scene.layers[1].add_label(
        pos=(scene.width / 2, scene.height / 3),
        text='DiamondQuest',
        font='kirsty',
        fontsize=50,
        color='white',
        align='center'
    )

    hello = scene.layers[2].add_label(
        pos=(scene.width / 2, (2 * (scene.height / 3))),
        text='Hello.....world.',
        fontsize=25,
        color='gold',
        align='center'
    )

    w2d.run()


@w2d.event
def on_mouse_down(pos):
    mouse_x, mouse_y = pos
    cx, cy = circle.pos

    hit = hypot(mouse_x - cx, mouse_y - cy) < circle.radius

    if hit:
        circle.radius = 35
        w2d.animate(circle, 'bounce_end', radius=25)

#     clock = pygame.time.Clock()

#     # model = GameModel()
#     window = Window()
#     window.draw(fullscreen=False)

#     GameModel.on_start()
#     MenuModel.initialize()
#     MapView.update_view()
#     window.show_view(ModeType.MAP)
#     window.show_view(ModeType.MENU)

#     player = PlayerModel.get_player()

#     print("1 to hide initial menu")
#     print("Esc to toggle menu")
#     print("J to toggle Journal")

#     logger.info("Entering event loop")
#     while GameModel.running:
#         if not options.noclip:
#             player.move(Direction.BELOW)
#             player.reorient()

#         # Keep the loop running at roughly 16 FPS.
#         # TODO: Is there a better way to handle this?
#         clock.tick(FPS)

#         # Controller Tick - Handle Input
#         GameModel.running = KeyboardController.handle_input()

#         if GameModel.running:
#             if not options.noclip:
#                 player.move(Direction.BELOW)
#                 player.reorient()
#             # System Tick - Update Model
#             update_controllers()
#             # View Tick - Update View
#             update_views()


# def update_controllers():
#     MenuController.process_action()
#     PlayerController.process_action()
#     JournalController.process_action()


# # Called the right update_view depending on state.
# def update_views():
#     MapView.update_view()
#     PlayerView.update_view()
#     MenuView.update_view()
#     JournalView.update_view()


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)

    main()
    # terrible_test_code_function()
