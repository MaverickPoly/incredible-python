import pygame
from settings import *


class Fruit:
    def __init__(self, x: int, y: int):
        self.pos = pygame.Vector2(x, y)

    def draw(self, display: pygame.Surface):
        pygame.draw.rect(display, RED, (self.pos.x * CELL_SIZE, self.pos.y * CELL_SIZE, CELL_SIZE, CELL_SIZE))
