#!/usr/bin/python3
# -*- coding: utf-8 -*-

import pygame
from pygame.sprite import Group
from configuracion import Configuracion
from estadisticas import Estadisticas
from pizarra_puntaje import pizarra_puntaje
from boton import Boton
from nave import Nave
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
    bullets = Group()
    aliens = Group()

    # Crear las filas con aliens.
    gf.create_fleet(ai_ajustes, pantalla, nave, aliens)

    # Sonido de fondo.
    #pygame.mixer.music.load("Interplanetary_Odyssey.ogg")
    #pygame.mixer.music.play()

    # Bucle del juego.
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
