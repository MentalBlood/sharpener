import pstats
import cProfile



class Profile(cProfile.Profile):
	
	@property
	def report(self):

		stats = pstats.Stats(self)
		
		return {
			'time': stats.total_tt,
			'calls': {
				k[2]: {
					'number': v[0], 
					'time': v[2]
				} 
				for k, v in stats.stats.items()
			}
		}



import sys
sys.modules[__name__] = Profile