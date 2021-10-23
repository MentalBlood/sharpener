import pstats
import cProfile



class Profile(cProfile.Profile):
	
	@property
	def report(self):
		return {
			k[2]: {
				'number': v[0], 
				'time': v[2]
			} 
			for k, v in pstats.Stats(self).stats.items()
		}



import sys
sys.modules[__name__] = Profile