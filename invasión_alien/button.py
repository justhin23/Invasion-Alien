import pygame.font

class Button():

    def __init__(self, ai_settings, pantalla, msg):
        """Initialize button attributes."""
        self.pantalla = pantalla
        self.pantalla_rect = pantalla.get_rect()
     
        # Set the dimensions and properties of the button.
        self.ancho, self.alto = 250, 40
        self.boton_color = (200, 255, 20)
        self.texto_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 20)   
  
        # Build the button's rect object, and center it.
        self.rect = pygame.Rect(0, 0, self.ancho, self.alto)
        self.rect.center = self.pantalla_rect.center
        
        # The button message only needs to be prepped once.
        self.prep_msg(msg)

    def prep_msg(self, msg):
        """Turn msg into a rendered image, and center text on the button."""
        self.msg_image = self.font.render(msg, True, self.texto_color,
            self.boton_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center
        
    def draw_button(self):
        # Draw blank button, then draw message.
        self.pantalla.fill(self.boton_color, self.rect)
        self.pantalla.blit(self.msg_image, self.msg_image_rect)