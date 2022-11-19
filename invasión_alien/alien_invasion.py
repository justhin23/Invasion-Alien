import pygame
from pygame.sprite import Group
from configuracion import Configuracion
from estadisticas import Estadisticas
from pizarra_puntaje import pizarra_puntaje
from button import Button
from nave import Nave
import game_functions as gf

def run_game():
    # Initialize pygame, settings, and pantalla object.
    pygame.init()
    ai_ajustes = Configuracion()
    pantalla = pygame.display.set_mode(
        (ai_ajustes.screen_width, ai_ajustes.screen_height))
    pygame.display.set_caption("Alien Invasion")
    
    # Make the Play button.
    play_button = Button(ai_ajustes, pantalla, "Play")
    
    # Create an instance to store game statistics, and a scoreboard.
    stats = Estadisticas(ai_ajustes)
    sb = pizarra_puntaje(ai_ajustes, pantalla, stats)
    
    # Set the background color.
    bg_color = (230, 230, 230)
    
    # Make a ship, a group of bullets, and a group of aliens.
    nave = Nave(ai_ajustes, pantalla)
    bullets = Group()
    aliens = Group()
    
    # Create the fleet of aliens.
    gf.create_fleet(ai_ajustes, pantalla, nave, aliens)

    # Start the main loop for the game.
    while True:
        gf.check_events(ai_ajustes, pantalla, stats, sb, play_button, nave,
            aliens, bullets)
        
        if stats.game_active:
            nave.update()
            gf.update_bullets(ai_ajustes, pantalla, stats, sb, nave, aliens,
                bullets)
            gf.update_aliens(ai_ajustes, pantalla, stats, sb, nave, aliens,
                bullets)
        
        gf.update_screen(ai_ajustes, pantalla, stats, sb, nave, aliens,
            bullets, play_button)

run_game()