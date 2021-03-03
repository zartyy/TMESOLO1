from robot2 import Robot
from affichageGraphique import Arene, Fenetre
from controleur import Controleur

arene = Arene(30, 25)
fenetre = Fenetre(arene)
fenetre.afficher()
fenetre.init_window.mainloop()