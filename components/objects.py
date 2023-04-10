import pygame

class Object(pygame.sprite.Sprite):
    def __init__(self, pos, width, height, pic):
        super().__init__()
        self.pos = pos
        self.width = width
        self.height = height
        self.pic = pygame.transform.scale(pic, (width, height))
        self.render_object()

    def render_object(self):
        self.image = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        self.image.blit(self.pic, (0, 0))
        self.rect = self.image.get_rect(topleft = self.pos)
        # pygame.draw.rect(self.image, (255, 255, 255), self.image.get_rect(), 2)
