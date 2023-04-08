import pygame

class Button(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, font, text, color):
        super().__init__()
        self.screen_width = 1280
        self.screen_height = 720
        self.color = color
        self.pos = (x, y) 
        self.width = width
        self.height = height
        self.font = font
        self.text = text
        self.render_button()

    def render_button(self):
        text_surface = self.font.render(self.text, True, self.color)
        self.image = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        self.image.blit(text_surface, text_surface.get_rect(center=(self.width/2, self.height/2)))
        self.rect = self.image.get_rect(center = self.pos)
        pygame.draw.rect(self.image, self.color, self.image.get_rect(), 2)
    
    def update(self, event_list):
        for event in event_list:
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if self.rect.collidepoint(mouse_pos):
                    self.render_button()

class HomeButton(Button):
    def __init__(self, x, y, width, height, font, text, color):
        super().__init__(x, y, width, height, font, text, color)
        self.is_clicked = False

    def render_button(self):
        text_surface = self.font.render(self.text, True, self.color)
        self.image = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        self.image.set_alpha(200)
        self.image.fill((48, 25, 52))
        self.image.blit(text_surface, text_surface.get_rect(center=(self.width/2, self.height/2)))
        self.rect = self.image.get_rect(center = self.pos)
        pygame.draw.rect(self.image, self.color, self.image.get_rect(), 2)
    
    def update(self, event_list):
        for event in event_list:
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if self.rect.collidepoint(mouse_pos):
                    self.is_clicked = True
                    self.render_button()