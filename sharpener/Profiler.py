import pstats
import cProfile

from . import parseProfile



def parseProfile(p):
	return {
		k[2]: {
			'number': v[0], 
			'time': v[2]
		} 
		for k, v in p.stats.items()
	}


class Profiler:

	def __init__(self):
		self.profile = cProfile.Profile()
	
	def enable(self):
		self.profile.enable()
	
	def disable(self):
		self.profile.disable()
	
	@property
	def stats(self):
		return parseProfile(pstats.Stats(self.profile))



import sys
sys.modules[__name__] = Profiler