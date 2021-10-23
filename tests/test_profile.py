from math import sqrt
from sharpener import Profile



def test_stats():

	p = Profile()
	
	p.enable()
	[sqrt(i) for i in range(10 ** 4)]
	p.disable()
	
	assert type(p.report) == dict
	
	assert 'time' in p.report
	assert type(p.report['time']) == float
	
	assert 'calls' in p.report
	for k, v in p.report['calls'].items():
		
		assert type(k) == str
		assert type(v) == dict
		
		assert 'number' in v
		assert type(v['number']) == int
		assert type(v['time']) == float