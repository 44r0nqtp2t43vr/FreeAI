import pygame
import numpy as np
import components.objects as objs


def updatePos(old_psprite_pos, new_psprite_pos):
    if old_psprite_pos == new_psprite_pos:
        return old_psprite_pos
    if old_psprite_pos[0] == new_psprite_pos[0]:
        if old_psprite_pos[1] > new_psprite_pos[1]:
            return (old_psprite_pos[0], old_psprite_pos[1] - 20)
        else:
            return (old_psprite_pos[0], old_psprite_pos[1] + 20)
    else:
        if old_psprite_pos[0] > new_psprite_pos[0]:
            return (old_psprite_pos[0] - 20, old_psprite_pos[1])
        else:
            return (old_psprite_pos[0] + 20, old_psprite_pos[1])
        
def executeForLoop(response, old_pos, block_group, sprite_group):
    screen_width = 1280
    screen_height = 720

    tags_list = response['tags_list']
    tags = [tagged_word[1] for tagged_word in tags_list]
    number_indices = [index for index in range(len(tags_list)) if tags_list[index][1] == 'number']
    if '!' in tags:
        conditioner_index = tags.index('!')
    elif 'operator_glt' in tags:
        conditioner_index = tags.index('operator_glt')
    if tags_list[conditioner_index + 1][0] == '=':
        has_or_equal = True
    else:
        has_or_equal = False
    number_one = int(tags_list[number_indices[0]][0])
    number_two = int(tags_list[number_indices[1]][0])
    function_name = tags_list[tags.index('function_name')][0]

    if number_one < number_two:
        difference = number_two - number_one
    else:
        difference = number_one - number_two
    if has_or_equal:
        difference = difference + 1
    
    if function_name == 'goright':
        new_pos = (old_pos[0] + 40 * difference, old_pos[1])
        test_list = np.arange(old_pos[0] + 40, new_pos[0] + 40, 40).tolist()
    elif function_name == 'goleft':
        new_pos = (old_pos[0] - 40 * difference, old_pos[1])
        test_list = np.arange(new_pos[0], old_pos[0], 40).tolist()
    elif function_name == 'godown':
        new_pos = (old_pos[0], old_pos[1] + 40 * difference)
        test_list = np.arange(old_pos[1] + 40, new_pos[1] + 40, 40).tolist()
    elif function_name == 'goup':
        new_pos = (old_pos[0], old_pos[1] - 40 * difference)
        test_list = np.arange(new_pos[1], old_pos[1], 40).tolist()
    
    if (new_pos[0] < 0 or new_pos[0] > screen_width - 40) or (new_pos[1] < 0 or new_pos[1] > screen_height - 40):
        return old_pos
    
    test_pic = pygame.image.load('assets/images/sprite_freeai.png').convert_alpha()
    if function_name == 'goright' or function_name == 'goleft':
        for x in test_list:
            test_sprite = objs.Object((x, new_pos[1]), 40, 40, test_pic)
            if len(pygame.sprite.spritecollide(test_sprite, block_group, False)) > 0 or len(pygame.sprite.spritecollide(test_sprite, sprite_group, False)):
                return old_pos
    else:
        for y in test_list:
            test_sprite = objs.Object((new_pos[0], y), 40, 40, test_pic)
            if len(pygame.sprite.spritecollide(test_sprite, block_group, False)) > 0 or len(pygame.sprite.spritecollide(test_sprite, sprite_group, False)):
                return old_pos
    
    return new_pos