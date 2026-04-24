import pygame
from settings import *
from ball import Ball


class Paddle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.rect = pygame.Rect(x, y, PADDLE_WIDTH, PADDLE_HEIGHT)
        self.direction = pygame.Vector2(0, 0)

    def reset(self):
        self.rect = pygame.Rect(self.x, self.y, PADDLE_WIDTH, PADDLE_HEIGHT)
        self.direction = pygame.Vector2(0, 0)

    def check_ball_collision(self, ball: Ball):
        ball_rect = pygame.Rect(
            ball.center.x - BALL_RADIUS, ball.center.y - BALL_RADIUS,
            BALL_RADIUS * 2, BALL_RADIUS * 2
        )

        return self.rect.colliderect(ball_rect)

    def update(self, key_up, key_down):
        keys = pygame.key.get_pressed()

        if keys[key_up]: self.rect.y -= PADDLE_SPEED
        if keys[key_down]: self.rect.y += PADDLE_SPEED

        if self.rect.y <= 0: self.rect.y = 0
        if self.rect.bottom >= HEIGHT: self.rect.bottom = HEIGHT

    def draw(self, window: pygame.Surface):
        pygame.draw.rect(window, "gray", self.rect)
