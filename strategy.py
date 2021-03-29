from robot import Robot
import math
import time


class StrategyAvance:
	def __init__(self, robot):
		self.robot= robot
		self.distance=10
		self.distanceCourant=0
		self.appelTime= 0
	def run(self, fps):
		temps= time.clock()- self.appelTime
		rayonRoue= self.robot.WHEEL_DIAMETER /2
		self.robot.set_motor_dps("MOTOR_LEFT", 90)
		self.robot.set_motor_dps("MOTOR_RIGHT", 90)
		if self.appelTime!=0:
			self.distanceCourant+=(math.pi*min(self.robot.get_motor_position[0], self.robot.get_motor_position[0] *rayonRoue*temps)/(180.0)
		self.appelTime= time.time()
	def start(distance):
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
	def run(self, fps):
		temps= time.clock()- self.appelTime
		rayonRoue= self.robot.WHEEL_DIAMETER /2
		rayonRobot= self.robot.WHEEL_BASE_WIDTH
		vitesse_tourne= 10
		if (self.direction==0):
			self.robot.set_motor_dps(vitesse_tourne, "RIGHT")
		else: self.robot.set_motor_dps(vitesse_tourne, "LEFT")
		# Calcule de l'angle du Robot
		if self.appelTime!=0:
			self.angleCourant+= (rayonRoue*vitesse_tourne*1.0*temps)/rayonRobot
		self.appelTime= time.clock()
		self.stop()

	def start(self, direction):
		self.angleCourant=0
		self.direction=direction
		self.appelTime=0

	def stop(self):
		print(self.angleCourant)
		if self.angleCourant>= self.angle:
			self.robot.set_motor_dps(0, "RIGHT")
			return True
		return False

class StategyTracerCarre:
	def __init__(self, robot):
		self.robot= robot
		self.s_avance= StrategyAvance(robot)
		self.s_turnLeft= StrategyTourneGauche(robot)
		self.tab= [s_avance, s_turnLeft, s_avance, s_turnLeft,s_avance, s_turnLeft, s_avance]
		self.action=0

	def run(self, fps):
		if self.tab[self.action].stop():
			self.action+=1
			if self.stop(): return
			else: self.tab[self.action].start()
		self.tab[self.action].run()

	def start(self):
		self.action=0
		self.tab[self.action].start()

	def stop(self):
		return self.action>=len(self.tab)

