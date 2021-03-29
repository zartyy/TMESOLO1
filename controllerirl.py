from robot import Robot
from Robot2I013 import *
from gopigo import *
from math import pi as PI
import time

class Controler:
	def __init__(self, couleurLed, fps):
		self.robot = Robot2I013()
        #self.couleurLed = couleurLed
        self.fps = fps
        
        def arret(self):
            self.robot.stop()

        def avance_droit(self, vitesse):
            self.robot.set_motor_dps("MOTOR_LEFT", vitesse)
            self.robot.set_motor_dps("MOTOR_RIGHT", vitesse)

        def avance_pas_droit(self, vitesseGauche, vitesseDroite):
            self.robot.set_motor_dps("MOTOR_LEFT", vitesseGauche)
            self.robot.set_motor_dps("MOTOR_RIGHT", vitesseDroite)

        def execute_action(self, strategy):
                strategy.run()

            
