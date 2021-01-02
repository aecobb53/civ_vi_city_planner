from backend.resources.horses import Horses
from backend.resources.iron import Iron
from backend.resources.niter import Niter
from backend.resources.coal import Coal
from backend.resources.oil import Oil
from backend.resources.aluminum import Aluminum
from backend.resources.uranium import Uranium
import pytest

# testdata = [
#     ('food', 0),
#     ('production', 0),
#     ('gold', 0),
#     ('science', 0),
#     ('culture', 0),
#     ('faith', 0),
#     ('resource_type', 'strategic'),
#     ('terrain', [

#     ]),
#     ('features', [
#         'rainforest',
#     ]),
#     ('improvement', [
#         'plantation',
#     ]),
# ]

# Horses
testdata = [
    ('food', 1),
    ('production', 1),
    ('gold', 0),
    ('science', 0),
    ('culture', 0),
    ('faith', 0),
    ('resource_type', 'strategic'),
    ('terrain', [
        'grassland',
        'plains',
    ]),
    ('features', None),
    ('improvement', [
        'pasture',
    ]),
]
@pytest.mark.parametrize("resource, value", testdata)
def test_horses(resource, value):
    test_resource = Horses()
    assert getattr(test_resource, resource) == value

# Iron
testdata = [
    ('food', 0),
    ('production', 0),
    ('gold', 0),
    ('science', 1),
    ('culture', 0),
    ('faith', 0),
    ('resource_type', 'strategic'),
    ('terrain', [
        'deserth',
        'grasslandh',
        'plainsh',
        'tundrah',
    ]),
    ('features', None),
    ('improvement', [
        'mine',
    ]),
]
@pytest.mark.parametrize("resource, value", testdata)
def test_iron(resource, value):
    test_resource = Iron()
    assert getattr(test_resource, resource) == value

# Niter
testdata = [
    ('food', 1),
    ('production', 1),
    ('gold', 0),
    ('science', 0),
    ('culture', 0),
    ('faith', 0),
    ('resource_type', 'strategic'),
    ('terrain', [
        'desert',
        'grassland',
        'plains',
        'tundra',
    ]),
    ('features', None),
    ('improvement', [
        'mine',
    ]),
]
@pytest.mark.parametrize("resource, value", testdata)
def test_niter(resource, value):
    test_resource = Niter()
    assert getattr(test_resource, resource) == value

# Coal
testdata = [
    ('food', 0),
    ('production', 2),
    ('gold', 0),
    ('science', 0),
    ('culture', 0),
    ('faith', 0),
    ('resource_type', 'strategic'),
    ('terrain', [
        'grasslandh',
        'plainsh',
    ]),
    ('features', None),
    ('improvement', [
        'mine',
    ]),
]
@pytest.mark.parametrize("resource, value", testdata)
def test_coal(resource, value):
    test_resource = Coal()
    assert getattr(test_resource, resource) == value

# Oil
testdata = [
    ('food', 0),
    ('production', 3),
    ('gold', 0),
    ('science', 0),
    ('culture', 0),
    ('faith', 0),
    ('resource_type', 'strategic'),
    ('terrain', [
        'grassland',
        'desert',
        'trundra',
        'coast',
        'lake',
    ]),
    ('features', None),
    ('improvement', [
        'oil_well',
        'offshore_oil_well',
    ]),
]
@pytest.mark.parametrize("resource, value", testdata)
def test_oil(resource, value):
    test_resource = Oil()
    assert getattr(test_resource, resource) == value

# Aluminum
testdata = [
    ('food', 0),
    ('production', 0),
    ('gold', 0),
    ('science', 1),
    ('culture', 0),
    ('faith', 0),
    ('resource_type', 'strategic'),
    ('terrain', [
        'desert',
        'plains',
    ]),
    ('features', None),
    ('improvement', [
        'mine',
    ]),
]
@pytest.mark.parametrize("resource, value", testdata)
def test_aluminum(resource, value):
    test_resource = Aluminum()
    assert getattr(test_resource, resource) == value

# Uranium
testdata = [
    ('food', 0),
    ('production', 2),
    ('gold', 0),
    ('science', 0),
    ('culture', 0),
    ('faith', 0),
    ('resource_type', 'strategic'),
    ('terrain', [
        'desert',
        'grassland',
        'plains',
        'tundra',
    ]),
    ('features', None),
    ('improvement', [
        'mine',
    ]),
]
@pytest.mark.parametrize("resource, value", testdata)
def test_uranium(resource, value):
    test_resource = Uranium()
    assert getattr(test_resource, resource) == value
