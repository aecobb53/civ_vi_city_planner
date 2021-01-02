from backend.resources.bananas import Bananas
from backend.resources.copper import Copper
from backend.resources.cattle import Cattle
from backend.resources.crabs import Crabs
from backend.resources.deer import Deer
from backend.resources.fish import Fish
from backend.resources.maize import Maize
from backend.resources.rice import Rice
from backend.resources.sheep import Sheep
from backend.resources.stone import Stone
from backend.resources.wheat import Wheat
import pytest

# Bananas
testdata = [
    ('food', 1),
    ('production', 0),
    ('gold', 0),
    ('science', 0),
    ('culture', 0),
    ('faith', 0),
    ('resource_type', 'bonus'),
    ('terrain', None),
    ('features', [
        'rainforest',
    ]),
    ('improvement', [
        'plantation',
    ]),
]
@pytest.mark.parametrize("resource, value", testdata)
def test_bananas(resource, value):
    test_resource = Bananas()
    assert getattr(test_resource, resource) == value

# Copper
testdata = [
    ('food', 0),
    ('production', 0),
    ('gold', 2),
    ('science', 0),
    ('culture', 0),
    ('faith', 0),
    ('resource_type', 'bonus'),
    ('terrain', [
        'grasslandh',
        'plainsh',
        'deserth',
        'tundrah',
        'snowh',
    ]),
    ('features', None),
    ('improvement', [
        'mine',
    ]),
]
@pytest.mark.parametrize("resource, value", testdata)
def test_copper(resource, value):
    test_resource = Copper()
    assert getattr(test_resource, resource) == value

# Cattle
testdata = [
    ('food', 1),
    ('production', 0),
    ('gold', 0),
    ('science', 0),
    ('culture', 0),
    ('faith', 0),
    ('resource_type', 'bonus'),
    ('terrain', [
        'grassland',
    ]),
    ('features', None),
    ('improvement', [
        'pasture',
    ]),
]
@pytest.mark.parametrize("resource, value", testdata)
def test_cattle(resource, value):
    test_resource = Cattle()
    assert getattr(test_resource, resource) == value

# Crabs
testdata = [
    ('food', 0),
    ('production', 0),
    ('gold', 2),
    ('science', 0),
    ('culture', 0),
    ('faith', 0),
    ('resource_type', 'bonus'),
    ('terrain', [
        'coast',
        'lake',
    ]),
    ('features', None),
    ('improvement', [
        'fishing_boats',
    ]),
]
@pytest.mark.parametrize("resource, value", testdata)
def test_crabs(resource, value):
    test_resource = Crabs()
    assert getattr(test_resource, resource) == value

# Deer
testdata = [
    ('food', 0),
    ('production', 1),
    ('gold', 0),
    ('science', 0),
    ('culture', 0),
    ('faith', 0),
    ('resource_type', 'bonus'),
    ('terrain', None),
    ('features', None),
    ('improvement', [
        'camp',
    ]),
]
@pytest.mark.parametrize("resource, value", testdata)
def test_deer(resource, value):
    test_resource = Deer()
    assert getattr(test_resource, resource) == value

# Fish
testdata = [
    ('food', 1),
    ('production', 0),
    ('gold', 0),
    ('science', 0),
    ('culture', 0),
    ('faith', 0),
    ('resource_type', 'bonus'),
    ('terrain', [
        'coast',
        'lake',
    ]),
    ('features', None),
    ('improvement', [
        'fishing_boats',
    ]),
]
@pytest.mark.parametrize("resource, value", testdata)
def test_fish(resource, value):
    test_resource = Fish()
    assert getattr(test_resource, resource) == value

# Maize
testdata = [
    ('food', 0),
    ('production', 0),
    ('gold', 2),
    ('science', 0),
    ('culture', 0),
    ('faith', 0),
    ('resource_type', 'bonus'),
    ('terrain', [
        'grasssland',
        'plains',
    ]),
    ('features', None),
    ('improvement', [
        'farm',
    ]),
]
@pytest.mark.parametrize("resource, value", testdata)
def test_maize(resource, value):
    test_resource = Maize()
    assert getattr(test_resource, resource) == value

# Rice
testdata = [
    ('food', 1),
    ('production', 0),
    ('gold', 0),
    ('science', 0),
    ('culture', 0),
    ('faith', 0),
    ('resource_type', 'bonus'),
    ('terrain', [
        'grassland',
    ]),
    ('features', None),
    ('improvement', [
        'plantation',
    ]),
]
@pytest.mark.parametrize("resource, value", testdata)
def test_rice(resource, value):
    test_resource = Rice()
    assert getattr(test_resource, resource) == value

# Sheep
testdata = [
    ('food', 1),
    ('production', 0),
    ('gold', 0),
    ('science', 0),
    ('culture', 0),
    ('faith', 0),
    ('resource_type', 'bonus'),
    ('terrain', [
        'grasslandh',
        'plainsh',
        'deserth',
        'tundrah',
    ]),
    ('features', None),
    ('improvement', [
            'pasture',
    ]),
]
@pytest.mark.parametrize("resource, value", testdata)
def test_sheep(resource, value):
    test_resource = Sheep()
    assert getattr(test_resource, resource) == value

# Stone
testdata = [
    ('food', 0),
    ('production', 1),
    ('gold', 0),
    ('science', 0),
    ('culture', 0),
    ('faith', 0),
    ('resource_type', 'bonus'),
    ('terrain', [
        'grassland',
        'grasslandh',
    ]),
    ('features', None),
    ('improvement', [
            'mine',
    ]),
]
@pytest.mark.parametrize("resource, value", testdata)
def test_stone(resource, value):
    test_resource = Stone()
    assert getattr(test_resource, resource) == value

# Wheat
testdata = [
    ('food', 1),
    ('production', 0),
    ('gold', 0),
    ('science', 0),
    ('culture', 0),
    ('faith', 0),
    ('resource_type', 'bonus'),
    ('terrain', [
        'plains',
    ]),
    ('features', None),
    ('improvement', [
        'plantation',
    ]),
]
@pytest.mark.parametrize("resource, value", testdata)
def test_wheat(resource, value):
    test_resource = Wheat()
    assert getattr(test_resource, resource) == value
