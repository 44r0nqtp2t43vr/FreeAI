import pygame
import components.buttons as btns

class Level0Screen():
    def __init__(self, screen):
        self.screen = screen
        self.screen_width = 1280
        self.screen_height = 720

        # import images
        self.lvl0_bg = pygame.image.load('assets/images/lvl0_bg.jpg').convert()
        # self.lvl0_bg = pygame.transform.scale(self.lvl0_bg, (self.screen_width, (self.screen_height//3)*2))

        # import texts
        # title_font = pygame.font.Font('assets/fonts/KenneyRocketSquare.ttf', 72)
        # self.title_text = title_font.render('FreeAI', True, (255, 255, 255))
        # self.title_textRect = self.title_text.get_rect(center=(self.screen_width//2, self.screen_height//4 + 40))

        # import components
        # story_button_font = pygame.font.Font('assets/fonts/KenneyHighSquare.ttf', 60)
        # self.story_button = btns.HomeButton(self.screen_width//2, (self.screen_height//4)*3 - 40, 200, 60, story_button_font, "Story", (255, 255, 255))

        # initialize sprite group
        # self.home_group = pygame.sprite.Group(self.story_button)
    
    def displayLevel0Screen(self):
        self.top_surface = pygame.Surface((self.screen_width, (self.screen_height//3)*2), pygame.SRCALPHA)
        self.top_surface.blit(self.lvl0_bg, (0, 0))
        self.screen.blit(self.top_surface, (0, 0))
        # self.screen.blit(self.title_text, self.title_textRect)
        # self.home_group.draw(self.screen)