from time import sleep

class Robot:

    def __init__(self):
        self.vitesse_roue_gauche = 0.0
        self.vitesse_roue_droite = 0.0
        self.VITESSE_CHANGEMENT_DIRECTION = 50 #Vitesse ajoutée à une des roues pour faire tourner le robot
    
    def changerVitesse(self, tours_par_minute_roues):
        self.vitesse_roue_droite += tours_par_minute_roues
        self.vitesse_roue_gauche += tours_par_minute_roues
    
    def ordonnerVitesse(self, tours_par_minute_roues):
        self.vitesse_roue_droite = tours_par_minute_roues
        self.vitesse_roue_gauche = tours_par_minute_roues
    
    def changerDirection(self, direction):
        if (direction == "gauche"):
            self.vitesse_roue_droite += self.VITESSE_CHANGEMENT_DIRECTION
        elif (direction == "droite"):
            self.vitesse_roue_gauche += self.VITESSE_CHANGEMENT_DIRECTION
        else :
            print("Direction non valide, aucun changement pris en compte")

    def finChangementDirection(self):
        if (self.vitesse_roue_droite > self.vitesse_roue_gauche):
            self.vitesse_roue_droite = self.vitesse_roue_gauche
        elif (self.vitesse_roue_droite < self.vitesse_roue_gauche):  
            self.vitesse_roue_gauche = self.vitesse_roue_droite


robot = Robot()
"""print(robot.vitesse_roue_gauche)
    robot.changerVitesse(50)
    robot.changerVitesse(25)
    print(robot.vitesse_roue_gauche)
    robot.changerVitesse(-20)
    print(robot.vitesse_roue_gauche)
    robot.ordonnerVitesse(100)
    print(robot.vitesse_roue_gauche)
    print(robot.vitesse_roue_droite)"""

"""print(robot.vitesse_roue_gauche)
print(robot.vitesse_roue_droite)
robot.changerDirection("gauche")
print(robot.vitesse_roue_gauche)
print(robot.vitesse_roue_droite)
sleep(1)
robot.finChangementDirection()
print(robot.vitesse_roue_gauche)
print(robot.vitesse_roue_droite)
robot.changerDirection("droite")
print(robot.vitesse_roue_gauche)
print(robot.vitesse_roue_droite)
sleep(1)
robot.finChangementDirection()
print(robot.vitesse_roue_gauche)
print(robot.vitesse_roue_droite)"""
