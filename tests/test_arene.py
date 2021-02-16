import unittest
from arene import Arene
class TestRobot(unittest.TestCase):
	def setUp(self):
		a=[0]
		self.a= Arene()

	def test_arene(self):
		for x in range(len(self.a.tableau)):
			for y in range(len(self.a.tableau[x])):
				if x==self.a.robot.pos[0] and y==self.a.robot.pos[1]:
					self.assertEqual(self.a.tableau[x][y],2)
				else:
					self.assertEqual(self.a.tableau[x][y],0)

		self.assertEqual(self.a.robot.id, "robot")
		self.assertEqual(self.a.robot.pos, [10.0, 10.0])

	def test_avancerRobot(self):
		self.a.avancerRobot()
		self.assertEqual(self.a.robot.pos, [10.0, 10.0])
		pos= self.a.robot.pos
		self.assertEqual(self.a.tableau[int(pos[0])][int(pos[1])], 2)

		self.a.robot.changerVitesseSimple(1)
		self.a.avancerRobot()
		self.assertEqual(self.a.robot.pos, [11.0, 10.0])
		pos= self.a.robot.pos
		self.assertEqual(self.a.tableau[int(pos[0])][int(pos[1])], 2)

	def test_tourneRobot(self):
		self.a.tourneRobot(10)
		self.assertEqual(self.a.robot.angle, 10)

if __name__ == '__main__':
	unittest.main()
