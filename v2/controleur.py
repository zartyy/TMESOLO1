
class Controleur:

    def __init__(self, robot, arene):
        self.robot = robot
        self.arene = arene

    def changerVitesse(self, vitesse):
        self.robot.changerVitesse(vitesse*4.46)#conversion en tour/minute
    
    def setVitesse(self, vitesse):
        self.robot.ordonnerVitesse(vitesse*4.46)
    
    def tournerDroite(self):
        self.robot.changerDirection("droite")

    def tournerGauche(self):
        self.robot.changerDirection("gauche")
    
    def arreterTourner(self):
        self.robot.finChangementDirection()