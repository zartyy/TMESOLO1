class Robot:
   def __init__(self,carte,nom):
      self.id= nom
      self.map = carte #le robot recupere la grille
      self.dir= [0,0]
      self.pos= [0,0]
