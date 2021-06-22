
 
class Girl(object):
	"""docstring for girl"""
	def __init__(self, age, color, weight, appearance):
		self.age = age
		self.color = color
		self.weight = weight
		self.appearance = appearance
	def smile(self):
		print('XiXi')

Jean = Girl(6, 'white', 25, 'pretty')

print(Jean.age)

Jean.smile()


