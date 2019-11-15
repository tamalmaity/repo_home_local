import pygame
from grid import Grid
import os


os.environ['SDL_VIDEO_WINDOW_POS'] = '250,150'

win = pygame.display.set_mode((300,300))

pygame.display.set_caption('Tic-tac-toe')

run = True

player = "X"

obj_g = Grid()

while run:
    for event in pygame.event.get():
        if (event.type == pygame.QUIT):
            run = False

        if (event.type == pygame.MOUSEBUTTONDOWN) and (not obj_g.game_over):
            if (pygame.mouse.get_pressed()[0]):           #returns a tuple like (1,0,0) for left click
                x,y = pygame.mouse.get_pos()
                x = x//100        #integer division to get cell coordinates
                y = y//100
                obj_g.get_mouse(x,y,player)

                if obj_g.valid_move == True:
                    if (player == "X"):
                        player = "O"
                    elif (player == "O"):
                        player = "X"

        if (event.type == pygame.KEYDOWN):
            if (event.key == pygame.K_SPACE and obj_g.game_over):
                obj_g.clear_grid()
                obj_g.game_over = False


            elif (event.key == pygame.K_ESCAPE):
                run = False

            #obj_g.grid_print()





    win.fill((244,232,104))

    obj_g.draw(win) # Noob error. Don't put this line above fill for obvious reasons

    pygame.display.flip()   # like display update but for entire surface at a time

    if obj_g.message == True:
        obj_g.message_show(obj_g.message_index, 'X' if player=='O' else 'O')



