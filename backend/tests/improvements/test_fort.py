from backend.improvements.fort import Fort
import pytest

@pytest.fixture(scope="function")
def setup_improvement():
    imp = Fort()
    return imp

# Init
testdata = [
    ('food', 0),
    ('production', 0),
    ('gold', 0),
    ('science', 0),
    ('culture', 0),
    ('faith', 0),
    ('housing', 0),
    ('appeal', 0),
    ('power', 0),
    ('acceptable_terrain', None),
    ('acceptable_features', None),
    ('resources', None),
]
@pytest.mark.parametrize("resource, value", testdata)
def test_init(setup_improvement, resource, value):
    test_improvement = setup_improvement
    assert getattr(test_improvement, resource) == value
