#!/usr/bin/env python3
import pygame
from pygame.locals import *
from diamondquest.hello import hello
from diamondquest.view import GameView


def main():
    pygame.init()

    model = GameModel()
    view = GameView()
    running = True
    while running:
        # ControllerTick()
        # ViewTick()
        for event in ygame.event.get():
            if event.type == QUIT:
                running = False
                # Handle Events
        view.draw(model)


if __name__ == "__main__":
    main()
