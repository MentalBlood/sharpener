from . import Profile
from timeit import timeit



def report(
	f,
	exclude_calls,
	profile
):

	if profile:

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

	else:

		r = {
			'time': timeit('f()', globals=globals() | {'f': f}, number=1),
			'calls': {}
		}

	return r



import sys
sys.modules[__name__] = report