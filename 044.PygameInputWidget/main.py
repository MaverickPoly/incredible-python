import pygame
from settings import *
from input_field import InputField


class App:
    def __init__(self):
        pygame.init()
        pygame.key.set_repeat(200, 50)

        self.display = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption(TITLE)

        self.running = True
        self.clock = pygame.time.Clock()

        self.input_field = InputField(10, 10, 400, 50,
                                      "notoserif", 30, "white", "black")

    def handle_input(self):
        mouse_input = pygame.mouse.get_pressed()

        if mouse_input[0]:
            mouse_pos = pygame.mouse.get_pos()
            if self.input_field.rect.collidepoint(mouse_pos):
                self.input_field.focus()
            else:
                self.input_field.unfocus()

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.KEYDOWN:

                    if self.input_field.focused:
                        if event.key == pygame.K_BACKSPACE:
                            self.input_field.delete_char()
                        else:
                            char = event.unicode
                            if char:
                                self.input_field.add_char(char)

            self.display.fill(BACKGROUND)

            self.handle_input()

            self.input_field.draw(self.display)

            pygame.display.flip()

if __name__ == '__main__':
    App().run()
