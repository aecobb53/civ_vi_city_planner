from backend.improvements.geothermal_plant import GeothermalPlant
import pytest

@pytest.fixture(scope="function")
def setup_improvement():
    imp = GeothermalPlant()
    return imp

# Init
testdata = [
    ('food', 0),
    ('production', 2),
    ('gold', 0),
    ('science', 1),
    ('culture', 0),
    ('faith', 0),
    ('housing', 0),
    ('appeal', 0),
    ('power', 4),
    ('acceptable_terrain', None),
    ('acceptable_features', [
        'geothermal_fissure',
    ]),
    ('resources', None),
]
@pytest.mark.parametrize("resource, value", testdata)
def test_init(setup_improvement, resource, value):
    test_improvement = setup_improvement
    assert getattr(test_improvement, resource) == value
