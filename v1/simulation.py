from robot import Robot
from arene import Arene
from fenetre import Fenetre
from controler import Controler
import time

begin = time.time()

#une instance de robot doit etre crée

a=Arene()
c= Controler(a.robot)
f= Fenetre(a)# ajouter le robot en paramètre
f.afficher()
threadf= Thread(target=f.boucle, args=(fps,))
threadf.start()
f.init_window.mainloop()

end = time.time()

print("temps d'exécution : "+ str(end - begin)+"s")
