import pygame

couleur = True
def dessiner(screen, lst):
    x = 250
    y = 150
    for i in range(len(lst)):
        for n in range(len(lst[i])):
            if lst[i][n] == 1:
                circle = pygame.draw.circle(screen, (0, 115, 252), (x, y), 50)
            if lst[i][n] == 2:
                circle = pygame.draw.circle(screen, (252, 45, 0), (x, y), 50)
            else:
                circle = pygame.draw.circle(screen, (0, 0, 0), (x, y), 50, 2)
            x += 115
        y += 115
        x = 250

def remplirCoord(lst):
    lstCoord = []
    x = 250
    y = 150
    for i in range(len(lst)):
        lstCoord.append([])
        for n in range(len(lst[i])):
            lstCoord[i].append((x, y))
            x += 115
        y += 115
        x = 250

    return lstCoord