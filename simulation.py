from robot import Robot
from arene import Arene
from fenetre import Fenetre 
import time

begin = time.time()

#une instance de robot doit etre crée

a=Arene()
f= Fenetre(a)# ajouter le robot en paramètre
f.afficher()
f.init_window.mainloop()

end = time.time()

print("temps d'exécution : "+ str(end - begin)+"s")