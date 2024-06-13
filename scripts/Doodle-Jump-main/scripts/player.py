from scripts.sprite import Sprite

class Player(Sprite):
    def __init__(self, center, image, jump, speed, gravity):
        super().__init__(center, image)
        self.jump = jump
        self.speed = speed
        self.gravity = gravity
        self.is_walking_right = False
        self.is_walking_left = False
        self.velocity_y = 0
        self.on_platform = False
    def update(self):
        self.velocity_y = min(self.velocity_y + self.gravity, 15)
        self.rect.y += self.velocity_y

        if self.is_walking_left != self.is_walking_right:
            if self.is_walking_left:
                self.rect.x -= self.speed
            else:
                self.rect.x += self.speed