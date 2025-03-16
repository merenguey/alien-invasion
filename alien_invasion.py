import sys
from time import sleep
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet
ticks = []
class AlienInvasion:
    #Overall class to manage game assets and behavior.

    def __init__(self):
        #Initialize game and create game resources.
        pygame.init()
        self.clock = pygame.time.Clock()

        self.settings = Settings()
        self.screen = pygame.display.set_mode((1280, 720), pygame.SCALED, vsync=1)
        self.background = pygame.transform.scale(pygame.image.load("/home/deck/Pictures/game art/alien invasion/background.jpg"), self.screen.get_size())
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Alien Invasion")
        self.ship = Ship(self)
        self.bg_color = (self.settings.bg_color)
        self.bullets = pygame.sprite.Group()
    
    
        
    def run_game(self):
        #Start main game loop
        while True:
            self._check_events()
            self._update_screen()
            self._update_bullets()
            self.ship.update()
            self.clock.tick(self.settings.frame_rate)

    def _check_keyup_events(self, event):
        if event.key == pygame.K_d:
            self.ship.moving_right = False
        if event.key == pygame.K_a:
            self.ship.moving_left = False

    def _check_keydown_events(self, event):
        if event.key == pygame.K_d:
            self.ship.moving_right = True
        if event.key == pygame.K_a:
                self.ship.moving_left = True
        if event.key == pygame.K_ESCAPE:
             sys.exit()
        if event.key == pygame.K_SPACE:
             self._fire_bullet(pygame.time.get_ticks(), ticks)
    
    #Check events (duh)
    def _check_events(self):
     for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    self._check_keydown_events(event)
                elif event.type == pygame.KEYUP:
                     self._check_keyup_events(event)
                    
    def _fire_bullet(self, current_ticks,ticks):
         if len(ticks) == 0:
             new_bullet = Bullet(self)
             self.bullets.add(new_bullet)
             ticks.append(current_ticks)

         elif current_ticks - ticks[0] > 500:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)
            ticks.append(current_ticks)
            del ticks[0]

    def _update_bullets(self):
         self.bullets.update()
         for bullet in self.bullets.copy():
                 if bullet.rect.bottom <= 0:
                      self.bullets.remove(bullet)

    #Make the most recently drawn screen visible.
    def _update_screen(self):
        self.screen.blit(self.background, self.background.get_rect())
        for bullet in self.bullets.sprites():
             bullet.draw_bullet()
        self.ship.blitme()
        pygame.display.flip()

if __name__ == "__main__":
    #Make a game instance and run the game
    ai = AlienInvasion()
    ai.run_game()