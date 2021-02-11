# coding: utf-8
from arene import Arene
from math import pi as PI
from tkinter import *

class Fenetre:
	def __init__(self, arene):
		# Ajout de l'arene
		self.arene= arene

		# Vitesse du robot
		self.arene.robot.vitesse=2

		self.init_window=Tk()
		# fenêtre principale
		self.init_window.title("C'est bien parti pour le 100/100")
		self.init_window.geometry("900x575")
		self.init_window.config(background='#41B77F')

		#texte
		self.label_title = Label(self.init_window, text="Clique gauche sur une case pour placer ou retirer un objet, le robot est dans la case rouge", font = ("",14), bg='#41B77F', fg='white')
		self.label_title.pack(side=BOTTOM)
		
		# Création d'une Frame pour le contrôle du robot
		self.frame_control= Frame(self.init_window, relief="sunken", bd=5)
		self.frame_control.pack(side=LEFT)
		self.label_frame= Label(self.frame_control, text="Contrôle Robot")
		self.label_frame.pack(side=TOP)
		#bouton
		self.button_haut = Button(self.frame_control, text="avance", command= self.avancerRobot)
		self.button_haut.pack(side=TOP) 
		self.button_tourne= Button(self.frame_control, text="tourne à droite", command= self.arene.tourneRobot)
		self.button_tourne.pack(side=LEFT)
 
		# les 2 couleurs à utiliser
		self.couleurs = {0: "white", 1: "#41B77F", 2: "red"}

		# dimensions du canevas
		self.can_width = 620
		self.can_height = 620

		# taille d'une case
		self.size = 25

		# création canevas
		self.can = Canvas(self.init_window, width=self.can_width, height=self.can_height)
		self.can.pack()

	def afficher(self):
		"""
		Fonction d'affichage du tableau ; 1 élément = 1 case
		La couleur de la "case" dépend de l'état de l'élement correspondant, 0 ou 1
		"""
		for i in range(len(self.arene.tableau)):
			for j in range(len(self.arene.tableau[i])):
				self.can.create_rectangle(i * self.size, j * self.size , i * self.size + self.size, j * self.size + self.size, fill = self.couleurs[self.arene.tableau[i][j]])

	def modifierTableau(self,evt):
		pos_x = int(evt.x / self.size)
		pos_y = int(evt.y / self.size)
		# inverser la valeur de l'élément cliqué si c'est un obstacle ou une case vide
	   	# ne fait rien si on clique sur le robot
		if self.arene.tableau[pos_x][pos_y] == 2:
			self.arene.tableau[pos_x][pos_y] = 2
		elif self.arene.tableau[pos_x][pos_y] == 0:
			self.arene.tableau[pos_x][pos_y] = 1
		else:
			self.arene.tableau[pos_x][pos_y] = 0

		self.afficher(self.arene.tableau)

	def avancerRobot(self):
		self.arene.avancerRobot()
		self.afficher()
		print(self.arene.robot.pos)

