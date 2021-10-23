from sharpener import Benchmarks



def test_init():

	b = Benchmarks()

	assert type(b.modules) == dict
	assert len(b.modules) == 2

	assert sorted(b.modules.keys()) == ['list', 'math']

	assert sorted(b.modules['list'].keys()) == ['index']
	assert sorted(b.modules['math'].keys()) == ['power', 'sqr', 'sqrt']