"""
main_app.py

Sorting Algorithms App

This module contains the main application for
display sorting algorithms using Pygame.

It includes a class `Button` for creating interactive buttons,
and a `SortingAlgorithmsApp` class for running the application.
"""
from random import randint
import sys

import pygame

from .displayers import ALGORITHMS_DISPLAYERS
from .constants import BUTTON_HEIGHT, BUTTON_WIDTH, BUTTON_X, WHITE, BLACK, RED, GREEN, WIDTH, HEIGHT, MIN, MAX, N


class Button:
    """
    Button class for creating interactive buttons on a Pygame screen.

    Args:
        screen (pygame.Surface): The screen to draw the button on.
        x (int): The x coordinate of the button.
        y (int): The y coordinate of the button.
        width (int): The width of the button.
        height (int): The height of the button.
        text (str): The text displayed on the button.
        color (tuple): The color of the button.

    Attributes:
        rect (pygame.Rect): The rectangle representing the button.
        text (str): The text displayed on the button.
        color (tuple): The color of the button.
        screen (pygame.Surface): The screen to draw the button on.

    Methods:
        draw(): Draw the button on the screen.
        is_clicked(pos): Check if the button is clicked given a mouse position.
    """
    def __init__(self, screen, x, y, width, height, text, color, key=""):
        """
        Initialize the button

        Args:
            screen (pygame.Surface): the screen to draw on
            x (int): x coordinate of the button
            y (int): y coordinate of the button
            width (int): width of the button
            height (int): height of the button
            text (str): text of the button
            color (tuple): color of the button
            key (str): key of the button
        """
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.color = color
        self.screen = screen
        self.key = key

    def draw(self):
        """
        Draw the button on the screen
        """
        pygame.draw.rect(self.screen, self.color, self.rect)
        font = pygame.font.SysFont("", 30)
        text_surface = font.render(self.text, True, BLACK)
        text_rect = text_surface.get_rect(center=self.rect.center)
        self.screen.blit(text_surface, text_rect)

    def is_clicked(self, pos):
        """
        Check if the button is clicked given a mouse position

        Args:
            pos (tuple): the position of the mouse

        Returns:
            bool: True if the button is clicked, False otherwise
        """
        return self.rect.collidepoint(pos)


class SortingAlgorithmsApp:
    """
    Main application for display sorting algorithms

    Attributes:
        running (bool): True if the app is running, False otherwise
        algorithm_selected (str): the selected algorithm
        order_selected (str): the selected order
        algorithm_displayer (BaseSortDisplayer): the displayer for the selected algorithm
        list (list): the list of numbers to sort

    Methods:
        draw_title(title): Draw the title on the screen
        quit(): Quit the app
        run(): Run the app
        select_algorithm(): Select the solving method
        select_order(): Select the order of the list
        start_algorithm(): Start the selected algorithm
    """
    def __init__(self):
        """
        Initialize the app
        """
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Sorting Algorithms")
        self.running = True
        self.algorithm_selected = ""
        self.order_selected = ""
        self.algorithm_displayer = None
        self.list = [randint(MIN, MAX) for _ in range(N)]

    def draw_title(self, title):
        """
        Draw the title on the screen

        Args:
            title (str): the title
        """
        font = pygame.font.SysFont("", 50)
        text = font.render(title, True, BLACK)
        text_rect = text.get_rect(center=(WIDTH // 2, 50))
        self.screen.blit(text, text_rect)

    def quit(self):
        """
        Quit the app
        """
        self.running = False
        pygame.quit()
        sys.exit()

    def run(self):
        """
        Run the app
        """
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.quit()
            self.select_algorithm()

    def select_algorithm(self):
        """
        Select the solving method
        """
        buttons = [
            Button(
                screen=self.screen, 
                x=BUTTON_X, y=150 + 50 * i + i * 10, 
                width=BUTTON_WIDTH, height=BUTTON_HEIGHT, 
                text=" ".join(method.split("_")).capitalize(),
                color=GREEN, key=method
            ) for i, method in enumerate(ALGORITHMS_DISPLAYERS.keys())
        ]
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.quit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    for button in buttons:
                        if button.is_clicked(event.pos):
                            self.algorithm_selected = button.key
                            self.select_order()

            self.screen.fill(WHITE)

            self.draw_title("Select Sorting Algorithm")

            for button in buttons:
                button.draw()

            pygame.display.update()

    def select_order(self):
        """
        Select the order of the list
        """
        buttons = [
            Button(
                screen=self.screen, 
                x=BUTTON_X, y=150, 
                width=BUTTON_WIDTH, height=BUTTON_HEIGHT, 
                text="Ascending",
                color=GREEN, key="asc"
            ),
            Button(
                screen=self.screen, 
                x=BUTTON_X, y=210, 
                width=BUTTON_WIDTH, height=BUTTON_HEIGHT, 
                text="Descending",
                color=GREEN, key="desc"
            )
        ]
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.quit()
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_BACKSPACE:
                    self.select_algorithm()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    for button in buttons:
                        if button.is_clicked(event.pos):
                            self.order_selected = button.key
                            print(self.order_selected)
                            self.start_algorithm()

            self.screen.fill(WHITE)

            self.draw_title("Select Sorting Order")

            for button in buttons:
                button.draw()

            pygame.display.update()

    def start_algorithm(self):
        """
        Start the selected algorithm
        """
        button = Button(
            screen=self.screen, x=BUTTON_X, y=300, width=BUTTON_WIDTH, height=BUTTON_HEIGHT, text="Start", color=GREEN
        )
        algorithm_displayer = ALGORITHMS_DISPLAYERS[self.algorithm_selected](
            self.screen, self.list[:], self.order_selected
        )
        start = False
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.quit()
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_BACKSPACE:
                    self.select_order()
                elif event.type == pygame.MOUSEBUTTONDOWN and button.is_clicked(event.pos) and not start:
                    print("Start")
                    start = True
                    algorithm_displayer.sort()
            if not start:
                self.screen.fill(WHITE)
                self.draw_title(algorithm_displayer.title)
                button.draw()
            pygame.display.update()


def main():
    app = SortingAlgorithmsApp()
    app.run()


if __name__ == "__main__":
    main()
