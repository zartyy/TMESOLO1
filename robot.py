from math import *
class Robot:
   def __init__(self,carte,nom):
      self.id= nom
      self.map = carte #le robot recupere la grille
      self.vitesse = 0.0
      self.dir = [0.0,0.0]
      self.pos = [0.0,0.0]
      self.angle = arctan(self.dir[1]/self.dir[0])
   
   def seDeplacer():
      self.pos[0] = self.pos[0] + self.vitesse * cos(self.angle)
      self.pos[1] = self.pos[1] + self.vitesse * sin(self.angle)
    
      
   
      
   def mapUpdate(NouvelleCarte):
      self.map= NouvelleCarte
    
      
