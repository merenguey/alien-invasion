import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """class for bullets"""

    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.picture = pygame.image.load("/home/deck/Pictures/game art/alien invasion/heart_bullet.png")
        self.image = pygame.transform.scale(self.picture, (self.settings.bullet_size, self.settings.bullet_size))

        #create temp rect at 0,0 before setting correct pos
        self.rect = self.image.get_rect()
        self.rect.midtop = ai_game.ship.rect.midtop

        self.y = float(self.rect.y)

    def update(self):
        self.y -= self.settings.bullet_speed
        self.rect.y = self.y

    def draw_bullet(self):
        self.screen.blit(self.image, self.rect)