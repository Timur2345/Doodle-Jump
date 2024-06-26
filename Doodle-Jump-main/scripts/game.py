import pygame
from scripts.constants import display_size
from scripts.function import load_image
from scripts.player import Player
from scripts.platform_generator import PlatformGenerator
class Game():
    def __init__(self):
        self.background = load_image("assets", "images", "background.png")
        self.platforms = []
        self.player = Player(
            load_image("assets","images","player.png"),
            (240,600),
            20,
            10,
            0.75,
        )
        self.offset_y=0
        self.platform_generator = PlatformGenerator(200)
        self.platform_generator.create_start_cofiguration()

    def render_objects(self,scene):
        scene.blit(self.background, (0,0))
        for platform in self.platforms:
            platform.render(scene, self.offset_y)
        self.player.render(scene, self.offset_y)
    def process_key_down_event(self,key):
        if key == pygame.K_a:
            self.player.is_walking_left = True
        if key == pygame.K_d:
            self.player.is_walking_right = True
    def process_key_up_event(self,key):
        if key == pygame.K_a:
            self.player.is_walking_left = False
        if key == pygame.K_d:
            self.player.is_walking_right = False
    def update_objects(self):
        for platform in self.platforms:
            if self.player.collide(platform.rect):
                self.player.on_platform = True
        self.player.update()
        if self.player.rect.bottom - self.offset_y < display_size[1] / 3:
            self.offset_y = self.player.rect.bottom - display_size[1] / 3
        self.platform_generator.update(self.offset_y, self.platforms)
