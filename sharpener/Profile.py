import pstats
import cProfile



class Profile(cProfile.Profile):

	def __init__(self, exclude_calls=["<method 'disable' of '_lsprof.Profiler' objects>"], **kwargs):
		self.exclude_calls = exclude_calls
		super().__init__(**kwargs)
	
	@property
	def report(self):

		stats = pstats.Stats(self)
		
		calls = {
			'time': stats.total_tt,
			'calls': {
				k[2]: {
					'number': v[0], 
					'time': v[2]
				} 
				for k, v in stats.stats.items()
			}
		}

		for name in self.exclude_calls:
			calls['time'] -= calls['calls'][name]['time']
			del calls['calls'][name]
		
		return calls



import sys
sys.modules[__name__] = Profile