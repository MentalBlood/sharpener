from . import Profile



def report(
	f,
	exclude_calls
):

	exclude_calls.append("<method 'disable' of '_lsprof.Profiler' objects>")

	p = Profile()

	p.enable()
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