import pygame
import components.buttons as btns
import components.objects as objs

class Level0Screen():
    def __init__(self, screen):
        self.screen = screen
        self.screen_width = 1280
        self.screen_height = 720

        # import images
        self.lvl0_bg = pygame.image.load('assets/images/bg_lvl0.jpg').convert()
        free_sprite_pic = pygame.image.load('assets/images/sprite_free.png').convert_alpha()
        ai_sprite_pic = pygame.image.load('assets/images/sprite_ai.png').convert_alpha()
        metal_block_pic = pygame.image.load('assets/images/block_metal.png').convert()
        # self.lvl0_bg = pygame.transform.scale(self.lvl0_bg, (self.screen_width, (self.screen_height//3)*2))

        # import texts
        # title_font = pygame.font.Font('assets/fonts/KenneyRocketSquare.ttf', 72)
        # self.title_text = title_font.render('FreeAI', True, (255, 255, 255))
        # self.title_textRect = self.title_text.get_rect(center=(self.screen_width//2, self.screen_height//4 + 40))

        # define blocks positions and types
        block_defs = [[560, 200, 0], [680, 200, 1], [560, 240, 2], [600, 240, 2], [640, 240, 2]]

        # import components
        blocks = []
        for block_def in block_defs:
            if block_def[2] == 0:
                block = objs.Object((block_def[0], block_def[1]), 40, 40, free_sprite_pic)
            elif block_def[2] == 1:
                block = objs.Object((block_def[0], block_def[1]), 40, 40, ai_sprite_pic)
            elif block_def[2] == 2:
                block = objs.Object((block_def[0], block_def[1]), 40, 40, metal_block_pic)
            blocks.append(block)
        # story_button_font = pygame.font.Font('assets/fonts/KenneyHighSquare.ttf', 60)
        # self.story_button = btns.HomeButton(self.screen_width//2, (self.screen_height//4)*3 - 40, 200, 60, story_button_font, "Story", (255, 255, 255))

        # initialize sprite group
        self.block_group = pygame.sprite.Group(blocks)
        # self.home_group = pygame.sprite.Group(self.story_button)
    
    def displayLevel0Screen(self):
        self.top_surface = pygame.Surface((self.screen_width, (self.screen_height//3)*2), pygame.SRCALPHA)
        self.top_surface.blit(self.lvl0_bg, (0, 0))
        self.screen.blit(self.top_surface, (0, 0))
        self.block_group.draw(self.screen)
        # self.screen.blit(self.title_text, self.title_textRect)
        # self.home_group.draw(self.screen)