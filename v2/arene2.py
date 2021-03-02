
class Arene:

    def  __init__(self, x, y):
        self.x = x
        self.y = y
        self.matrice = []
        for i in range(self.x):
            self.matrice.append([0] * self.y)
            
    def changementEtat(self, entier, x, y):
        self.matrice[x][y] = entier
        
arene = Arene(10,15)
"""print(arene.x)
    print(arene.y)
    print(arene.matrice[0][2])
    arene.matrice[0][2] = 5 
    print(arene.matrice[0][2])
    arene.changementEtat(10, 0, 2)
    print(arene.matrice[0][2])"""