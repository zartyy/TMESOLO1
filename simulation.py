from robot import Robot
from arene import Arene
from fenetre import Fenetre 
import time

begin = time.time()

a=Arene()
f= Fenetre(a)
f.afficher()
# binding de la fonction modifierTableau sur le canevas
f.can.bind("<Button-1>", f.modifierTableau)
f.init_window.mainloop()

#la boucle ne marche pas encore
"""
i = 3
while(i > 0) :

    f.afficher()
    i = i - 1
    print("un tour")
    time.sleep(1)
"""

end = time.time()

print(f"temps d'exécution : {end - begin}s")
        
    


