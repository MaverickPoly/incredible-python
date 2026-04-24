import pygame
from settings import *
from random import choice


class Ball:
    def __init__(self, center):
        self.initial_pos = center
        self.center = pygame.Vector2(center)
        self.direction = pygame.Vector2(choice([-1, 1]), choice([-1, 1]))

    def bounce_x(self):
        self.direction.x *= -1

    def bounce_y(self):
        self.direction.y *= -1

    def reset(self):
        self.center = pygame.Vector2(self.initial_pos)
        self.direction = pygame.Vector2(choice([-1, 1]), choice([-1, 1]))

    def move(self):
        self.center += self.direction * BALL_SPEED

    def update(self):
        """-1: Went left; 0: On track; +1: went right"""
        self.move()

        # TOP
        if self.center.y - BALL_RADIUS <= 0: self.bounce_y()
        # BOTTOM
        if self.center.y + BALL_RADIUS >= HEIGHT: self.bounce_y()

        # LEFT
        if self.center.x - BALL_RADIUS <= 0:
            return -1

        # RIGHT
        if self.center.x + BALL_RADIUS >= WIDTH:
            return 1

        return 0

    def draw(self, window: pygame.Surface):
        pygame.draw.circle(window, "red", self.center, BALL_RADIUS)
