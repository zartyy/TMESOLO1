from robot import Robot
import math
import time


class StrategyAvance:
	def __init__(self, robot):
		self.robot= robot
		self.distance=10
		self.distanceCourant=0
		self.appelTime= 0
	
	def run(self):
		d=self.robot.get_distance()
		if d<3 and d>=0:
			print("Trop près")
			self.robot.stop()
			return 1
		temps= time.time()- self.appelTime
		rayonRoue= self.robot.WHEEL_DIAMETER /2
		self.robot.set_motor_dps(3, 90)
		if self.appelTime!=0:
			self.distanceCourant+=(math.pi*min(self.robot.vitesse_roue[0], self.robot.vitesse_roue[1] *rayonRoue*temps))/(180.0)
		self.appelTime = time.time()
		return 0
	
	def start(self, distance):
		self.distanceCourant=0
		self.distance= distance
		self.appelTime=0


	def stop(self):
		if self.distanceCourant>= self.distance:
			self.robot.stop()
			return True
		return False


class StrategyTourneGauche:
	def __init__(self, robot):
		self.robot= robot
		self.angleCourant=0
		self.angle=90
		self.direction=0
		self.appelTime= 0
	def run(self):
		temps= time.time()- self.appelTime
		rayonRoue= self.robot.WHEEL_DIAMETER*0.5
		rayonRobot= self.robot.WHEEL_BASE_WIDTH
		vitesse_tourne= 100
		if (self.direction==0):
			self.robot.set_motor_dps(1, vitesse_tourne)
		else: self.robot.set_motor_dps(2, vitesse_tourne)
		# Calcule de l'angle du Robot
		if self.appelTime!=0:
			self.angleCourant+= (rayonRoue*vitesse_tourne*1.0*temps)/rayonRobot
		self.appelTime= time.time()
		self.stop()
		

	def start(self, direction):
		self.angleCourant=0
		self.direction=direction
		self.appelTime=0

	def stop(self):
		print(self.angleCourant)
		if self.angleCourant>= self.angle:
			self.robot.set_motor_dps(3, 0)
			return True
		return False

class StrategyTracerCarre:
	def __init__(self, robot):
		self.robot= robot
		self.s_avance= StrategyAvance(robot)
		self.s_turnLeft= StrategyTourneGauche(robot)
		self.tab= [self.s_avance, self.s_turnLeft, self.s_avance, self.s_turnLeft, self.s_avance, self.s_turnLeft, self.s_avance]
		self.action=0

	def run(self):
		if self.tab[self.action].stop():
			self.action+=1
			if self.stop(): return
			else:
				if self.action%2==0:
					self.tab[self.action].start(70)
				else: self.tab[self.action].start(0)
		if self.tab[self.action].run()==1: self.action+=1

	def start(self):
		self.action=0
		self.tab[self.action].start(70)

	def stop(self):
		return self.action>=len(self.tab)

