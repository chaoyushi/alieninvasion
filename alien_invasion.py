import pygame
from pygame.sprite import Group

from settings import Settings
from game_stats import GameStats
from ship import Ship
from button import Button
from scoreboard import Scoreboard
import game_functions as gf


pygame.mixer.init()
pygame.mixer_music.load('music/bg_music.wav')
pygame.mixer_music.play()
def run_game():
    # Initialize pygame, settings, and screen object.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    #创建play按钮
    play_button=Button(ai_settings,screen,"Play")
    
    # Create an instance to store game statistics.
    stats = GameStats(ai_settings)
    sb=Scoreboard(ai_settings,screen,stats)

    

    
    # Make a ship, a group of bullets, and a group of aliens.
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()
    
    # Create the fleet of aliens.
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # Start the main loop for the game.
    while True:
        gf.check_events(ai_settings, screen,stats,sb,play_button, ship,aliens,
                        bullets)
        
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen,stats,sb, ship, aliens, bullets)
            gf.update_aliens(ai_settings,  screen,stats,sb, ship, aliens, bullets)
        
        gf.update_screen(ai_settings, screen, stats,sb,ship, aliens, bullets,play_button)


run_game()
