from math import *
class Robot:
   def __init__(self,carte,nom):
      self.id= nom
      self.map = carte #le robot recupere la grille
      self.vitesse = 0.0
      self.pos = {'x': 0.0,'y': 0.0}
      self.angle = 0
   
   def seDeplacer(self,time,acc):
      self.pos['x'] = self.pos['x'] + self.vitesse * cos(self.angle) * time + 1/2 * acc * time**2
      self.pos['y'] = self.pos['y'] + self.vitesse * sin(self.angle) * time + 1/2 * acc * time**2

    
   def changerVitesse(self,tours_min): #prend en argument le nombre de tours par minutes en plus ou en moins voulus.
      self.vitesse = self.vitesse + (tours_min/60) # * perimetre de la roue (valeur de son rayon à demander)       
      if self.vitesse < 0.0 :
          self.vitesse = 0.0
      #demander la vitesse max du robot.
      
   def changerVitesseSimple(self,vitesse):
      self.vitesse = self.vitesse + vitesse
      
   def changerAngle(self,degree):
      self.angle = self.angle + degree

   def placerRobot(self,x, y):
      self.pos['x'] = x
      self.pos['y'] = y
      
      
   def mapUpdate(self,NouvelleCarte):
      self.map= NouvelleCarte

    
      
