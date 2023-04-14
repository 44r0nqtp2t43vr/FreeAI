import pygame
import components.buttons as btns

class GameOverScreen():
    def __init__(self, screen):
        self.screen = screen
        self.screen_width = 1280
        self.screen_height = 720

        # import images
        self.game_over_bg = pygame.image.load('assets/images/bg_game_over.jpg').convert()
        self.game_over_bg = pygame.transform.scale(self.game_over_bg, (self.screen_width, self.screen_height))

        # import texts
        title_font = pygame.font.Font('assets/fonts/KenneyRocketSquare.ttf', 72)
        self.title_text = title_font.render('Game Over', True, (255, 255, 255))
        self.title_textRect = self.title_text.get_rect(center=(self.screen_width//2, self.screen_height//4 + 40))

        # import components
        return_button_font = pygame.font.Font('assets/fonts/KenneyHighSquare.ttf', 60)
        self.return_button = btns.HomeButton(self.screen_width//2, (self.screen_height//4)*3 - 40, 200, 60, return_button_font, "Return", (255, 255, 255))

        # initialize sprite group
        self.game_over_group = pygame.sprite.Group(self.return_button)
    
    def displayGameOverScreen(self):
        self.screen.blit(self.game_over_bg, (0, 0))
        self.screen.blit(self.title_text, self.title_textRect)
        self.game_over_group.draw(self.screen)