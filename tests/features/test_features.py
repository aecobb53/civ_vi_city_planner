from backend.features.cataract import Cataract
from backend.features.cliffs import Cliffs
from backend.features.floodplains import Floodplains
from backend.features.geothermal_fissure import GeothermalFissure
from backend.features.ice import Ice
from backend.features.impact_zone import ImpactZone
from backend.features.marsh import Marsh
from backend.features.mountain import Mountain
from backend.features.oasis import Oasis
from backend.features.rainforest import Rainforest
from backend.features.reef import Reef
from backend.features.river import River
from backend.features.volcanic_soil import VolcanicSoil
from backend.features.volcano import Volcano
from backend.features.woods import Woods
import pytest

# testdata = [
#     ('food', 0),
#     ('production', 0),
#     ('gold', 0),
#     ('acceptable_terrain', [

#     ]),
# ]


# Cataract Init
testdata = [
    ('food', 0),
    ('production', 0),
    ('gold', 0),
    ('acceptable_terrain', [
        'coast',
        'lake',
        'ocean',
    ]),
]
@pytest.mark.parametrize("resource, value", testdata)
def test_cataract(resource, value):
    test_feature = Cataract()
    assert getattr(test_feature, resource) == value

# Cliffs Init
testdata = [
    ('food', 0),
    ('production', 0),
    ('gold', 0),
    ('acceptable_terrain', [
        'desert',
        'deserth',
        'grassland',
        'grasslandh',
        'plains',
        'plainsh',
        'snow',
        'snowh',
        'tundra',
        'tundrah',
    ]),
]
@pytest.mark.parametrize("resource, value", testdata)
def test_cliffs(resource, value):
    test_feature = Cliffs()
    assert getattr(test_feature, resource) == value

# Floodplains Init
testdata = [
    ('food', 3),
    ('production', 0),
    ('gold', 0),
    ('acceptable_terrain', [
        'desert',
        'plains',
        'grassland',
    ]),
]
@pytest.mark.parametrize("resource, value", testdata)
def test_floodplains(resource, value):
    test_feature = Floodplains()
    assert getattr(test_feature, resource) == value
Floodplains

# GeothermalFissure Init
testdata = [
    ('food', 0),
    ('production', 0),
    ('gold', 0),
    ('science', 1),
    ('acceptable_terrain', [
        'desert',
        'grassland',
        'plains',
        'snow',
        'tundra',
    ]),
]
@pytest.mark.parametrize("resource, value", testdata)
def test_geothermal_fissure(resource, value):
    test_feature = GeothermalFissure()
    assert getattr(test_feature, resource) == value
GeothermalFissure

# Ice Init
testdata = [
    ('food', 0),
    ('production', 0),
    ('gold', 0),
    ('acceptable_terrain', [
        'coast',
        'ocean',
    ]),
]
@pytest.mark.parametrize("resource, value", testdata)
def test_ice(resource, value):
    test_feature = Ice()
    assert getattr(test_feature, resource) == value

# ImpactZone Init
testdata = [
    ('food', 0),
    ('production', 0),
    ('gold', 0),
    ('acceptable_terrain', [
        'desert',
        'deserth',
        'grassland',
        'grasslandh',
        'plains',
        'plainsh',
        'snow',
        'snowh',
        'tundra',
        'tundrah',
    ]),
]
@pytest.mark.parametrize("resource, value", testdata)
def test_impact_zone(resource, value):
    test_feature = ImpactZone()
    assert getattr(test_feature, resource) == value
ImpactZone

# Marsh Init
testdata = [
    ('food', 1),
    ('production', 0),
    ('gold', 0),
    ('acceptable_terrain', [
        'grassland',
    ]),
]
@pytest.mark.parametrize("resource, value", testdata)
def test_marsh(resource, value):
    test_feature = Marsh()
    assert getattr(test_feature, resource) == value

# Mountain Init
testdata = [
    ('food', 0),
    ('production', 0),
    ('gold', 0),
    ('acceptable_terrain', [
        'desert',
        'grassland',
        'plains',
        'snow',
        'tundra',
    ]),
]
@pytest.mark.parametrize("resource, value", testdata)
def test_mountain(resource, value):
    test_feature = Mountain()
    assert getattr(test_feature, resource) == value

# Oasis Init
testdata = [
    ('food', 3),
    ('production', 0),
    ('gold', 1),
    ('acceptable_terrain', [
        'desert',
    ]),
]
@pytest.mark.parametrize("resource, value", testdata)
def test_oasis(resource, value):
    test_feature = Oasis()
    assert getattr(test_feature, resource) == value

# Rainforest Init
testdata = [
    ('food', 1),
    ('production', 0),
    ('gold', 0),
    ('acceptable_terrain', [
        'plains',
        'plainsh',
    ]),
]
@pytest.mark.parametrize("resource, value", testdata)
def test_rainforest(resource, value):
    test_feature = Rainforest()
    assert getattr(test_feature, resource) == value
Rainforest

# Reef Init
testdata = [
    ('food', 1),
    ('production', 1),
    ('gold', 0),
    ('acceptable_terrain', [
        'coast',
    ]),
]
@pytest.mark.parametrize("resource, value", testdata)
def test_reef(resource, value):
    test_feature = Reef()
    assert getattr(test_feature, resource) == value

# River Init
testdata = [
    ('food', 0),
    ('production', 0),
    ('gold', 0),
    ('acceptable_terrain', [
        'desert',
        'deserth',
        'grassland',
        'grasslandh',
        'plains',
        'plainsh',
        'snow',
        'snowh',
        'tundra',
        'tundrah',
    ]),
]
@pytest.mark.parametrize("resource, value", testdata)
def test_river(resource, value):
    test_feature = River()
    assert getattr(test_feature, resource) == value

# VolcanicSoil Init
testdata = [
    ('food', 0),
    ('production', 0),
    ('gold', 0),
    ('acceptable_terrain', [
        'desert',
        'deserth',
        'grassland',
        'grasslandh',
        'plains',
        'plainsh',
        'snow',
        'snowh',
        'tundra',
        'tundrah',
    ]),
]
@pytest.mark.parametrize("resource, value", testdata)
def test_volcanic_soil(resource, value):
    test_feature = VolcanicSoil()
    assert getattr(test_feature, resource) == value
VolcanicSoil

# Volcano Init
testdata = [
    ('food', 0),
    ('production', 0),
    ('gold', 0),
    ('acceptable_terrain', [
        'desert',
        'grassland',
        'plains',
        'snow',
        'tundra',
    ]),
]
@pytest.mark.parametrize("resource, value", testdata)
def test_volcano(resource, value):
    test_feature = Volcano()
    assert getattr(test_feature, resource) == value

# Woods Init
testdata = [
    ('food', 0),
    ('production', 1),
    ('gold', 0),
    ('acceptable_terrain', [
        'grassland',
        'grasslandh',
        'plains',
        'plainsh',
        'tundra',
        'tundrah',
    ]),
]
@pytest.mark.parametrize("resource, value", testdata)
def test_woods(resource, value):
    test_feature = Woods()
    assert getattr(test_feature, resource) == value
