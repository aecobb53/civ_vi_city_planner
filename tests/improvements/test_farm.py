from backend.improvements.farm import Farm
import pytest

@pytest.fixture(scope="function")
def setup_improvement():
    imp = Farm()
    return imp

# Init
testdata = [
    ('food', 1),
    ('production', 0),
    ('gold', 0),
    ('science', 0),
    ('culture', 0),
    ('faith', 0),
    ('housing', .5),
    ('appeal', 0),
    ('power', 0),
    ('acceptable_terrain', [
        'grassland',
        'plains',
    ]),
    ('acceptable_features', [
        'floodplains',
        'volcanic_soil',
    ]),
    ('resources', [
        'wheat',
        'rice',
        'maize',
    ]),
]
@pytest.mark.parametrize("resource, value", testdata)
def test_init(setup_improvement, resource, value):
    test_improvement = setup_improvement
    assert getattr(test_improvement, resource) == value
