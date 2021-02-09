from robot import *
from arene import *

# programme
a=Arene()
a.afficher(a.tableau)
# binding de la fonction modifierTableau sur le canevas
a.can.bind("<Button-1>", a.modifierTableau)
# boucle principale
a.init_window.mainloop()
