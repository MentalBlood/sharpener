from . import Profile



def report(f, kwargs={}, n=1):

	p = Profile()

	p.enable()
	for i in range(n):
		f(**kwargs)
	
	p.disable()

	return p.report



import sys
sys.modules[__name__] = report