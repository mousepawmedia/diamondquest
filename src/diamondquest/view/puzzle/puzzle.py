import pygame
import pygame.font
from diamondquest.view.window import Window, View
from functools import reduce
from random import randint

""" Deals with MathView
"""
# window.draw_shadow()
# TODO:


class PuzzleView:
    def draw_puzzle(self, problem):

        font = pygame.font.Font(
            "../assets/fonts/cascadia-code/Cascadia.ttf", 60
        )  # TODO
        rendered_problem = font.render(problem, True, (0, 0, 255))
        problem_display_area = rendered_problem.get_rect()
        problem_display_area.center = ()

        # surface = Window.get_surface(Views.MATH)

        # Get Transparent Background
        # Window.draw_shadow()
        # draw on surface

        # surface.blit(rendered_problem, problem_display_area)
        # Window.redraw_window()

    def depth_range(self, depth):
        # defines range of numbers based on depth
        # increases the range with increasing depth
        if 0 <= depth <= 7:
            return randint(1, 10)
        elif 8 <= depth <= 15:
            return randint(11, 100)
        elif 16 <= depth <= 23:
            return randint(101, 1000)
        elif 24 <= depth <= 31:
            return randint(1001, 5000)
        elif 32 <= depth <= 39:
            return randint(5001, 10000)
        elif 40 <= depth <= 47:
            return randint(10001, 50000)
        elif 48 <= depth <= 55:
            return randint(50001, 100000)
        elif 56 <= depth <= 63:
            return randint(100001, 200000)

    def depth_numberofterms(self, depth):
        # defines range of numbers based on depth
        # increases the range with increasing depth
        if 0 <= depth <= 7:
            return 2
        elif 8 <= depth <= 15:
            return 2
        elif 16 <= depth <= 23:
            return 3
        elif 24 <= depth <= 31:
            return 3
        elif 32 <= depth <= 39:
            return 4
        elif 40 <= depth <= 47:
            return 4
        elif 48 <= depth <= 55:
            return 5
        elif 56 <= depth <= 63:
            return 5

    def power_level_operators(self, powerlevel, numberofterms, depth):
        listofNumbers = list()
        for i in range(numberofterms):
            i = self.depth_range(depth)
            listofNumbers.append(i)
        if powerlevel == 1:
            answer = sum(listofNumbers)
            return listofNumbers, answer, "+"
        elif powerlevel == 2:
            answer = reduce((lambda x, y: x - y), listofNumbers)
            return listofNumbers, answer, "-"
        elif powerlevel == 3:
            answer = reduce((lambda x, y: x * y), listofNumbers)
            return listofNumbers, answer, "*"
        elif powerlevel == 4:
            answer = reduce((lambda x, y: x / y), listofNumbers)
            return listofNumbers, answer, "/"
        elif powerlevel == 5:
            pass
        elif powerlevel == 6:
            pass
        elif powerlevel == 7:
            pass
        elif powerlevel == 8:
            pass

    def tool_difficulty(self, tool, powerlevel, depth):
        # Pickaxe two terms one operator
        # drill multiple terms one operator
        # tnt multiple terms multiple operator
        # operators depend on power level
        if tool == "pickaxe":
            numberofterms = 2
            self.power_level_operators(powerlevel, numberofterms, depth)
        elif tool == "drill":
            numberofterms = self.depth_numberofterms(depth)
            self.power_level_operators(powerlevel, numberofterms, depth)
        elif tool == "tnt":
            pass

    def puzzle_string(self, powerlevel, numberofterms, depth):
        # Convert list of Numbers to String and add Operators
        # return it to pygame fonts to render on screen
        listofNumbers, answer, operator = self.power_level_operators(
            powerlevel, numberofterms, depth
        )
        listofString = [str(number) for number in listofNumbers]
        if operator == "+":
            puzzleString = "+".join(listofString)
        elif operator == "-":
            puzzleString = "-".join(listofString)
        elif operator == "*":
            puzzleString = "*".join(listofString)
        elif operator == "/":
            puzzleString = "/".join(listofString)

        # implement scorer
        return puzzleString, answer

    def player_input(self):
        playerInput = input("Enter Answer")
        print("Answer" + playerInput)
        return int(playerInput)

    def scorer(self, answer, score):
        check_answer = self.answer_check(self.player_input(), answer)
        if check_answer == True:
            score = score + 1
            # level or points increase
            pass
        elif check_answer == False:
            score = score
            # level stays same points stay same
            pass
        return score

    def answer_check(self, userresponse, correctanswer):
        # Returns a bool
        # Increase level for true
        # Display Incorrect for false
        if userresponse == correctanswer:
            return True
        else:
            return False

    def bubble_puzzles(self, spectrum):
        # Future Task: Deals with in game Maths Puzzles with bubbles.
        # This can also use puzzle generator with changing spectrum
        pass
