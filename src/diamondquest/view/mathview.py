import pygame
import pygame.font
from diamondquest.view.window import Window, Views


""" Deals with MathView
"""
# window.draw_shadow()
# TODO:


def draw_puzzle(problem):

    font = pygame.font.Font("PrefferedFont.ttf", 24)
    rendered_problem = font.render(problem, True, (0, 0, 255))
    problem_display_area = rendered_problem.get_rect()
    # problem_display_area.center = ()

    surface = Window.get_surface(Views.MATH)

    # Get Transparent Background
    Window.draw_shadow()
    # draw on surface

    surface.blit(rendered_problem, problem_display_area)
    Window.redraw()
