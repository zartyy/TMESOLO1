class Arene:
	def __init__(self, longueur, largeur, robot):
		# On initialise une grille vide longueur x largeur
		self.grille= [[ 0 for n in range(longueur)] for i in range(largeur)]
		self.robot= robot

	def modifierTableau(self,evt):
		pos_x = int(evt.x / size)
    		pos_y = int(evt.y / size)
 
		# inverser la valeur de l'élément cliqué si c'est un obstacle ou une case vide
	   	# ne fait rien si on clique sur le robot
    		if tableau[pos_x][pos_y] == 2:
        		return
    		elif tableau[pos_x][pos_y] == 0:
        		tableau[pos_x][pos_y] = 1
    		else:
        		tableau[pos_x][pos_y] = 0
