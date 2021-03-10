from robot import Robot
from arene import Arene
from fenetre import Fenetre
from controler import Controler
from threading import Thread
import time

fps=20
# programme
r= Robot([],"Robot")
c= Controler(r)
a=Arene(c,r)
f= Fenetre(a, c)

threadf= Thread(target=f.boucle, args=(fps,))
threada= Thread(target=a.boucle, args=(fps,))
threadf.start()
threada.start()


# boucle principale
f.init_window.mainloop()

end = time.time()
print("temps d'exécution : "+ str(end - begin)+"s")
