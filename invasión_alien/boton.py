#!/usr/bin/python3
# -*- coding: utf-8 -*-

import pygame.font


class Boton():

    def __init__(self, ai_settings, pantalla, msg):
        """Función especial para atributos del botón."""
        self.pantalla = pantalla
        self.pantalla_rect = pantalla.get_rect()

        # Tamaño del botón
        self.ancho, self.alto = 250, 40
        self.boton_color = (200, 255, 20)
        self.texto_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 20)

        # Ubicar el botón al centro de la pantalla
        self.rect = pygame.Rect(400, 400, self.ancho, self.alto)

        # Mensaje del botón.
        self.prep_msg(msg)

    def prep_msg(self, msg):
        """Convertir el botón en una imagen con su mensaje."""
        self.msg_image = self.font.render(msg, True, self.texto_color,
                                          self.boton_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        """Dibujar el botón y luego el mensaje."""
        self.pantalla.fill(self.boton_color, self.rect)
        self.pantalla.blit(self.msg_image, self.msg_image_rect)
