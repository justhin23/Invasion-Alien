#!/usr/bin/python3
# -*- coding: utf-8 -*-

import pygame
from pygame.sprite import Group
from configuracion import Configuracion
from estadisticas import Estadisticas
from pizarra_puntaje import pizarra_puntaje
from boton import Boton
from nave import Nave
from msg_go import Game_over_msg
import game_functions as gf


def run_game():

    pygame.init()
    ai_ajustes = Configuracion()
    pantalla = pygame.display.set_mode(
        (ai_ajustes.screen_width, ai_ajustes.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # Botón de play.
    play_button = Boton(ai_ajustes, pantalla, "Play")

    # Pizarra que muestra las estadísticas.
    stats = Estadisticas(ai_ajustes)
    sb = pizarra_puntaje(ai_ajustes, pantalla, stats)

    # Nave, grupos de balas y grupos de aliens.
    nave = Nave(ai_ajustes, pantalla)
    balas = Group()
    aliens = Group()

    # Crear las filas con aliens.
    gf.create_fleet(ai_ajustes, pantalla, nave, aliens)

    # Mensaje de game over.
    mensaje_go = Game_over_msg(ai_ajustes, pantalla, "Game over")

    # Sonido de fondo.
    pygame.mixer.music.load("Interplanetary_Odyssey.ogg")
    pygame.mixer.music.play(loops=-1)

    # Bucle del juego.
    while True:
        gf.check_events(ai_ajustes, pantalla, stats, sb, play_button, nave,
                        aliens, balas)

        if stats.game_active:
            nave.update()
            gf.update_bullets(ai_ajustes, pantalla, stats, sb, nave, aliens,
                              balas)
            gf.update_aliens(ai_ajustes, pantalla, stats, sb, nave, aliens,
                             balas, mensaje_go)
            

        gf.update_screen(ai_ajustes, pantalla, stats, sb, nave, aliens,
                       balas, play_button, mensaje_go)
        

run_game()
