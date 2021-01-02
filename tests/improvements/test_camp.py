from backend.improvements.camp import Camp
import pytest

@pytest.fixture(scope="function")
def setup_improvement():
    imp = Camp()
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
        'deer',
        'furs',
        'ivory',
        'truffles',
        'honey',
    ]),
]
@pytest.mark.parametrize("resource, value", testdata)
def test_init(setup_improvement, resource, value):
    test_improvement = setup_improvement
    assert getattr(test_improvement, resource) == value
