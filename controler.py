# coding: utf-8
from robot import Robot
from math import pi as PI
import time
from strategy import StrategyTourneGauche, StrategyAvance, StrategyTracerCarre

class Controler(object):
	def __init__(self, robot):
		self.exit=False
		self.robot= robot
		self.enMarche= False
		self.tab=[0 for i in range(7)]
		self.actionCourant=-1
		self.s_turnLeft= StrategyTourneGauche(self.robot)
		self.s_forward= StrategyAvance(self.robot)
		self.s_carre= StrategyTracerCarre(self.robot)

	def boucle(self,fps):
		while True:
			if self.exit:
				break
			self.update(fps)
			time.sleep(1./fps)

	def update(self, fps):
		action=-1
		for i in range(len(self.tab)):
			if self.tab[i]==1:
				action=i
				break
		if action==-1:
			return
		print(self.tab)
		# s'arrêter
		if action==0:
			self.robot.stop()
			self.tab[action]=0
		# Avancer
		elif action==1:
			if not self.s_forward.stop():
				self.s_forward.run()
			else: self.tab[action]=0
		# tracer un carre
		elif action==4:
			if not self.s_carre.stop():
				self.s_carre.run()
			else: self.tab[action]=0
		# Tourner
		elif action==5:
			if not self.s_turnLeft.stop():
				self.s_turnLeft.run()
			else: self.tab[action]=0

	def signal(self, intention):
		print("Signal recu: "+ intention)
		indice=-1
		if intention=="arret":
			indice=0
		elif intention=="avancer":
			indice=1
			self.s_forward.start(50)
		elif intention=="tracerCarre":
			indice=4
			self.s_carre.start()
		elif intention=="tournerGauche":
			indice=5
			self.s_turnLeft.start(0)
		elif intention=="tournerDroite":
			indice=5
			self.s_turnLeft.start(1)

		if indice==-1:
			print("Controler: Erreur indice=-1")
		elif self.tab[indice]==0:
			self.tab[indice]=1
