from robot import Robot
from arene import Arene
from fenetre import Fenetre 
import time

begin = time.time()

a=Arene()
f= Fenetre(a)
f.afficher()
f.init_window.mainloop()

end = time.time()

print("temps d'exécution : "+ str(end - begin)+"s")
        
    


