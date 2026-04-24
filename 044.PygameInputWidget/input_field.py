import pygame


class InputField:
    """Input Field Widget implementation"""

    def __init__(self, x, y, width, height, font: str, font_size, bg_color, text_color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.bg_color = bg_color
        self.text_color = text_color

        self.current_text = ""
        self.surface = pygame.Surface((width, height))
        self.surface.set_clip(pygame.Rect(0, 0, self.width, self.height))
        self.font = pygame.font.SysFont(font, font_size)
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

        self.focused = True

    def focus(self):
        self.focused = True
    def unfocus(self):
        self.focused = False

    def add_char(self, char: str):
        self.current_text += char

    def delete_char(self):
        self.current_text = self.current_text[:-1]

    def draw(self, surface: pygame.Surface):
        self.surface.fill(self.bg_color)

        # Text to Input field
        text_surface = self.font.render(self.current_text, True, self.text_color)

        margin_vertical = (self.height - text_surface.get_height()) // 2
        if margin_vertical < 0: margin_vertical = 0

        self.surface.blit(text_surface, (10, margin_vertical))
        surface.blit(self.surface, (self.x, self.y))

