from tkinter import *
from robot import *
from math import pi as PI
TAILLE_ARENE_X = 25
TAILLE_ARENE_Y = 25
class Arene:
	def __init__(self,matrice_x=TAILLE_ARENE_X,matrice_y=TAILLE_ARENE_Y):
		# matrice à deux dimensions
		self.tableau = []
		for i in range(matrice_x):
		    self.tableau.append([0] * matrice_y)
		
		# Ajout du Robot dans l'Arène
		self.robot= Robot(self.tableau, "robot")
		self.robot.pos = {'x':10, 'y':10}
		pos= self.robot.pos
		self.tableau[int(pos['x'])][int(pos['y'])]=2 #conversion des floats en entier
	
	def avancerRobot(self):
		x= self.robot.pos['x']
		y= self.robot.pos['y']
		self.tableau[int(x)][int(y)]=0 #conversion des floats en entier
		self.robot.changerVitesse(60)
		self.robot.seDeplacer(1,0)
		newpos= self.robot.pos
		if (newpos['x']<0 or newpos['x']>=TAILLE_ARENE_X or newpos['y']<0 or newpos['y']>=TAILLE_ARENE_Y):
			self.robot.pos= {'x': x, 'y': y}
		pos= self.robot.pos
		self.tableau[int(pos['x'])][int(pos['y'])]=2 #conversion des floats en entier
		
	def tourneRobot(self):
		self.robot.changerAngle(PI/2)


