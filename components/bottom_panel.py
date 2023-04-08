import pygame
import components.buttons as btns

class BottomPanel():
    def __init__(self, screen):
        self.screen = screen
        self.screen_width = 1280
        self.screen_height = 720

        # import images
        self.bpanel_bg = pygame.image.load('assets/images/bpanel_bg.png').convert()
        # self.bpanel_bg = pygame.transform.scale(self.bpanel_bg, (self.screen_width, (self.screen_height//3)*2))

        # import texts
        # title_font = pygame.font.Font('assets/fonts/KenneyRocketSquare.ttf', 72)
        # self.title_text = title_font.render('FreeAI', True, (255, 255, 255))
        # self.title_textRect = self.title_text.get_rect(center=(self.screen_width//2, self.screen_height//4 + 40))

        # import components
        run_button_font = pygame.font.Font('assets/fonts/KenneyFutureNarrow.ttf', 48)
        self.run_button = btns.RunButton((self.screen_width//8)*7 + (self.screen_width//8)//2, (self.screen_height//3)//2, 120, 120, run_button_font, "Run", (255, 255, 255))
        # story_button_font = pygame.font.Font('assets/fonts/KenneyHighSquare.ttf', 60)
        # self.story_button = btns.HomeButton(self.screen_width//2, (self.screen_height//4)*3 - 40, 200, 60, story_button_font, "Story", (255, 255, 255))

        # initialize sprite group
        self.bpanel_group = pygame.sprite.Group(self.run_button)
        # self.home_group = pygame.sprite.Group(self.story_button)
    
    def displayBottomPanel(self):
        self.bottom_surface = pygame.Surface((self.screen_width, self.screen_height//3), pygame.SRCALPHA)
        self.bottom_surface.blit(self.bpanel_bg, (0, 0))
        self.bpanel_group.draw(self.bottom_surface)
        self.screen.blit(self.bottom_surface, (0, (self.screen_height//3)*2))
        
        # self.screen.blit(self.title_text, self.title_textRect)
        # self.home_group.draw(self.screen)