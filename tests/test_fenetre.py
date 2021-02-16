import unittest
from fenetre import Fenetre
from arene import Arene
from math import pi as PI
class TestRobot(unittest.TestCase):
	def setUp(self):
		self.a=Arene()
		self.f= Fenetre(self.a)

	def test_fenetre(self):
		self.assertEqual(self.f.arene, self.a)

	def test_avancerRobot(self):
		self.f.avancerRobot()
		self.assertEqual(self.f.arene.robot.pos, [12.0, 10.0])
		pos= self.a.robot.pos
		self.assertEqual(self.a.tableau[int(pos[0])][int(pos[1])], 2)

		self.a.robot.changerVitesseSimple(1)
		self.f.avancerRobot()
		self.assertEqual(self.f.arene.robot.pos, [15.0, 10.0])
		pos= self.a.robot.pos

	def test_tourneRobot(self):
		self.f.tourneRobot()
		self.assertEqual(self.a.robot.angle, PI/2)

	def test_tourneRobot10(self):
		self.f.tourneRobot10()
		self.assertEqual(self.a.robot.angle, PI/9)

	def test_tourneRobot10(self):
		self.f.tourneRobot_10()
		self.assertEqual(self.a.robot.angle, -PI/9)

	def test_augmenterVitesseRobot(self):
		vitesse= self.f.arene.robot.vitesse
		self.f.augmenterVitesseRobot()
		self.assertEqual(self.f.arene.robot.vitesse, vitesse+1)

	def test_augmenterVitesseRobot(self):
		vitesse= self.f.arene.robot.vitesse
		self.f.diminuerVitesseRobot()
		self.assertEqual(self.f.arene.robot.vitesse, vitesse-1)

if __name__ == '__main__':
	unittest.main()