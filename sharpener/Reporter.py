from . import Profile



def Reporter(n):

	def decorator(f):

		def new_f(*args, **kwargs):

			p = Profile()
			
			p.enable()
			for i in range(n):
				f(*args, **kwargs)
			p.disable()

			return p.report

		return new_f
	
	return decorator



import sys
sys.modules[__name__] = Reporter