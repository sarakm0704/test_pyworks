import random

class Dice:
	def __init__(self, val=6):
		if val not in [4,6,8,12,20]:
			raise Exception('This is not regular polyhedron')
		self.face_num = val

	def shoot(self):
		return random.randint(1, self.face_num)
