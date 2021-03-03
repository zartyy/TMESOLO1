from robot2 import Robot
from affichageGraphique import Arene, Fenetre
from controleur import Controleur

robot = Robot
arene = Arene(30, 25)
fenetre = Fenetre(arene)
controleur = Controleur(robot, arene)

arene.placerRobot(15,12)

fenetre.afficher()
fenetre.init_window.mainloop()
