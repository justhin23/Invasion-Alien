#!/usr/bin/python3
# -*- coding: utf-8 -*-

import pygame.font
from pygame.sprite import Group
from nave import Nave


class pizarra_puntaje():
    "Esta clase es una pizarra que informa la puntuación del usuario."

    def __init__(self, ai_ajustes, pantalla, estadisticas):
        "Características del registro de puntuación"
        self.screen = pantalla
        self.screen_rect = pantalla.get_rect()
        self.ai_settings = ai_ajustes
        self.stats = estadisticas

        # Configuración de la pizarra.
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

        # Preparar información de la pizarra.
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_ships()

    def prep_score(self):
        "Crear una imagen con información de puntaje"
        rounded_score = int(round(self.stats.score, -1))
        score_str = "{:,}".format(rounded_score)
        self.score_image = self.font.render(score_str, True, self.text_color,
                                            self.ai_settings.bg_color)

        # Ubicar la puntuación en la parte superior derecha de la consola.
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def prep_high_score(self):
        "Crear una imagen con la puntuación más alta alcanzada."
        puntuacion_alta = int(round(self.stats.high_score, -1))
        puntuacion_alta_str = "{:,}".format(puntuacion_alta)
        self.high_score_image = self.font.render(puntuacion_alta_str, True,
                                                 self.text_color,
                                                 self.ai_settings.bg_color)

        # Ubicar la puntuación más alta en la parte superior derecha
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top

    def prep_level(self):
        """Mostrar el nivel con una imagen renderizada."""
        self.level_image = self.font.render(str(self.stats.level), True,
                                            self.text_color,
                                            self.ai_settings.bg_color)

        # Posición del nivel en la pantalla.
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10

    def prep_ships(self):
        """Mostrar cuantas vidas queda."""
        self.ships = Group()
        for nave_numero in range(self.stats.ships_left):
            nave = Nave(self.ai_settings, self.screen)
            nave.rect.x = 10 + nave_numero * nave.rect.width
            nave.rect.y = 10
            self.ships.add(nave)

    def show_score(self):
        """Dibujar puntuación en la pantalla."""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.ships.draw(self.screen)
