# Example file showing a basic pygame "game loop"
import pygame

import components.bottom_panel as btpnl
import components.objects as objs

import screens.home_screen as hmscr
import screens.level_0_screen as l0scr
import screens.level_1_screen as l1scr

import modules.scripts as script
import modules.executors as execute

# pygame setup
pygame.init()
screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('FreeAI')
clock = pygame.time.Clock()

running = True
screen_name = 'level_1'
script_index = 0
star_pos_index = 0
lives = 10
if screen_name == 'level_0':
    prompt = script.lvl0_script[script_index]
elif screen_name == 'level_1':
    prompt = script.lvl1_script[script_index]

# import screens & components
home_screen = hmscr.HomeScreen(screen)
lvl0_screen = l0scr.Level0Screen(screen)
lvl1_screen = l1scr.Level1Screen(screen)
bottom_panel = btpnl.BottomPanel(screen, lives)

# home group
home_group = getattr(home_screen, 'home_group')
home_awaken_button = getattr(home_screen, 'awaken_button')

# bottom panel group
bpanel_group = getattr(bottom_panel, 'bpanel_group')
bpanel_run_button = getattr(bottom_panel, 'run_button')
bpanel_text_input = getattr(bottom_panel, 'text_input')

# screen block groups
lvl1_block_group = getattr(lvl1_screen, 'block_group')

# screen sprite groups
lvl1_sprite_group = getattr(lvl1_screen, 'sprite_group')

# feedback block pics
right_block_pic = pygame.image.load('assets/images/block_right.png').convert_alpha()
wrong_block_pic = pygame.image.load('assets/images/block_wrong.png').convert_alpha()
if screen_name == 'home' or screen_name == 'level_0':
    feedback_block = objs.Object((680, 240), 40, 40, wrong_block_pic)
elif screen_name == 'level_1':
    feedback_block = objs.Object((0, 400), 40, 40, wrong_block_pic)
feedback_block_group = pygame.sprite.Group(feedback_block)

# player_sprite
player_sprite_pic = pygame.image.load('assets/images/sprite_freeai.png').convert_alpha()
if screen_name == 'home' or screen_name == 'level_1':
    player_sprite = objs.Object((0, 360), 40, 40, player_sprite_pic)
    player_sprite_group = pygame.sprite.Group(player_sprite)
    old_psprite_pos = getattr(player_sprite, 'pos')
    new_psprite_pos = getattr(player_sprite, 'pos')
    lvl1_star_pos_list = [(400, 240), (1040, 400), (1160, 40)]
    # star sprite
    star_pic = pygame.image.load('assets/images/star.png').convert_alpha()
    star = objs.Object(lvl1_star_pos_list[star_pos_index], 40, 40, star_pic)
    star_group = pygame.sprite.Group(star)

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
        elif screen_name == 'level_1':
            prompt = script.lvl1_script[script_index]
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
    elif screen_name == 'level_1':
        lvl1_screen.displayLevel1Screen()
        bottom_panel.displayBottomPanel()
        old_psprite_pos = execute.updatePos(old_psprite_pos, new_psprite_pos)
        player_sprite = objs.Object(old_psprite_pos, 40, 40, player_sprite_pic)
        player_sprite_group = pygame.sprite.Group(player_sprite)
        player_sprite_group.draw(screen)
        if len(pygame.sprite.spritecollide(player_sprite, star_group, False)) > 0:
            if star_pos_index < len(lvl1_star_pos_list) - 1:
                star_pos_index = star_pos_index + 1
            if script_index < len(script.lvl1_script) - 1:
                script_index = script_index + 1
                if script.lvl1_script[script_index]['is_prompt'] == True:
                    setattr(bpanel_text_input, 'text', '')
                    setattr(bpanel_text_input, 'active', True)
                else:
                    setattr(bpanel_text_input, 'text', 'proceed();')
                    setattr(bpanel_text_input, 'active', False)
        star = objs.Object(lvl1_star_pos_list[star_pos_index], 40, 40, star_pic)
        star_group = pygame.sprite.Group(star)
        star_group.draw(screen)
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
            elif screen_name == 'level_1':
                feedback_block = objs.Object((0, 400), 40, 40, right_block_pic)
                feedback_block_group = pygame.sprite.Group(feedback_block)
                feedback_block_group.draw(screen)
                if script_index < len(script.lvl1_script) - 1:
                    if script_index not in script.lvl1_withold:
                        if script_index == script.lvl1_to_validate[0]:
                            old_psprite_pos = getattr(player_sprite, 'pos')
                            new_psprite_pos = execute.executeForLoop(bpanel_run_button_response, old_psprite_pos, lvl1_block_group, lvl1_sprite_group)
                            if old_psprite_pos == new_psprite_pos:
                                lives = lives - 1
                        script_index = script_index + 1
                    elif script_index == script.lvl1_withold[0]:
                        old_psprite_pos = getattr(player_sprite, 'pos')
                        new_psprite_pos = execute.executeForLoop(bpanel_run_button_response, old_psprite_pos, lvl1_block_group, lvl1_sprite_group)
                        if old_psprite_pos == new_psprite_pos:
                            lives = lives - 1
                else:
                    script_index = 0
                    star_pos_index = 0
                    screen_name = 'level_2'
                if script.lvl1_script[script_index]['is_prompt'] == True:
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
            elif screen_name == 'level_1':
                feedback_block = objs.Object((0, 400), 40, 40, wrong_block_pic)
                feedback_block_group = pygame.sprite.Group(feedback_block)
                feedback_block_group.draw(screen)
            lives = lives - 1
            if lives == 0:
                screen_name = 'game_over'
            # pygame.draw.rect(screen, (204, 0, 0), pygame.Rect(40, 40, 40, 40))
        bpanel_run_button_response = setattr(bpanel_run_button, 'res', None)
    else: 
        # if screen_name == 'level_0':
        #     feedback_block_group.draw(screen)
        feedback_block_group.draw(screen)
        # pygame.draw.rect(screen, (204, 0, 0), pygame.Rect(40, 40, 40, 40))    

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()