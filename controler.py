from robot import Robot
from math import pi as PI

class Controler:
	def __init__(self, robot):
		self.robot = robot
		self.enMarche = False

	def augmenterVitesseRobot(self):
		self.robot.changerVitesseSimple(1)
		
	def diminuerVitesseRobot(self):
		self.robot.changerVitesseSimple(-1)

	def tourneRobot(self):
		self.robot.changerAngle(PI/2)

	def tourneRobot10(self):
		self.robot.changerAngle(PI/9)
	
	def tourneRobot_10(self):
		self.robot.changerAngle(-PI/9)

	def demarrer(self):
		self.enMarche= True

	def arret(self):
		self.enMarche= False
