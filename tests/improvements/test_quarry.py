from backend.improvements.quarry import Quarry
import pytest

@pytest.fixture(scope="function")
def setup_improvement():
    imp = Quarry()
    return imp

# Init
testdata = [
    ('food', 0),
    ('production', 1),
    ('gold', 0),
    ('science', 0),
    ('culture', 0),
    ('faith', 0),
    ('housing', 0),
    ('appeal', -1),
    ('power', 0),
    ('acceptable_terrain', None),
    ('acceptable_features', None),
    ('resources', [
        'stone',
        'marble',
        'gypsum',
    ]),
]
@pytest.mark.parametrize("resource, value", testdata)
def test_init(setup_improvement, resource, value):
    test_improvement = setup_improvement
    assert getattr(test_improvement, resource) == value
