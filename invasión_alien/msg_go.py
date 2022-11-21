#!/usr/bin/python3
# -*- coding: utf-8 -*-

import pygame.font


class Game_over_msg():
    "Esta clase es un mensaje de game over."

    def __init__(self, ai_ajustes, pantalla, msg):
        "Características del registro de puntuación"
        self.pantalla = pantalla
        self.pantalla_rect = pantalla.get_rect()

        # Tamaño del botón
        self.ancho, self.alto = 250, 70
        self.fondo_color = (230, 230, 230)
        self.texto_color = (255, 0, 0)
        self.font = pygame.font.SysFont(None, 30)

        # Ubicar el botón al centro de la pantalla
        self.rect = pygame.Rect(0, 0, self.ancho, self.alto)
        self.rect.center = self.pantalla_rect.center

        # Preparar información del mensaje.
        self.prepa_msg(msg)

    def prepa_msg(self, msg):
        """Convertir el botón en una imagen con su mensaje."""
        self.msg_image = self.font.render(msg, True, self.texto_color,
                                          self.fondo_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_msg(self):
        """Dibujar el fondo y luego el mensaje."""
        self.pantalla.fill(self.fondo_color, self.rect)
        self.pantalla.blit(self.msg_image, self.msg_image_rect)
