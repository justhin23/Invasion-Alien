#!/usr/bin/python3
# -*- coding: utf-8 -*-

import pygame
from pygame.sprite import Sprite


class Nave(Sprite):
    "Esta es la clase de la nave que se utilizará para jugar."
    def __init__(self, ai_settings, screen):
        "Posición inicial de la nave en la pantalla"
        super(Nave, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # Cargar imagen de la nave.
        self.image = pygame.image.load("images/nave1.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Ubicar la nave en el centro de la pantalla cuando inicia el juegp.
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # Valor decmal para el centro de la nave.
        self.center = float(self.rect.centerx)

        # Movimiento.
        self.moving_right = False
        self.moving_left = False

    def center_ship(self):
        "Centrar la nave"
        self.center = self.screen_rect.centerx

    def update(self):
        "Actualizar la ubicación de la nave de la nave."

        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor

        # Actualizar la posición con self.center
        self.rect.centerx = self.center

    def blitme(self):
        "Dibujar la imagen de la nave en su posición."
        self.screen.blit(self.image, self.rect)
