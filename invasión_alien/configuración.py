class Configuración():
    "Es una clase encaragada de todas las configuraciones del juego."

    def __init__(self):
        "Especificaciones varias."
        # Especificaciones para la consola.
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # Ship settings.
        self.ship_limit = 3

        # Especificaciones de las balas.
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3

        # Configuración de aliens.
        self.fleet_drop_speed = 8

        # Aumentos de velocidad.
        self.speedup_scale = 1.1
        # Aumentos en los valores de los puntos.
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        "Configuraciones cambiantes durante el juego."
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1

        # Puntos ganados por cada alien derribado.
        self.alien_points = 10

        # MOvimiento de la nave (1 derecha, -1 izquierda).
        self.fleet_direction = 1

    def increase_speed(self):
        "Velocidades para aliens y puntajes por cada alien."
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
