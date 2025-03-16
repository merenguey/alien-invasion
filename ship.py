import pygame
class Ship:
    #Class to manage player
    
    def __init__(self, ai_game):
        #Initialize ship
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        #Load the ship image and get it's rect
        self.picture = pygame.image.load("/home/deck/Pictures/game art/alien invasion/spaceship.png")
        self.image = pygame.transform.scale(self.picture, (120, 120))
        self.rect = self.image.get_rect()

        #Start each new ship at the bottom center of the screen.
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)

        #Set movement flag to false by default and speed to default value
        self.moving_right = False
        self.moving_left = False

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.speed
        
        self.rect.x = self.x

    def blitme(self):
        #Draw the ship at it's current location.
        self.screen.blit(self.image, self.rect)
    
    