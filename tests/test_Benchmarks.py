from sharpener import Benchmarks, Reports



def test_init():

	b = Benchmarks()

	assert type(b.modules) == dict
	assert len(b.modules) == 2

	assert sorted(b.modules.keys()) == ['list', 'math']

	assert sorted(b.modules['list'].keys()) == ['Index']
	assert sorted(b.modules['math'].keys()) == ['Power', 'Sqr', 'Sqrt']


def test_run():

	b = Benchmarks()

	reports = b.run({
		'math::Sqrt': {
			'n': 10 ** 5
		},
		'list::Index': {
			'l': [i for i in range(10 ** 6)],
			'e': 2
		}
	})

	assert type(reports) == Reports
	assert len(reports) == 2
	assert 'time' in reports['math::Sqrt']
	assert 'calls' in reports['math::Sqrt']
	assert not any([c in reports['math::Sqrt']['calls'] for c in ["<method 'disable' of '_lsprof.Profiler' objects>"]])