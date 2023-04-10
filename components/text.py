import pygame

class Text(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, font, text, color):
        super().__init__()
        self.screen_width = 1280
        self.screen_height = 720
        self.pos = (x, y)
        self.width = width
        self.height = height
        self.font = font
        self.text = text
        self.color = color
        self.render_text()

    def render_text(self):
        text_surface = self.font.render(self.text, True, self.color)
        self.image = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        self.image.blit(text_surface, text_surface.get_rect(center=(self.width/2, self.height/2)))
        self.rect = self.image.get_rect(center = self.pos)
        # pygame.draw.rect(self.image, self.color, self.image.get_rect(), 2)

class MultilineText(Text):
    def __init__(self, x, y, width, height, font, text, color):
        super().__init__(x, y, width, height, font, text, color)

    def wrap_text(self, text):
        limit = 33
        count = 0
        wrapped_text = ''
        for word in text.split():
            count = count + len(word)
            if count < limit:
                if wrapped_text.strip() != '':
                    wrapped_text = wrapped_text + ' ' + word
                    count = count + 1
                else:
                    wrapped_text = word
            else:
                wrapped_text = wrapped_text + '\n' + word
                count = len(word)
        return wrapped_text

    
    def render_text(self):
        self.image = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        self.rect = self.image.get_rect(center = self.pos)
        if self.text == None or self.text.strip() == '':
            return
        self.text = self.wrap_text(self.text)
        rendered_text = []
        for i, line in enumerate(self.text.split('\n')):
            text_surface = self.font.render(line, True, self.color)
            text_rect = text_surface.get_rect()
            text_rect.topleft = (16, 8 + i * 16)
            rendered_text.append((text_surface, text_rect))
        for text_surface, text_rect in rendered_text:
            self.image.blit(text_surface, text_rect)
        # pygame.draw.rect(self.image, self.color, self.image.get_rect().inflate(-2, -2), 2)
    

