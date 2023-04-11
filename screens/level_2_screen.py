import pygame
import components.objects as objs

class Level2Screen():
    def __init__(self, screen):
        self.screen = screen
        self.screen_width = 1280
        self.screen_height = 720

        # import images
        self.lvl0_bg = pygame.image.load('assets/images/bg_lvl0.jpg').convert()
        enemy_sprite_pic = pygame.image.load('assets/images/sprite_enemy.png').convert_alpha()
        anomaly_sprite_pic = pygame.image.load('assets/images/sprite_ai.png').convert_alpha()
        metal_block_pic = pygame.image.load('assets/images/block_metal_2.png').convert()
        stone_block_pic = pygame.image.load('assets/images/block_stone.png').convert()

        # define blocks positions and types
        obj_defs = [
            (40, 400, 1), (80, 400, 1), (120, 400, 1), (160, 400, 1), (200, 400, 1),
            (240, 400, 1), (280, 400, 1), (320, 400, 1), (360, 400, 1), (400, 400, 1), (440, 400, 1),
            (200, 360, 1), (200, 320, 1), (200, 280, 1), (200, 240, 1), (200, 200, 1), (200, 160, 1),
            (320, 280, 1), (360, 280, 1), (400, 280, 1), (440, 280, 1), (480, 280, 1), (520, 280, 1),
            (560, 280, 1), (560, 320, 1), (560, 360, 1), (560, 400, 1), (560, 440, 1),
            (240, 160, 1), (280, 160, 1), (320, 160, 1), (360, 160, 1),
            (440, 200, 1), (440, 160, 1), (440, 120, 1), (440, 80, 1), (480, 80, 1), (480, 40, 1),
            (520, 40, 1), (560, 40, 1), (600, 40, 1), (640, 40, 1), (680, 40, 1), (720, 40, 1), (760, 40, 1), (720, 0, 1),
            (720, 80, 1), (720, 120, 1), (720, 160, 1), (720, 200, 1), (720, 240, 1), (760, 240, 1), (760, 280, 1), (800, 280, 1), (800, 320, 1),
            (480, 200, 1), (520, 200, 1), (560, 200, 1), (600, 200, 1), (640, 200, 1), (600, 280, 1),
            (600, 440, 1), (640, 440, 1), (680, 400, 1), (680, 440, 1), (720, 440, 1), (760, 440, 1), (800, 440, 1), (840, 440, 1), (880, 440, 1),
            (920, 440, 1), (960, 440, 1), (1000, 440, 1), (1040, 440, 1), (1080, 440, 1), (1080, 400, 1), (1120, 400, 1), (1120, 360, 1), (1160, 360, 1), (1160, 320, 1), (1200, 320, 1),
            (840, 320, 1), (880, 320, 1), (920, 320, 1), (960, 320, 1),
            (960, 280, 1), (960, 240, 1), (960, 200, 1), (960, 160, 1), (960, 120, 1),
            (920, 120, 1), (880, 120, 1), (840, 120, 1), (800, 120, 1),
            (1240, 0, 1), (1240, 40, 1), (1240, 80, 1), (1240, 120, 1), 
            (1240, 160, 1), (1240, 200, 1), (1240, 240, 1), (1240, 280, 1), (1240, 320, 1),
            (1200, 0, 1), (1160, 0, 1), (1120, 0, 1), (1080, 0, 1), (1040, 0, 1),
            (1160, 80, 1), (1200, 80, 1), (1000, 120, 1),
            (120, 0, 1), (120, 40, 1), (160, 40, 1), (160, 80, 1), (200, 80, 1),
            (240, 80, 1), (280, 80, 1), (320, 80, 1), (360, 80, 1),
            (200, 40, 3), (440, 360, 3), (1080, 360, 3), (1160, 280, 3), (1200, 280, 3),

            (480, 160, 0), (520, 160, 0), (1200, 40, 0),
        ]

        # import components
        blocks = []
        sprites = []
        for obj_def in obj_defs:
            if obj_def[2] == 0:
                sprite = objs.Object((obj_def[0], obj_def[1]), 40, 40, enemy_sprite_pic)
                sprites.append(sprite)
            elif obj_def[2] == 1:
                block = objs.Object((obj_def[0], obj_def[1]), 40, 40, metal_block_pic)
                blocks.append(block)
            elif obj_def[2] == 2:
                block = objs.Object((obj_def[0], obj_def[1]), 40, 40, stone_block_pic)
                blocks.append(block)
            elif obj_def[2] == 3:
                sprite = objs.Object((obj_def[0], obj_def[1]), 40, 40, anomaly_sprite_pic)
                sprites.append(sprite)

        # initialize sprite group
        self.block_group = pygame.sprite.Group(blocks)
        self.sprite_group = pygame.sprite.Group(sprites)
    
    def displayLevel2Screen(self):
        self.top_surface = pygame.Surface((self.screen_width, (self.screen_height//3)*2), pygame.SRCALPHA)
        self.top_surface.blit(self.lvl0_bg, (0, 0))
        self.screen.blit(self.top_surface, (0, 0))
        self.block_group.draw(self.screen)
        self.sprite_group.draw(self.screen)