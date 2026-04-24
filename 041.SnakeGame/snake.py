import pygame
from settings import *
from fruit import Fruit


class Snake:
    """Snake Element of the Game"""

    def __init__(self):
        self.body = [
            pygame.Vector2(12, 10),
            pygame.Vector2(11, 10),
            pygame.Vector2(10, 10)
        ]

        self.direction = pygame.Vector2(RIGHT)
        self.lost = False

        # Move timeout
        self.last_move = pygame.time.get_ticks()
        self.can_move = False

    def handle_input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP] and self.direction != DOWN: self.direction = pygame.Vector2(UP)
        elif keys[pygame.K_DOWN] and self.direction != UP: self.direction = pygame.Vector2(DOWN)
        elif keys[pygame.K_LEFT] and self.direction != RIGHT: self.direction = pygame.Vector2(LEFT)
        elif keys[pygame.K_RIGHT] and self.direction != LEFT: self.direction = pygame.Vector2(RIGHT)

    def move(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.last_move > SNAKE_MOVE_TIMEOUT:
            self.can_move = True
            self.last_move = current_time

        if not self.can_move:
            return

        self.can_move = False
        current = self.body[0].copy()
        self.body[0] += self.direction

        for i in range(1, len(self.body)):
            part = self.body[i]
            self.body[i] = current
            current = part

    def check_lost(self):
        head = self.body[0]
        x, y = head.x * CELL_SIZE, head.y * CELL_SIZE

        if x < 0 or x >= WIDTH or y < 0 or y >= HEIGHT:
            self.lost = True

        for i in range(len(self.body)):
            for j in range(len(self.body)):
                if i == j:
                    continue

                if self.body[i] == self.body[j]:
                    self.lost = True
                    return

    def check_fruit_collision(self, fruits: list[Fruit]):
        head = self.body[0]
        for i in range(len(fruits)):
            if fruits[i].pos == head:
                return i
        return -1

    def grow(self):
        new_back_pos = self.body[-1].copy()
        new_back_pos += self.direction * -1
        self.body.append(new_back_pos)

    def update(self):
        self.handle_input()
        self.move()
        self.check_lost()

    def draw(self, display: pygame.Surface):
        for part in self.body:
            x, y = part.x * CELL_SIZE, part.y * CELL_SIZE
            pygame.draw.rect(display, BLUE, (x, y, CELL_SIZE, CELL_SIZE))
