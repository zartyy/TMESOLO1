import unittest
from robot import Robot
class TestRobot(unittest.TestCase):
	def setUp(self):
		a=[0]
		self.r= Robot(a,"Jean")

	def test_robot(self):
		self.assertEqual(self.r.id, "Jean")
		self.assertEqual(self.r.map, [0])
		self.assertEqual(self.r.pos[0], 0.0)
		self.assertEqual(self.r.pos[1], 0.0)
		self.assertEqual(self.r.angle, 0)

	def test_changerVitesseSimple(self):
		self.r.changerVitesseSimple(10)
		self.assertEqual(self.r.vitesse,10.0)

	def test_seDeplacer(self):
		self.r.seDeplacer(1,0)
		self.assertEqual(self.r.pos[0],0)
		self.assertEqual(self.r.pos[1],0)

		self.r.changerVitesseSimple(1)
		self.r.seDeplacer(1,0)
		self.assertEqual(self.r.pos[0],1)
		self.assertEqual(self.r.pos[1],0)

	def test_changerAngle(self):
		self.r.changerAngle(-10)
		self.assertEqual(self.r.angle, -10)

	def test_placerRobot(self):
		self.r.placerRobot(10,10)
		self.assertEqual(self.r.pos, [10,10])

	def test_mapUpdate(self):
		self.r.mapUpdate([1])
		self.assertEqual(self.r.map, [1])

if __name__ == '__main__':
	unittest.main()