from . import Profile



def report(
	f, 
	n=1,
	exclude_calls=[]
):

	exclude_calls.append("<method 'disable' of '_lsprof.Profiler' objects>")

	p = Profile()

	p.enable()
	for i in range(n):
		f()
	p.disable()

	r = p.report

	for name in exclude_calls:
		if name in r['calls']:
			r['time'] -= r['calls'][name]['time']
			del r['calls'][name]

	return r



import sys
sys.modules[__name__] = report