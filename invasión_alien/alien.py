#!/usr/bin/python3
# -*- coding: utf-8 -*-

import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """Esta es la clase para cada alien"""

    def __init__(self, ai_ajustes, pantalla):
        """Crear el alien y su posición."""
        super().__init__()
        self.pantalla = pantalla
        self.ai_ajustes = ai_ajustes

        # Cargar imagen del alien.
        self.image = pygame.image.load("images/alien1.png").convert_alpha()
        self.rect = self.image.get_rect()

        # Los aliens cominzan el juego en la parte superior izquierda.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # DArle un valor tipo float a la posición del alien.
        self.x = float(self.rect.x)

    def check_edges(self):
        """Verifica si la el alien está al borde de la pantalla
           devolviendo True."""
        screen_rect = self.pantalla.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

    def update(self):
        """Mover el alien hacia la derecha e izquierda"""
        self.x += (self.ai_ajustes.alien_speed_factor *
                   self.ai_ajustes.fleet_direction)
        self.rect.x = self.x

    def blitme(self):
        """Dibujar al alien según su ubicación."""
        self.pantalla.blit(self.image, self.rect)
