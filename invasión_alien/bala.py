#!/usr/bin/python3
# -*- coding: utf-8 -*-

import pygame
from pygame.sprite import Sprite


class Bala(Sprite):
    """Clase para hacer balas."""

    def __init__(self, ai_ajustes, pantalla, nave):
        """Crear la bala con una posición inicial igual a la de la nave."""
        super().__init__()
        self.pantalla = pantalla

        # Crear una línea y luego establecer su posición.
        self.rect = pygame.Rect(0, 0, ai_ajustes.bullet_width,
                                ai_ajustes.bullet_height)
        self.rect.centerx = nave.rect.centerx
        self.rect.top = nave.rect.top

        # Darle un valor de tipo float a la posición de la bala.
        self.y = float(self.rect.y)

        self.color = ai_ajustes.bullet_color
        self.speed_factor = ai_ajustes.bullet_speed_factor

    def update(self):
        """Mover la bala hacia arriba en línea recta."""
        # Actualizar el valor float de la posición de la bala.
        self.y -= self.speed_factor
        self.rect.y = self.y

    def dibujo_bala(self):
        """Dibujar la bala en la pantalla (consola)."""
        pygame.draw.rect(self.pantalla, self.color, self.rect)
