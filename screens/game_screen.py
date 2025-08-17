from typing import Optional
import pygame
from pygame import MOUSEBUTTONDOWN, Rect, display, mouse
from pygame.draw import circle, rect
from colors import BACKGROUND_COLOR, PLAYER_COLOR_MAP
from connect4 import Connect4
from constant import GRID_COLUMNS, GRID_ROWS, CIRCLE_RADIUS, TIE_CODE
from choices import ScreensEnum
from screens.victory_screen import set_winner

class GameScreen:
    def __init__(self, width, height, screen) -> None:
        self.connect4 = Connect4()
        self.size = self.width, self.height = width, height
        self.screen = screen

        self.background_rect = Rect(0, 0, self.width, self.height)

        self.radius = CIRCLE_RADIUS
        self.grid_centers = [[(0.0, 0.0) for _ in range(GRID_COLUMNS)] for _ in range(GRID_ROWS)]
        self.columns = [(0.0, 0.0) for _ in range(GRID_COLUMNS)]
        self.calculate_grid()

    def calculate_grid(self) -> None:
        total_circle_width_space = (2 * self.radius * GRID_COLUMNS)
        without_circle_width = self.width - total_circle_width_space
        padding_x = without_circle_width / (GRID_COLUMNS + 1)

        total_circle_height_space = (2 * self.radius * GRID_ROWS)
        without_circle_height = self.height - total_circle_height_space
        padding_y = without_circle_height / (GRID_ROWS + 1)

        cur_y = padding_y + self.radius
        for i in range(GRID_ROWS):
            cur_x = padding_x + self.radius
            for j in range(GRID_COLUMNS):
                self.grid_centers[i][j] = (cur_x, cur_y)
                cur_x += self.radius + padding_x + self.radius
            cur_y += self.radius + padding_y + self.radius

        cur_x = padding_x
        for i in range(GRID_COLUMNS):
            self.columns[i] = (cur_x, cur_x + 2*self.radius) 
            cur_x += self.radius +  self.radius + padding_x

    def controls(self) -> Optional[int]:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                exit()
            if event.type == MOUSEBUTTONDOWN:
                return self.mouse_button_down()

    def mouse_button_down(self) -> Optional[int]:
        mouse_x, _ = mouse.get_pos()
        pos = -1
        for i in range(GRID_COLUMNS):
            if (
                self.columns[i][0] <= mouse_x and
                mouse_x <= self.columns[i][1]
            ):
                pos = i
                break
        if pos != -1:
            _, _, _, winner = self.connect4.move(pos)
            if winner in (1, -1, TIE_CODE):
                self.draw()
                set_winner(winner)
                return ScreensEnum.Victory
        return None

    def draw_grid(self) -> None:
        for i in range(GRID_ROWS):
            for j in range(GRID_COLUMNS):
                circle(
                    self.screen, 
                    PLAYER_COLOR_MAP[self.connect4.grid[i][j]], 
                    self.grid_centers[i][j], 
                    self.radius
                )
    
    def draw(self) -> None:
        rect(self.screen, BACKGROUND_COLOR, self.background_rect)
        self.draw_grid()
        display.flip()
   
