# coding: utf-8
from tkinter import *
from robot import *
from math import pi as PI

class Arene:
	def __init__(self,matrice_x=25,matrice_y=25):
		# matrice à deux dimensions
		self.tableau = []
		for i in range(matrice_x):
		    self.tableau.append([0] * matrice_y)
		
		# Ajout du Robot dans l'Arène
		self.robot= Robot(self.tableau, "robot")
		self.robot.pos = [10.0,10.0]
		pos= self.robot.pos
		self.tableau[int(pos[0])][int(pos[1])]=2 #conversion des floats en entier
	
	def avancerRobot(self):
		x= self.robot.pos[0]
		y= self.robot.pos[1]
		self.tableau[int(x)][int(y)]=0 #conversion des floats en entier
		self.robot.seDeplacer(1,0)
		newpos= self.robot.pos
		if (newpos[0]<0 or newpos[0]>=25 or newpos[1]<0 or newpos[1]>=25):
			self.robot.pos= [x,y]
		pos= self.robot.pos
		if self.tableau[int(pos[0])][int(pos[1])]==1:
			print("Le robot est sur la même case qu'un obstacle")
		self.tableau[int(pos[0])][int(pos[1])]=2 #conversion des floats en entier

	def tourneRobot(self,angle):
		self.robot.changerAngle(angle)