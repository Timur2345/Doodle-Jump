import pygame
import os
from scripts.game import Game


class App():

    def __init__(self):
        pygame.display.set_caption("DoodleJump")
        image = pygame.image.load(os.path.join("assets", "icons", "icon.ico"))
        pygame.display.set_icon(image)
        self.working = True
        self.FPS = 60
        self.scene = pygame.display.set_mode((480, 720))
        self.clock = pygame.time.Clock() 
        self.game = Game()
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.working = False

    def update(self):
        ...

    def render(self):
        self.scene.fill((0,0,0))
        self.game.render_objects(self.scene)
        pygame.display.update()
    def run(self):
        while self.working:
            self.handle_events()
            self.update()
            self.render()
            self.clock.tick(self.FPS)