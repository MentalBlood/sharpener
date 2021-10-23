from math import sqrt
from sharpener import Reporter



def test_basic():

	f = lambda n: [sqrt(i) for i in range(n)]

	reporter = Reporter(10)(f)
	report = reporter(10 ** 4)

	assert type(report) == dict
	
	for k, v in report.items():
		assert type(k) == str
		assert type(v) == dict
		assert 'number' in v
		assert 'time' in v