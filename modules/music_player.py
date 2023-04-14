import pygame


def play_music(screen_name):
    if screen_name == 'level_0':
        pygame.mixer.music.stop()
        pygame.mixer.music.load('assets/music/joshua-mclean_down-the-river-we-go.wav')
        pygame.mixer.music.set_volume(0.3)
        pygame.mixer.music.play(-1)
    elif screen_name == 'level_1' or screen_name == 'level_2':
        pygame.mixer.music.stop()
        pygame.mixer.music.load('assets/music/joshua-mclean_brink.wav')
        pygame.mixer.music.set_volume(0.3)
        pygame.mixer.music.play(-1)
    elif screen_name == 'level_3':
        pygame.mixer.music.stop()
        pygame.mixer.music.load('assets/music/joshua-mclean_deitites-get-takeout-too.wav')
        pygame.mixer.music.set_volume(0.3)
        pygame.mixer.music.play(-1)
    elif screen_name == 'home':
        pygame.mixer.music.stop()
        pygame.mixer.music.load('assets/music/joshua-mclean_50s-bit.wav')
        pygame.mixer.music.set_volume(0.3)
        pygame.mixer.music.play(-1)
    elif screen_name == 'victory':
        pygame.mixer.music.stop()
        pygame.mixer.music.load('assets/music/joshua-mclean_celebrate.wav')
        pygame.mixer.music.set_volume(0.3)
        pygame.mixer.music.play(-1)
    elif screen_name == 'game_over':
        pygame.mixer.music.stop()
        pygame.mixer.music.load('assets/music/joshua-mclean_forest-of-the-king.wav')
        pygame.mixer.music.set_volume(0.3)
        pygame.mixer.music.play(-1)