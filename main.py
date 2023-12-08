import pygame
import sys
import dessin
import Victoire

pygame.init()

window_size = (1200, 900)

screen = pygame.display.set_mode(window_size)
pygame.display.set_caption("Pygame Window")
background_color = (255, 255, 255)

plateau = [[0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0]]

lstPos = dessin.remplirCoord(plateau)
Victoire.posGagnante(plateau)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                for i in range(len(lstPos)):
                    for n in range(len(lstPos[i])):
                        if lstPos[i][n][0]-50 <= mouse_x <= lstPos[i][n][0]+50:
                            if lstPos[i][n][1] - 50 <= mouse_y <= lstPos[i][n][1] + 50:
                                if plateau[i][n] == 0:
                                    if dessin.couleur:
                                        plateau[i][n] = 1
                                    else:
                                        plateau[i][n] = 2
                                    dessin.couleur = not dessin.couleur
                                    plateau = dessin.gravite(plateau)
                                    Victoire.posGagnante(plateau)

    screen.fill(background_color)
    dessin.dessiner(screen, plateau)
    pygame.display.flip()

