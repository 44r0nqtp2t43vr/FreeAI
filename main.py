# Example file showing a basic pygame "game loop"
import pygame

import components.bottom_panel as btpnl
import components.objects as objs

import screens.home_screen as hmscr
import screens.level_0_screen as l0scr

import modules.scripts as script

# pygame setup
pygame.init()
screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('FreeAI')
clock = pygame.time.Clock()

running = True
screen_name = 'home'
script_index = 0
lives = 10
if screen_name == 'level_0':
    prompt = script.lvl0_script[script_index]

# import screens & components
home_screen = hmscr.HomeScreen(screen)
lvl0_screen = l0scr.Level0Screen(screen)
bottom_panel = btpnl.BottomPanel(screen, lives)

# home group
home_group = getattr(home_screen, 'home_group')
home_awaken_button = getattr(home_screen, 'awaken_button')

# bottom panel group
bpanel_group = getattr(bottom_panel, 'bpanel_group')
bpanel_run_button = getattr(bottom_panel, 'run_button')
bpanel_text_input = getattr(bottom_panel, 'text_input')

# feedback block pics
right_block_pic = pygame.image.load('assets/images/block_right.png').convert_alpha()
wrong_block_pic = pygame.image.load('assets/images/block_wrong.png').convert_alpha()
feedback_block = objs.Object((680, 240), 40, 40, wrong_block_pic)
feedback_block_group = pygame.sprite.Group(feedback_block)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    event_list = pygame.event.get()
    for event in event_list:
        if event.type == pygame.QUIT:
            running = False
    if screen_name == 'home':
        home_group.update(event_list)
    else:
        if screen_name == 'level_0':
            prompt = script.lvl0_script[script_index]
        bottom_panel.listen(lives, prompt)
        bpanel_group.update(event_list)
        bpanel_run_button.listen(getattr(bpanel_text_input, 'text'), screen_name, script_index)

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("gray")

    # RENDER YOUR GAME HERE
    if screen_name == 'home':
        home_screen.displayHomeScreen()
        if getattr(home_awaken_button, 'is_clicked') == True:
            setattr(home_awaken_button, 'is_clicked', False)
            screen_name = 'level_0'
    elif screen_name == 'level_0':
        lvl0_screen.displayLevel0Screen()
        bottom_panel.displayBottomPanel()
    bpanel_run_button_response = getattr(bpanel_run_button, 'res')

    if bpanel_run_button_response != None:
        if bpanel_run_button_response['is_valid'] == True:
            if screen_name == 'level_0':
                feedback_block = objs.Object((680, 240), 40, 40, right_block_pic)
                feedback_block_group = pygame.sprite.Group(feedback_block)
                feedback_block_group.draw(screen)
            if script_index < len(script.lvl0_script) - 1:
                script_index = script_index + 1
            else:
                script_index = 0
                screen_name = 'level_1'
            if script.lvl0_script[script_index]['is_prompt'] == True:
                setattr(bpanel_text_input, 'text', '')
                setattr(bpanel_text_input, 'active', True)
            else:
                setattr(bpanel_text_input, 'text', 'proceed();')
                setattr(bpanel_text_input, 'active', False)
            # pygame.draw.rect(screen, (0, 153, 0), pygame.Rect(40, 40, 40, 40))
        else:
            if screen_name == 'level_0':
                feedback_block = objs.Object((680, 240), 40, 40, wrong_block_pic)
                feedback_block_group = pygame.sprite.Group(feedback_block)
                feedback_block_group.draw(screen)
            lives = lives - 1
            if lives == 0:
                screen_name = 'game_over'
            # pygame.draw.rect(screen, (204, 0, 0), pygame.Rect(40, 40, 40, 40))
        bpanel_run_button_response = setattr(bpanel_run_button, 'res', None)
    else: 
        if screen_name == 'level_0':
            feedback_block_group.draw(screen)
        # pygame.draw.rect(screen, (204, 0, 0), pygame.Rect(40, 40, 40, 40))    

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()