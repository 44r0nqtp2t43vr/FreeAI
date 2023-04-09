import pygame

class TextInput(pygame.sprite.Sprite):
    def __init__(self, x, y, w, h, font, color):
        super().__init__()
        self.screen_width = 1280
        self.screen_height = 720
        self.color = color
        self.backcolor = None
        self.pos = (x, y) 
        self.width = w
        self.height = h
        self.font = font
        self.active = False
        self.text = ""
        self.render_text()

    def render_text(self):
        rendered_text = []
        for i, line in enumerate(self.text.split('\n')):
            line = line.replace('\t', '     ')
            text_surface = self.font.render(line, True, self.color, self.backcolor)
            text_rect = text_surface.get_rect()
            text_rect.topleft = (4, 4 + i * 40)
            rendered_text.append((text_surface, text_rect))
        self.image = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        if self.backcolor:
            self.image.fill(self.backcolor)
        for text_surface, text_rect in rendered_text:
            self.image.blit(text_surface, text_rect)
        # pygame.draw.rect(self.image, self.color, self.image.get_rect().inflate(-2, -2), 2)
        self.rect = self.image.get_rect(center = self.pos)

    def update(self, event_list):
        for event in event_list:
            # if event.type == pygame.MOUSEBUTTONDOWN and not self.active:
            #     self.active = self.rect.collidepoint(event.pos)
            self.active = True
            if event.type == pygame.KEYDOWN and self.active:
                if event.key == pygame.K_RETURN:
                    # self.active = False
                    self.text += '\n'
                elif event.key == pygame.K_TAB:
                    self.text += '\t'
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                self.render_text()