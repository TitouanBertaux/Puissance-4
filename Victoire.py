

def posGagnante(lst):

	#pour chaque ligne de la liste 
	for i in range (len(lst)):
		valeur = 0
		cpt = 0
		#pour chaque valeur de la ligne
		for n in lst[i]:
			if n == 1 or n == 2:
				if valeur == 0 or valeur == n:
					valeur = n
					cpt +=1
				else:
					valeur = 0
					cpt = 0
				if cpt == 4:
					if n == 1:
						print("victoire jaune")
					else:
						print("victoire rouge")
					return True
	#pour chaque colonne de la liste
	for i in range (len(lst[0])):
		valeur = 0
		cpt = 0
		for n in range (len(lst)):
			if lst[n][i] == 1 or lst[n][i] == 2:
				if valeur == 0 or valeur == lst[n][i]:
					valeur = lst[n][i]
					cpt +=1
				else:
					valeur = 0
					cpt = 0
				if cpt == 4:
					if n == 1:
						print("victoire jaune")
					else:
						print("victoire rouge")
						return True
	# pour chaque diagonale de la liste
	for i in range(len(lst)):
		for n in range(len(lst[i])):
			if lst[i][n] == 1 or lst[i][n] == 2:
				if n < 4 and i < len(lst) - 3:
					if lst[i][n] == lst[i+1][n+1] and lst[i][n] == lst[i+2][n+2] and lst[i][n] == lst[i+3][n+3]:
						if lst[i][n] == 1:
							print("victoire jaune")
						else:
							print("victoire rouge")
						return True
				if n > 2 and i < len(lst) - 3:
					if lst[i][n] == lst[i+1][n-1] and lst[i][n] == lst[i+2][n-2] and lst[i][n] == lst[i+3][n-3]:
						if lst[i][n] == 1:
							print("victoire jaune")
						else:
							print("victoire rouge")
						return True
