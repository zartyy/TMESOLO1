# coding: utf-8

from math import *
class Robot:
   def __init__(self,carte,nom):
      self.id= nom
      self.map = carte #le robot recupere la grille
      self.vitesse = 0.0
      self.pos = [0.0,0.0]
      self.angle = 0
      self.vitesse_roue=[0,0] # En degre par seconde
   

   def seDeplacer(self,time,acc):
      self.pos[0] = self.pos[0] + self.vitesse * cos(self.angle) * time
      self.pos[1] = self.pos[1] + self.vitesse * sin(self.angle) * time + 1/2 * acc * time**2
      # Arrondi de la position du robot à 3 chiffre après la virgule
      self.pos[0]= round(self.pos[0], 3)
      self.pos[1]= round(self.pos[1], 3)
    
   def changerVitesseRoue(self, dps, port): #prend en argument le nombre de tours par minutes en plus ou en moins voulus.
      i=-1
      if port=="MOTORLEFT":
         i=0
      elif port=="RIGHT":
         i=1
      else:
         print("Erreur")
         return
      self.vitesse_roue[i] = self.vitesse[i] + dps
      
   def changerVitesseSimple(self,vitesse):
      self.vitesse = self.vitesse + vitesse
      if self.vitesse < 0.0 :
          self.vitesse = 0.0
      
   def changerAngle(self,degree):
      if self.angle >= 2*pi:
          self.angle = self.angle + degree - 2*pi
      elif self.angle < 0:
          self.angle = self.angle + degree + 2*pi
      else:
          self.angle = self.angle + degree

   def placerRobot(self,x, y):
      self.pos[0] = x
      self.pos[1] = y
      
   def mapUpdate(self,NouvelleCarte):
      self.map= NouvelleCarte
