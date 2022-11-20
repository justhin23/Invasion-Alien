#!/usr/bin/python3
# -*- coding: utf-8 -*-

class Estadisticas():
    "Actualización de estadísticas del juego."

    def __init__(self, ai_settings):
        "Iniciar estadísticas."
        self.ai_settings = ai_settings
        self.reset_stats()

        # Iniciar el juego en estado inactivo.
        self.game_active = False

        # La puntuación más alta antes de iniciar es 0.
        self.high_score = 0

    def reset_stats(self):
        "Estadísticas que cambian durante la partida."
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1
