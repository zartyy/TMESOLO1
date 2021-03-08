from robot import Robot
from arene import Arene
from fenetre import Fenetre
from threading import Thread
from controler import Controler

fps=80

# programme
a=Arene()
c= Controler(a.robot)
f= Fenetre(a, c)
f.afficher()

threadf= Thread(target=f.boucle, args=(fps,))
threadf.start()

# boucle principale
f.init_window.mainloop()
