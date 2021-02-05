class Arene:
	def __init__(self, longueur, largeur, robot):
		# On initialise une grille vide longueur x largeur
		self.grille= [[ 0 for n in range(longueur)] for i in range(largeur)]
		self.robot= robot

