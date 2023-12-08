

def posGagnante(lst):

    for i in range (len(lst)):
        valeur = 0
        cpt = 0
        for n in lst[i]:
            if n == 1 or n == 2:
                if valeur == 0 or valeur == n:
                    valeur = n
                    cpt +=1
                else:
                    valeur = 0
                    cpt = 0
                if cpt == 4:
                    print("victoire")
