from sharpener import Benchmarks



def test_init():

	b = Benchmarks()

	assert type(b.modules) == dict
	assert len(b.modules) == 2
	assert 'list' in b.modules
	assert 'math' in b.modules