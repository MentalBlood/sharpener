from sharpener import Benchmarks, Reports



def test_init():

	b = Benchmarks()

	assert type(b.modules) == dict
	assert len(b.modules) == 2

	assert sorted(b.modules.keys()) == ['list', 'math']

	assert sorted(b.modules['list'].keys()) == ['index']
	assert sorted(b.modules['math'].keys()) == ['power', 'sqr', 'sqrt']


def test_run():

	b = Benchmarks()

	reports = b.run({
		'math::sqrt': {
			'n': 10 ** 5
		}
	})

	assert type(reports) == Reports
	assert len(reports) == 1
	assert 'time' in reports['math::sqrt']
	assert 'calls' in reports['math::sqrt']
	assert not any([c in reports['math::sqrt']['calls'] for c in ["<method 'disable' of '_lsprof.Profiler' objects>"]])