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

def gravite(lst):
    rows = len(lst)
    cols = len(lst[0])

    for j in range(cols):
        # Traverse each column from bottom to top
        for i in range(rows - 2, -1, -1):
            if lst[i][j] != 0:
                # Find the next available position in the column
                k = i + 1
                while k < rows and lst[k][j] == 0:
                    lst[k][j] = lst[k - 1][j]
                    lst[k - 1][j] = 0
                    k += 1

    return lst
