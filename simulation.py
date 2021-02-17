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
f.button_continue.bind('<ButtonPress-1>',f.avancerEnContinue(4))

f.init_window.mainloop()

end = time.time()

print("temps d'exécution : "+ str(end - begin)+"s")
        
    


