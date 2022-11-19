import pygame
from pygame.sprite import Sprite

class Bala(Sprite):
    """Clase para hacer balas."""

    def __init__(self, ai_ajustes, pantalla, nave):
        """Create a bullet object, at the ship's current position."""
        super().__init__()
        self.pantalla = pantalla
        
        # Create bullet rect at (0, 0), then set correct position.
        self.rect = pygame.Rect(0, 0, ai_ajustes.bullet_width,
            ai_ajustes.bullet_height)
        self.rect.centerx = nave.rect.centerx
        self.rect.top = nave.rect.top
        
        # Store a decimal value for the bullet's position.
        self.y = float(self.rect.y)

        self.color = ai_ajustes.bullet_color
        self.speed_factor = ai_ajustes.bullet_speed_factor

    def update (self):
        """Move the bullet up the pantalla."""
        # Update the decimal position of the bullet.
        self.y -= self.speed_factor
        # Update the rect position.
        self.rect.y = self.y

    def dibujo_bala(self):
        """Draw the bullet to the pantalla."""
        pygame.draw.rect(self.pantalla, self.color, self.rect)