from tkinter import *

class Arene:

    def  __init__(self, x, y):
        self.x = x
        self.y = y
        self.matrice = []
        for i in range(self.x):
            self.matrice.append([0] * self.y)
            
    def changementEtat(self, entier, x, y):
        self.matrice[x][y] = entier
        
"""arene = Arene(10,15)
    print(arene.x)
    print(arene.y)
    print(arene.matrice[0][2])
    arene.matrice[0][2] = 5 
    print(arene.matrice[0][2])
    arene.changementEtat(10, 0, 2)
    print(arene.matrice[0][2])"""


class Fenetre:

    def __init__(self, arene):
        self.arene = arene
        self.couleurs = {0: "white", 1: "#84E5EE", 2: "red"}#0 : rien dans la case, 1: obstacle dans la case, 2:robot dans la case

        self.init_window=Tk()
        self.init_window.title("Projet Robotique - affichage graphique")
        self.init_window.geometry("800x500")
        self.init_window.config(background='#84E5EE')

        self.label_title = Label(self.init_window, text="Clique gauche sur une case pour placer ou retirer un objet, le robot est dans la case rouge", font = ("",14), bg='#84E5EE', fg='white')
        self.label_title.pack(side=BOTTOM)
        
        # taille d'une case
        self.size_case = 15

        # dimensions du canevas
        self.can_width = arene.x * self.size_case 
        self.can_height = arene.y * self.size_case 

        # création canevas
        self.can = Canvas(self.init_window, width=self.can_width, height=self.can_height)
        self.can.pack()

        # binding de la fonction modifierTableau sur le canevas
        self.can.bind("<Button-1>", self.modifierTableau)

    def afficher(self):
        """
        Fonction d'affichage du tableau ; 1 élément = 1 case
        La couleur de la "case" dépend de l'état de l'élement correspondant
        """
        for i in range(0, self.arene.x):
            for j in range(0, self.arene.y):
                self.can.create_rectangle(i * self.size_case, j * self.size_case , i * self.size_case + self.size_case, j * self.size_case + self.size_case, fill = self.couleurs[self.arene.matrice[i][j]])

    def modifierTableau(self, evt):

        # inverser la valeur de l'élément cliqué si c'est un obstacle ou une case vide
        # ne fait rien si on clique sur le robot

        pos_x = int(evt.x / self.size_case)
        pos_y = int(evt.y / self.size_case)

        if self.arene.matrice[pos_x][pos_y] == 2:
            self.arene.matrice[pos_x][pos_y] = 2
        elif self.arene.matrice[pos_x][pos_y] == 0:
            self.arene.matrice[pos_x][pos_y] = 1
        else:
            self.arene.matrice[pos_x][pos_y] = 0

        self.afficher()

    def quit(self):
        self.init_window.destroy()

arene = Arene(30, 25)
fenetre = Fenetre(arene)
fenetre.afficher()
fenetre.init_window.mainloop()