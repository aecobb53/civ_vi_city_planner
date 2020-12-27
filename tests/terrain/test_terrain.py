from backend.terrain.coast import Coast
from backend.terrain.desert import Desert
from backend.terrain.grassland import Grassland
from backend.terrain.lake import Lake
from backend.terrain.ocean import Ocean
from backend.terrain.plains import Plains
from backend.terrain.snow import Snow
from backend.terrain.tundra import Tundra
import pytest

# Coast Init
testdata = [
    ('food', 1),
    ('production', 0),
    ('gold', 1),
    ('hills', False),
]
@pytest.mark.parametrize("resource, value", testdata)
def test_unhilled_coast(resource, value):
    test_terrain = Coast()
    assert getattr(test_terrain, resource) == value

# Tundra Init
testdata = [
    ('food', 1),
    ('production', 0),
    ('gold', 0),
    ('hills', False),
]
@pytest.mark.parametrize("resource, value", testdata)
def test_unhilled_tundra(resource, value):
    test_terrain = Tundra()
    assert getattr(test_terrain, resource) == value

testdata = [
    ('food', 1),
    ('production', 1),
    ('gold', 0),
    ('hills', True),
]
@pytest.mark.parametrize("resource, value", testdata)
def test_hilled_tundra(resource, value):
    test_terrain = Tundra(hills=True)
    assert getattr(test_terrain, resource) == value

# Snow Init
testdata = [
    ('food', 0),
    ('production', 0),
    ('gold', 0),
    ('hills', False),
]
@pytest.mark.parametrize("resource, value", testdata)
def test_unhilled_snow(resource, value):
    test_terrain = Snow()
    assert getattr(test_terrain, resource) == value

testdata = [
    ('food', 0),
    ('production', 1),
    ('gold', 0),
    ('hills', True),
]
@pytest.mark.parametrize("resource, value", testdata)
def test_hilled_snow(resource, value):
    test_terrain = Snow(hills=True)
    assert getattr(test_terrain, resource) == value

# Plains Init
testdata = [
    ('food', 1),
    ('production', 1),
    ('gold', 0),
    ('hills', False),
]
@pytest.mark.parametrize("resource, value", testdata)
def test_unhilled_plains(resource, value):
    test_terrain = Plains()
    assert getattr(test_terrain, resource) == value

testdata = [
    ('food', 1),
    ('production', 2),
    ('gold', 0),
    ('hills', True),
]
@pytest.mark.parametrize("resource, value", testdata)
def test_hilled_plains(resource, value):
    test_terrain = Plains(hills=True)
    assert getattr(test_terrain, resource) == value

# Ocean Init
testdata = [
    ('food', 1),
    ('production', 0),
    ('gold', 0),
    ('hills', False),
]
@pytest.mark.parametrize("resource, value", testdata)
def test_unhilled_ocean(resource, value):
    test_terrain = Ocean()
    assert getattr(test_terrain, resource) == value

# Lake Init
testdata = [
    ('food', 1),
    ('production', 0),
    ('gold', 1),
    ('hills', False),
]
@pytest.mark.parametrize("resource, value", testdata)
def test_unhilled_lake(resource, value):
    test_terrain = Lake()
    assert getattr(test_terrain, resource) == value

# Grassland Init
testdata = [
    ('food', 2),
    ('production', 0),
    ('gold', 0),
    ('hills', False),
]
@pytest.mark.parametrize("resource, value", testdata)
def test_unhilled_grassland(resource, value):
    test_terrain = Grassland()
    assert getattr(test_terrain, resource) == value

testdata = [
    ('food', 2),
    ('production', 1),
    ('gold', 0),
    ('hills', True),
]
@pytest.mark.parametrize("resource, value", testdata)
def test_hilled_grassland(resource, value):
    test_terrain = Grassland(hills=True)
    assert getattr(test_terrain, resource) == value

# Desert Init
testdata = [
    ('food', 0),
    ('production', 0),
    ('gold', 0),
    ('hills', False),
]
@pytest.mark.parametrize("resource, value", testdata)
def test_unhilled_desert(resource, value):
    test_terrain = Desert()
    assert getattr(test_terrain, resource) == value

testdata = [
    ('food', 0),
    ('production', 1),
    ('gold', 0),
    ('hills', True),
]
@pytest.mark.parametrize("resource, value", testdata)
def test_hilled_desert(resource, value):
    test_terrain = Desert(hills=True)
    assert getattr(test_terrain, resource) == value
