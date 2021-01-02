from backend.improvements.plantation import Plantation
import pytest

@pytest.fixture(scope="function")
def setup_improvement():
    imp = Plantation()
    return imp

# Init
testdata = [
    ('food', 0),
    ('production', 0),
    ('gold', 2),
    ('science', 0),
    ('culture', 0),
    ('faith', 0),
    ('housing', .5),
    ('appeal', 0),
    ('power', 0),
    ('acceptable_terrain', None),
    ('acceptable_features', None),
    ('resources', [
        'bananas',
        'citrus',
        'cocoa',
        'coffee',
        'cotton',
        'dyes',
        'silk',
        'sugar',
        'tea',
        'tobacco',
        'wine',
        'olives',
    ]),
]
@pytest.mark.parametrize("resource, value", testdata)
def test_init(setup_improvement, resource, value):
    test_improvement = setup_improvement
    assert getattr(test_improvement, resource) == value
