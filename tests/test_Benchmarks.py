from sharpener import Benchmarks



def test_init():

	b = Benchmarks()

	assert type(b.modules) == list
	assert len(b.modules) == 2