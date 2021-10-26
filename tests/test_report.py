from math import sqrt
from functools import partial
from sharpener import report



def test_basic():

	f = lambda n: [sqrt(i) for i in range(n)]

	r = report(
		f=partial(f, n=10**4), 
		n=10
	)

	assert type(r) == dict
	
	assert 'time' in r
	assert type(r['time']) == float
	
	assert 'calls' in r
	for k, v in r['calls'].items():
		
		assert type(k) == str
		assert type(v) == dict
		
		assert 'number' in v
		assert type(v['number']) == int
		assert type(v['time']) == float