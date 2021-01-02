from backend.improvements.wind_farm import WindFarm
import pytest

@pytest.fixture(scope="function")
def setup_improvement():
    imp = WindFarm()
    return imp

# Init
testdata = [
    ('food', 0),
    ('production', 1),
    ('gold', 1),
    ('science', 0),
    ('culture', 0),
    ('faith', 0),
    ('housing', 0),
    ('appeal', 0),
    ('power', 2),
    ('acceptable_terrain', [
        'deserth',
        'grasslandh',
        'plainsh',
        'snowh',
        'tundrah',
    ]),
    ('acceptable_features', None),
    ('resources', None),
]
@pytest.mark.parametrize("resource, value", testdata)
def test_init(setup_improvement, resource, value):
    test_improvement = setup_improvement
    assert getattr(test_improvement, resource) == value
