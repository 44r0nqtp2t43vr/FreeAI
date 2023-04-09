# Example file showing a basic pygame "game loop"
import pygame
import modules.compiler as comp

import components.bottom_panel as btpnl

import screens.home_screen as hmscr
import screens.level_0_screen as l0scr

# pygame setup
pygame.init()
screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('FreeAI')
clock = pygame.time.Clock()
lives = 10
prompt = 'Initialize an integer variable without a value to start repairing the robot, using the syntax “int repairCode;”. Int defines the variable named repairCode as an integer, which is one of the available data types in C. This allows the variable to be used in the succeeding lines of code.'

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
    else:
        bottom_panel.listen(lives, prompt)
        bpanel_group.update(event_list)
        bpanel_run_button.listen_code(getattr(bpanel_text_input, 'text'))

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
            pygame.draw.rect(screen, (0, 153, 0), pygame.Rect(40, 40, 40, 40))
        else: 
            pygame.draw.rect(screen, (204, 0, 0), pygame.Rect(40, 40, 40, 40))    

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()