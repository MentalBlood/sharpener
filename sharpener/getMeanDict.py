from statistics import mean



class Accumulator:

	def __init__(self):
		
		self.sum = 0
		self.number = 0
		self.type = int
	
	def add(self, value):

		self.sum += value
		self.number += 1
		
		if type(value) == float:
			self.type = float
	
	@property
	def current(self):
		if self.type == float:
			return self.sum / self.number
		else:
			return self.sum // self.number


def getMeanDict(*args):

	result = {}

	for d in args:

		for k in d.keys():

			if type(d[k]) == dict:
				if not k in result:
					result[k] = getMeanDict(*[e[k] for e in args if k in e])
			
			else:
				if not k in result:
					result[k] = Accumulator()
				result[k].add(d[k])
	
	for k in result:
		if type(result[k]) == Accumulator:
			result[k] = result[k].current

	return result



import sys
sys.modules[__name__] = getMeanDict