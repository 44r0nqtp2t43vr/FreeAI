# Example file showing a basic pygame "game loop"
import pygame
import modules.compiler as comp

import components.bottom_panel as btpnl

import screens.home_screen as hmscr
import screens.level_0_screen as l0scr

def compile(code):
    if code.strip() == '':
        return False
    preprocess_list = [['\n', ' '], ['\t', ' '], ['=', ' = '], [';', ' ; '], ['(', ' ( '], [')', ' ) '], ['{', ' { '], ['}', ' } '], ['+', ' + '], 
                       ['-', ' - '], ['*', ' * '], ['/', ' / '], ['%', ' % '], ['>', ' > '], ['<', ' < '], ['!', ' ! '] , [':', ' : ']]
    for pair in preprocess_list:
        code = code.replace(pair[0], pair[1])
    parser = comp.EarleyParser(comp.lexicon_dict, comp.grammar_dict)
    print(code)
    is_syn_correct = parser.parse(code.strip())
    if is_syn_correct == False:
        return None
    response = {
        'is_syn_correct': is_syn_correct,
        'statement_type': getattr(parser, 'statement_type'),
        'tags_list': getattr(parser, 'tags_list'),
    }
    return response

class TextInputBox(pygame.sprite.Sprite):
    def __init__(self, x, y, w, h, font):
        super().__init__()
        self.color = (255, 255, 255)
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
            t_surf = self.font.render(line, True, self.color, self.backcolor)
            t_rect = t_surf.get_rect()
            t_rect.topleft = (4, 4 + i * (40 + 0))
            rendered_text.append((t_surf, t_rect))
        # t_surf = self.font.render(self.text, True, self.color, self.backcolor)
        self.image = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        if self.backcolor:
            self.image.fill(self.backcolor)
        for t_surf, t_rect in rendered_text:
            self.image.blit(t_surf, t_rect)
        # self.image.blit(t_surf, (5, 5))
        pygame.draw.rect(self.image, self.color, self.image.get_rect().inflate(-2, -2), 2)
        self.rect = self.image.get_rect(topleft = self.pos)

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

class Button(pygame.sprite.Sprite):
    def __init__(self, x, y, w, h, font, text):
        super().__init__()
        self.color = (255, 255, 255)
        self.backcolor = None
        self.pos = (x, y) 
        self.width = w
        self.height = h
        self.font = font
        self.text = text
        self.render_button()

    def render_button(self):
        t_surf = self.font.render(self.text, True, self.color, self.backcolor)
        self.image = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        if self.backcolor:
            self.image.fill(self.backcolor)
        self.image.blit(t_surf, t_surf.get_rect(center=(self.width/2, self.height/2)))
        pygame.draw.rect(self.image, self.color, self.image.get_rect().inflate(-2, -2), 2)
        self.rect = self.image.get_rect(topleft = self.pos)
    
    def update(self, event_list):
        for event in event_list:
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if self.rect.collidepoint(mouse_pos):
                    self.render_button()

class RunButton(Button):
    def __init__(self, x, y, w, h, font, text):
        super().__init__(x, y, w, h, font, text)
        self.res = False

    def listen_code(self, code):
        self.code = code

    def update(self, event_list):
        for event in event_list:
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if self.rect.collidepoint(mouse_pos):
                    self.res = compile(self.code)

# pygame setup
pygame.init()
screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('FreeAI')
clock = pygame.time.Clock()

# import screens & components
home_screen = hmscr.HomeScreen(screen)
lvl0_screen = l0scr.Level0Screen(screen)
bottom_panel = btpnl.BottomPanel(screen)

# home group
home_group = getattr(home_screen, 'home_group')
home_story_button = getattr(home_screen, 'story_button')

# panel button group
font = pygame.font.SysFont(None, 60)
run_button = RunButton(960, 480, 320, 240, font, "Run")
text_input_box = TextInputBox(0, 480, 960, 240, font)
panel_group = pygame.sprite.Group(text_input_box, run_button)

running = True
screen_name = 'level_0'

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    event_list = pygame.event.get()
    for event in event_list:
        if event.type == pygame.QUIT:
            running = False
    if screen_name == 'home':
        home_group.update(event_list)
    # panel_group.update(event_list)
    # run_button.listen_code(getattr(text_input_box, 'text'))

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("gray")

    # RENDER YOUR GAME HERE
    if screen_name == 'home':
        home_screen.displayHomeScreen()
        if getattr(home_story_button, 'is_clicked') == True:
            setattr(home_story_button, 'is_clicked', False)
            screen_name = 'level_0'
    elif screen_name == 'level_0':
        lvl0_screen.displayLevel0Screen()
        bottom_panel.displayBottomPanel()
    # panel_group.draw(screen)
    # run_button_response = getattr(run_button, 'res')
    # if run_button_response and run_button_response['is_syn_correct'] == True:
    #     pygame.draw.rect(screen, (0, 153, 0), pygame.Rect(30, 30, 60, 60))
    # else: 
    #     pygame.draw.rect(screen, (204, 0, 0), pygame.Rect(30, 30, 60, 60))

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()