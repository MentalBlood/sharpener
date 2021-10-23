from math import sqrt
from sharpener import Profile



def test_stats():

	p = Profile()
	
	p.enable()
	[sqrt(i) for i in range(10 ** 4)]
	p.disable()
	
	assert type(p.report) == dict
	
	for k, v in p.report.items():
		assert type(k) == str
		assert type(v) == dict
		assert 'number' in v
		assert 'time' in v