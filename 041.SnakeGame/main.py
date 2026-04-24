import random
import pprint

import pygame

from settings import *
from snake import Snake
from fruit import Fruit


class Game:
    def __init__(self):
        # Global Settings
        pygame.init()
        self.record = self.load_record()

        # Window
        self.display = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption(TITLE)

        # Game states
        self.clock = pygame.time.Clock()
        self.running = True
        self.score = 3
        self.game_over = True

        self.last_fruit_generate = pygame.time.get_ticks()
        self.can_generate_fruit = False
        self.snake_fruit_generate_timeout = FRUIT_GENERATE_TIMEOUT

        # Game elements
        self.snake = Snake()
        self.fruits = []
        self.font = pygame.font.SysFont("freeserif", 40)
        # pprint.pprint(pygame.font.get_fonts())

    def save_record(self):
        try:
            with open(RECORD_FILENAME, "w") as f:
                f.write(str(max(self.record, self.score)))
        except Exception as e:
            print(f"Failed to save record: {e}")
            self.running = False

    def load_record(self):
        try:
            with open("record.txt", "r") as file:
                record_score = int(file.read().strip())
                return record_score
        except Exception as e:
            print(f"Failed to load record score: {e}")
            self.running = False

    def reset_game(self):
        self.score = 3
        self.snake = Snake()
        self.fruits = []
        self.last_fruit_generate = pygame.time.get_ticks()
        self.can_generate_fruit = False
        self.snake_fruit_generate_timeout = FRUIT_GENERATE_TIMEOUT

    def quit_game(self):
        self.save_record()
        self.running = False

    def draw_background(self):
        for i in range(ROWS):
            for j in range(COLS):
                color = LIGHT_GREEN if (i + j) % 2 == 0 else DARK_GREEN
                x, y = CELL_SIZE * i, CELL_SIZE * j
                pygame.draw.rect(self.display, color, (x, y, CELL_SIZE, CELL_SIZE))

    def generate_fruit(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.last_fruit_generate > self.snake_fruit_generate_timeout:
            self.can_generate_fruit = True
            self.snake_fruit_generate_timeout += 50

        if not self.can_generate_fruit:
            return

        self.last_fruit_generate = current_time
        self.can_generate_fruit = False
        x, y = random.randint(0, ROWS - 1), random.randint(0, COLS - 1)
        fruit = Fruit(x, y)
        self.fruits.append(fruit)

    def draw_texts(self):
        score_text = self.font.render(f"{self.score}", True, BLACK)
        self.display.blit(score_text, (10, 10))

    def update(self):
        pygame.display.update()

        self.generate_fruit()
        self.snake.update()

        snake_fruit_collision_index = self.snake.check_fruit_collision(self.fruits)
        if snake_fruit_collision_index != -1:
            self.fruits.pop(snake_fruit_collision_index)
            self.snake.grow()
            self.score += 1

        if self.snake.lost:
            self.game_over = True

    def draw(self):
        self.draw_background()

        for fruit in self.fruits:
            fruit.draw(self.display)
        self.snake.draw(self.display)
        self.draw_texts()

    def draw_game_over_screen(self):
        current_score_text = self.font.render(f"Score: {self.score}", True, BLACK)
        record_score_text = self.font.render(f"Record: {self.record}", True, BLACK)
        info_text = self.font.render(f"Press Enter to start...", True, BLACK)
        quit_text= self.font.render(f"Press q to quit...", True, BLACK)

        self.display.fill(WHITE)
        self.display.blit(current_score_text, ((WIDTH - current_score_text.get_width()) / 2, 200))
        self.display.blit(record_score_text, ((WIDTH - record_score_text.get_width()) / 2, 300))
        self.display.blit(info_text, ((WIDTH - info_text.get_width()) / 2, 400))
        self.display.blit(quit_text, ((WIDTH - quit_text.get_width()) / 2, 500))
        pygame.display.update()


    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.quit_game()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN and self.game_over:
                        self.reset_game()
                        self.game_over = False
                    if event.key == pygame.K_q and self.game_over:
                        self.quit_game()

            if self.game_over:
                self.draw_game_over_screen()
            else:
                self.update()
                self.draw()
            self.clock.tick(FPS)


if __name__ == '__main__':
    game = Game()
    game.run()
