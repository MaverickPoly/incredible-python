import argparse
import os.path

import pygame


WIDTH, HEIGHT = 500, 300
FPS = 30


class MusicPlayer:
    def __init__(self, filepath: str, filename: str):
        pygame.init()

        self.display = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption(filename)

        self.running = True
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont("serif", 28)

        self.current_pos = 0
        self.start_time = pygame.time.get_ticks()
        self.playing = True

        pygame.mixer.music.load(filepath)
        pygame.mixer.music.play()

    def _get_pos(self):
        if self.playing:
            elapsed = (pygame.time.get_ticks() - self.start_time) / 1000
            return self.current_pos + elapsed
        return self.current_pos

    def seek(self, seconds):
        seconds = max(seconds, 0)

        pygame.mixer.music.stop()
        pygame.mixer.music.play(start=seconds)

        self.current_pos = seconds
        self.start_time = pygame.time.get_ticks()

    def update(self):
        self.display.fill("black")

        # Draw some text
        volume_text = self.font.render(f"Volume: {round(pygame.mixer.music.get_volume(), 1)}", True, "white")
        pos_text = self.font.render(f"Position: {round(self._get_pos())}", True, "white")

        self.display.blit(volume_text, (10, 10))
        self.display.blit(pos_text, (10, volume_text.get_height() + 20))

        self.clock.tick(FPS)
        pygame.display.flip()

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        pygame.mixer.music.set_volume(min(pygame.mixer.music.get_volume() + 0.1, 1.0))
                    if event.key == pygame.K_DOWN:
                        pygame.mixer.music.set_volume(max(pygame.mixer.music.get_volume() - 0.1, 0.0))
                    if event.key == pygame.K_LEFT:
                        self.seek(self._get_pos() - 5)
                    if event.key == pygame.K_RIGHT:
                        self.seek(self._get_pos() + 5)
                    if event.key == pygame.K_SPACE:
                        if self.playing:
                            self.current_pos = self._get_pos()
                            pygame.mixer.music.pause()
                            self.playing = False
                        else:
                            pygame.mixer.music.unpause()
                            self.start_time = pygame.time.get_ticks()
                            self.playing = True
            self.update()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Simple Music Player app")
    parser.add_argument("filepath", help="Path to your audio file")
    args = parser.parse_args()

    filepath = args.filepath
    filename = os.path.basename(filepath)

    player = MusicPlayer(filepath, filename)
    player.run()
