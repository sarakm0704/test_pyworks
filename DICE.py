import random

class Dice:
	face_num = 6
	def __init__(self):
		print('HELLO! NICE TO MEET YA!')
	def shoot(self):
		return random.randint(1, self.face_num)
