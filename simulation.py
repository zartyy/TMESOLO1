from robot import Robot
from arene import Arene
from fenetre import Fenetre
from controler import Controler
from threading import Thread
import time

fps=80

begin = time.time()
# programme
a=Arene()
c= Controler(a.robot)
f= Fenetre(a,c)
f.afficher()

threadf= Thread(target=f.boucle, args=(fps,))
threadf.start()

# boucle principale
f.init_window.mainloop()

end = time.time()
print("temps d'exécution : "+ str(end - begin)+"s")
