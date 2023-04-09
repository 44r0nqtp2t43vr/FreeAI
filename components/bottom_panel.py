import pygame
import components.buttons as btns
import components.text_input as txin
import components.text as text

class BottomPanel():
    def __init__(self, screen, lives):
        self.screen = screen
        self.screen_width = 1280
        self.screen_height = 720
        self.lives = lives
        self.prompt = ''

        # import images
        self.bpanel_bg = pygame.image.load('assets/images/bpanel_bg.png').convert()
        # self.bpanel_bg = pygame.transform.scale(self.bpanel_bg, (self.screen_width, (self.screen_height//3)*2))

        # import texts
        # title_font = pygame.font.Font('assets/fonts/KenneyRocketSquare.ttf', 72)
        # self.title_text = title_font.render('FreeAI', True, (255, 255, 255))
        # self.title_textRect = self.title_text.get_rect(center=(self.screen_width//2, self.screen_height//4 + 40))

        # import components
        run_button_font = pygame.font.Font('assets/fonts/KenneyFutureNarrow.ttf', 48)
        self.run_button = btns.RunButton((self.screen_width//8)*7 + (self.screen_width//8)//2, (self.screen_height//3)//2, 120, 120, run_button_font, "Run", (53, 186, 243))
        text_input_font = pygame.font.Font('assets/fonts/KenneyMiniSquare.ttf', 32)
        self.text_input = txin.TextInput((self.screen_width//2)+240, (self.screen_height//3)//2, 440, 200, text_input_font, (255, 255, 255))
        title_font = pygame.font.Font('assets/fonts/KenneyFutureNarrow.ttf', 32)
        self.title = text.Text((self.screen_width//8)*3-20, (self.screen_height//3)//8, 280, 60, title_font, 'Code Editor', (255, 255, 255))
        player_font = pygame.font.Font('assets/fonts/KenneyFutureNarrow.ttf', 32)
        self.player = text.Text(self.screen_width//8+10, (self.screen_height//3)//8, 280, 60, player_font, 'Player', (53, 186, 243))
        prompt_text_font = pygame.font.Font('assets/fonts/KenneyMiniSquare.ttf', 16)
        self.prompt_text = text.MultilineText((self.screen_width//8)*3-20, ((self.screen_height//3)//8)*5, 280, 180, prompt_text_font, self.prompt, (255, 255, 255))

        # initialize sprite group
        self.bpanel_group = pygame.sprite.Group(self.run_button, self.text_input)
    
    def listen(self, lives, prompt):
        self.lives = lives
        self.prompt = prompt

        prompt_text_font = pygame.font.Font('assets/fonts/KenneyMiniSquareMono.ttf', 12)
        self.prompt_text = text.MultilineText((self.screen_width//8)*3, ((self.screen_height//3)//8)*5, 320, 180, prompt_text_font, self.prompt, (30, 167, 225))
        self.bpanel_group_2 = pygame.sprite.Group(self.title, self.player, self.prompt_text)

    def displayBottomPanel(self):
        self.bottom_surface = pygame.Surface((self.screen_width, self.screen_height//3), pygame.SRCALPHA)
        self.bottom_surface.blit(self.bpanel_bg, (0, 0))
        self.bpanel_group.draw(self.bottom_surface)
        self.bpanel_group_2.draw(self.bottom_surface)
        self.screen.blit(self.bottom_surface, (0, (self.screen_height//3)*2))