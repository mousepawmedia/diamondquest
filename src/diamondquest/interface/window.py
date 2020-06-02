import pygame
from diamondquest.interface import color


def draw_window(width, height, caption="DiamondQuest", color=color.black):
    screen = pygame.display.set_mode((width, height))

    pygame.display.set_caption(caption)
    screen.fill(color)

    pygame.display.flip()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
