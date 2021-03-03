from robot2 import Robot
from affichageGraphique import Arene, Fenetre
from controleur import Controleur

class Simulation:

    def __init__(self, robot, arene, controleur, fenetre, dep_robot_x, dep_robot_y):
        self.arene = arene
        self.robot = robot
        self.controleur = controleur
        self.fenetre = fenetre
        self.arene.placerRobot(dep_robot_x, dep_robot_y)

robot = Robot
arene = Arene(30, 25, robot)
fenetre = Fenetre(arene)
controleur = Controleur(robot, arene)
simulation = Simulation(robot, arene, controleur, fenetre, 15, 12)


fenetre.afficher()
fenetre.init_window.mainloop()
