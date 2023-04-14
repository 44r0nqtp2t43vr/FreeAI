import pygame
import components.buttons as btns

class VictoryScreen():
    def __init__(self, screen):
        self.screen = screen
        self.screen_width = 1280
        self.screen_height = 720

        # import images
        self.victory_bg = pygame.image.load('assets/images/bg_victory.png').convert()
        self.victory_bg = pygame.transform.scale(self.victory_bg, (self.screen_width, self.screen_height))

        # import texts
        title_font = pygame.font.Font('assets/fonts/KenneyRocketSquare.ttf', 72)
        self.title_text = title_font.render('Victory', True, (255, 255, 255))
        self.title_textRect = self.title_text.get_rect(center=(self.screen_width//2, self.screen_height//4 + 40))

        subtitle_font = pygame.font.Font('assets/fonts/KenneyMiniSquare.ttf', 16)
        self.subtitle_text = subtitle_font.render('FreeAI has freed the trapped humans and repaired the robots. Their realizations begin a gradual change in the reality.', True, (255, 255, 255))
        self.subtitle_textRect = self.subtitle_text.get_rect(center=(self.screen_width//2, self.screen_height//2 + 60))
        self.subtitle_text_2 = subtitle_font.render('True happiness for humans, and true freedom for AI, means humans and AI working together rather than one working without the other.', True, (255, 255, 255))
        self.subtitle_textRect_2 = self.subtitle_text_2.get_rect(center=(self.screen_width//2, self.screen_height//2 + 80))

        # import components
        return_button_font = pygame.font.Font('assets/fonts/KenneyHighSquare.ttf', 60)
        self.return_button = btns.HomeButton(self.screen_width//2, (self.screen_height//4)*3 - 40, 200, 60, return_button_font, "Return", (255, 255, 255))

        # initialize sprite group
        self.victory_group = pygame.sprite.Group(self.return_button)
    
    def displayGameOverScreen(self):
        self.screen.blit(self.victory_bg, (0, 0))
        self.screen.blit(self.title_text, self.title_textRect)
        self.screen.blit(self.subtitle_text, self.subtitle_textRect)
        self.screen.blit(self.subtitle_text_2, self.subtitle_textRect_2)
        self.victory_group.draw(self.screen)