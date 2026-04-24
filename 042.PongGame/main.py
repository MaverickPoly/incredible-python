import pygame
from settings import *
from paddle import Paddle
from ball import Ball


class Game:
    def __init__(self):
        # Init
        pygame.init()

        # Window
        self.window = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption(TITLE)

        # Game states
        self.clock = pygame.time.Clock()
        self.running = True
        self.font = pygame.font.SysFont("notoserif", 40)
        # notoserif

        # Game elements
        self.left_paddle = Paddle(MARGIN, (HEIGHT - PADDLE_HEIGHT) / 2)
        self.right_paddle = Paddle(WIDTH - MARGIN - PADDLE_WIDTH, (HEIGHT - PADDLE_HEIGHT) / 2)
        self.ball = Ball((WIDTH / 2, HEIGHT / 2))

        self.left_paddle_score = 0
        self.right_paddle_score = 0

    def draw_text(self):
        left_paddle_score = self.font.render(str(self.left_paddle_score), True, "white")
        right_paddle_score = self.font.render(str(self.right_paddle_score), True, "white")

        self.window.blit(left_paddle_score, (MARGIN, MARGIN))
        self.window.blit(right_paddle_score, (WIDTH - MARGIN - right_paddle_score.get_width(), MARGIN))

    def update(self):
        pygame.display.flip()

        self.left_paddle.update(pygame.K_w, pygame.K_s)
        self.right_paddle.update(pygame.K_UP, pygame.K_DOWN)

        if self.left_paddle.check_ball_collision(self.ball) or self.right_paddle.check_ball_collision(self.ball):
            self.ball.bounce_x()
            self.ball.move()

        status = self.ball.update()
        if status != 0:
            self.ball.reset()
            self.right_paddle.reset()
            self.left_paddle.reset()
            if status == -1:
                self.right_paddle_score += 1
            elif status == +1:
                self.left_paddle_score += 1

    def draw(self):
        self.window.fill("black")

        self.draw_text()
        self.left_paddle.draw(self.window)
        self.right_paddle.draw(self.window)
        self.ball.draw(self.window)

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            self.update()
            self.draw()
            self.clock.tick(FPS)


if __name__ == '__main__':
    game = Game()
    game.run()
