from sharpener import getMeanDict



def test_basic():
	assert getMeanDict({'a': 1}, {'a': 3}) == {'a': 2}


def test_cascade():
	assert getMeanDict({
		'a': {
			'b': 1
		}
	}, {
		'a': {
			'b': 3
		}
	}) == {
		'a': {
			'b': 2
		}
	}


def test_mixed():
	assert getMeanDict({
		'a': {
			'b': 1
		},
		'c': 10
	}, {
		'a': {
			'b': 3
		},
		'c': 20
	}) == {
		'a': {
			'b': 2
		},
		'c': 15
	}