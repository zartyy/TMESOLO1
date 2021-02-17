# coding: utf-8
from arene import Arene
from math import pi as PI
from tkinter import *
from time import *

class Fenetre:
	def __init__(self, arene):
		# Ajout de l'arene
		self.arene= arene

		# Vitesse du robot
		self.arene.robot.vitesse=2

		self.init_window=Tk()
		# fenêtre principale
		self.init_window.title("C'est bien parti pour le 100/100")
		self.init_window.geometry("900x750")
		self.init_window.config(background='#41B77F')

		#texte
		self.label_title = Label(self.init_window, text="Clique gauche sur une case pour placer ou retirer un objet, le robot est dans la case rouge", font = ("",14), bg='#41B77F', fg='white')
		self.label_title.pack(side=BOTTOM)

		# Création d'une Frame pour les attributs du Robot
		self.frame_attribut= LabelFrame(self.init_window, text= "Attributs du Robot", relief="sunken", labelanchor='n', bd=5)
		self.frame_attribut.pack()

		# Attribut
		self.label_pos= Label(self.frame_attribut, text="position [x : y] : "+str(self.arene.robot.pos))
		self.label_pos.pack()
		self.label_angle= Label(self.frame_attribut, text="angle: "+str((self.arene.robot.angle*180/PI)%360)+" degrés")
		self.label_angle.pack()
		self.label_vitesse= Label(self.frame_attribut, text="vitesse: "+str(self.arene.robot.vitesse*0.15*3.6)+" km/h")
		self.label_vitesse.pack()

		# Création d'une Frame pour le contrôle du robot
		self.frame_control= LabelFrame(self.init_window, text="Contrôle Robot",labelanchor='n' ,relief="sunken", bd=5)
		self.frame_control.pack(side=LEFT)

		#bouton de contrôle du Robot

		self.button_start = Button(self.frame_control, text="Démarrer", command= self.start)
		self.button_start.pack()

		self.button_avance = Button(self.frame_control, text="avance", command= self.avancerRobot)
		self.button_avance.pack()

		self.button_continue = Button(self.frame_control, text="avance en continue", command= self.avancerEnContinue)
		self.button_continue.pack()
		
		self.button_tourne= Button(self.frame_control, text="tourne à droite", command= self.tourneRobot)
		self.button_tourne.pack()
		
		self.button_tourne15= Button(self.frame_control, text="tourne de 15 degrés", command= self.tourneRobot15)
		self.button_tourne15.pack()
		
		self.button_tourne_15= Button(self.frame_control, text="tourne de -15 degrés", command= self.tourneRobot_15)
		self.button_tourne_15.pack()
		
		self.button_augmenteVitesse = Button(self.frame_control, text="augmenter la vitesse", command=self.augmenterVitesseRobot)
		self.button_augmenteVitesse.pack()
		
		self.button_diminueVitesse = Button(self.frame_control, text="diminuer la vitesse", command=self.diminuerVitesseRobot)
		self.button_diminueVitesse.pack()

		self.button_quit = Button(self.init_window, text="cliquer pour quitter", command=self.quit)
		self.button_quit.pack(side=RIGHT)
 
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
		
		
		# binding de la fonction modifierTableau sur le canevas
		self.can.bind("<Button-1>", self.modifierTableau)
		self.button_continue.bind('<ButtonPress-1>',self.avancerEnContinue(4))

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

		self.afficher()

	# Fait avancer le Robot dans l'Arene
	def avancerRobot(self):
		self.arene.avancerRobot()
		self.label_pos.configure(text="position: "+str(self.arene.robot.pos))
		self.afficher()
		print(self.arene.robot.pos)

	def augmenterVitesseRobot(self):
		self.arene.robot.changerVitesseSimple(1)
		self.label_vitesse.configure(text="vitesse: "+str(self.arene.robot.vitesse*0.15*3.6)+" km/h")
		
	def diminuerVitesseRobot(self):
		self.arene.robot.changerVitesseSimple(-1)
		self.label_vitesse.configure(text="vitesse: "+str(self.arene.robot.vitesse*0.15*3.6)+" km/h")

	def start(self):

		for i in range(0,3):
			sleep(1)
			self.avancerRobot()
			self.init_window.update_idletasks()

	def avancerEnContinue(self,vitesse_max=4):
		if(self.arene.robot.vitesse < vitesse_max):
			self.augmenterVitesseRobot()
			if(self.arene.robot.vitesse > vitesse_max):
				self.arene.robot.vitesse = vitesse_max
		self.avancerRobot()
	
	# Tourne le Robot de 90° à droite 
	def tourneRobot(self):
		self.arene.tourneRobot(PI/2)
		self.label_angle.configure(text="angle: "+str((self.arene.robot.angle*180/PI)%360))
	
	# Tourne le Robot de 15° à droite 
	def tourneRobot15(self):
		self.arene.tourneRobot(15*PI/180)
		self.label_angle.configure(text="angle: "+str((self.arene.robot.angle*180/PI)%360))
		
	# Tourne le Robot de 15° à gauche
	def tourneRobot_15(self):
		self.arene.tourneRobot(-15*PI/180)
		self.label_angle.configure(text="angle: "+str((self.arene.robot.angle*180/PI)%360))	

	def quit(self):
		self.init_window.destroy()
