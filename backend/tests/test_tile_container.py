import pytest

from backend.tile_container import Tile
from backend.terrain import *
from backend.features import *
from backend.improvements import *
from backend.districts import *
from backend.resources import *

# @pytest.fixture(scope="function")
def setup_tile_container(tile_element_list):
    dist = Tile(tile_element_list)
    return dist

# Init
def test_init():
    container = setup_tile_container([])
    assert getattr(container, 'terrain') is None
    assert getattr(container, 'hills') is None
    assert getattr(container, 'feature') is None
    assert getattr(container, 'river') is None
    assert getattr(container, 'resource') is None
    assert getattr(container, 'improvement') is None
    assert getattr(container, 'district') is None
    assert getattr(container, 'wonder') is None
    assert getattr(container, 'config') is not None

# Terrain, Hills, River
def test_terrain():
    container = setup_tile_container([
        'grassland',
        'hills',
        'river',
    ])
    assert isinstance(getattr(container, 'terrain'), Grassland)
    assert isinstance(getattr(container, 'hills'), Hills)
    assert isinstance(getattr(container, 'river'), River)

# Terrain, Hills, River
def test_feature_happy():
    container = setup_tile_container([
        'grassland',
        'woods',
        'hills',
        'river',
    ])
    assert isinstance(getattr(container, 'terrain'), Grassland)
    assert isinstance(getattr(container, 'feature'), Woods)
    assert isinstance(getattr(container, 'hills'), Hills)
    assert isinstance(getattr(container, 'river'), River)
    
def test_feature_sad():
    container = setup_tile_container([
        'grassland',
        'ice',
    ])
    print('feature')
    print(getattr(container, 'feature'))
    assert isinstance(getattr(container, 'terrain'), Grassland)
    assert getattr(container, 'feature') is None

# # Init
# testdata = [
#     ('food', 0),
#     ('production', 0),
#     ('gold', 0),
#     ('science', 0),
#     ('culture', 0),
#     ('faith', 0),
#     ('population', 0),
#     ('housing', 0),
#     ('citizen_slot', 0),
#     ('power', 0),
#     ('powered', False),
#     ('maintenance', 1),
#     ('building_list', None),
#     ('library', False),
#     ('university', False),
#     ('research_lab', False),
# ]
# @pytest.mark.parametrize("resource, value", testdata)
# def test_init(setup_district, resource, value):
#     test_district = setup_district
#     assert getattr(test_district, resource) == value

# # Library
# testdata = [
#     ('science', 4),
#     ('housing', 0),
#     ('citizen_slot', 1),
#     ('power', 0),
#     ('powered', False),
#     ('maintenance', 2),
#     ('building_list', [
#         'library',
#     ]),
#     ('library', True),
#     ('university', False),
#     ('research_lab', False),
# ]
# @pytest.mark.parametrize("resource, value", testdata)
# def test_library(setup_district, resource, value):
#     test_district = setup_district
#     test_district.set_buildings('library')
#     test_district.calculate_specialist_yield()
#     assert getattr(test_district, resource) == value

# # University
# testdata = [
#     ('science', 10),
#     ('housing', 1),
#     ('citizen_slot', 2),
#     ('power', 0),
#     ('powered', False),
#     ('maintenance', 4),
#     ('building_list', [
#         'library',
#         'university',
#     ]),
#     ('library', True),
#     ('university', True),
#     ('research_lab', False),
# ]
# @pytest.mark.parametrize("resource, value", testdata)
# def test_university(setup_district, resource, value):
#     test_district = setup_district
#     test_district.set_buildings('university')
#     test_district.calculate_specialist_yield()
#     assert getattr(test_district, resource) == value

# # Unpowered Research Lab
# testdata = [
#     ('science', 18),
#     ('housing', 1),
#     ('citizen_slot', 3),
#     ('power', 0),
#     ('powered', False),
#     ('maintenance', 7),
#     ('building_list', [
#         'library',
#         'university',
#         'research_lab',
#     ]),
#     ('library', True),
#     ('university', True),
#     ('research_lab', True),
# ]
# @pytest.mark.parametrize("resource, value", testdata)
# def test_unpowered_research_lab(setup_district, resource, value):
#     test_district = setup_district
#     test_district.set_buildings('research_lab', False)
#     test_district.calculate_specialist_yield()
#     assert getattr(test_district, resource) == value

# # Powered Research Lab
# testdata = [
#     ('science', 23),
#     ('housing', 1),
#     ('citizen_slot', 3),
#     ('power', 3),
#     ('powered', True),
#     ('maintenance', 7),
#     ('building_list', [
#         'library',
#         'university',
#         'research_lab',
#     ]),
#     ('library', True),
#     ('university', True),
#     ('research_lab', True),
# ]
# @pytest.mark.parametrize("resource, value", testdata)
# def test_powered_research_lab(setup_district, resource, value):
#     test_district = setup_district
#     test_district.set_buildings('research_lab', True)
#     test_district.calculate_specialist_yield()
#     assert getattr(test_district, resource) == value

# # Final check
# testdata = [
#     ('food', 0),
#     ('production', 0),
#     ('gold', 0),
#     ('science', 23),
#     ('culture', 0),
#     ('faith', 0),
#     ('population', 0),
#     ('housing', 1),
#     ('citizen_slot', 3),
#     ('power', 3),
#     ('powered', True),
#     ('maintenance', 7),
#     ('building_list', [
#         'library',
#         'university',
#         'research_lab',
#     ]),
#     ('library', True),
#     ('university', True),
#     ('research_lab', True),
# ]
# @pytest.mark.parametrize("resource, value", testdata)
# def test_final_check(setup_district, resource, value):
#     test_district = setup_district
#     test_district.set_buildings()
#     test_district.calculate_specialist_yield()
#     assert getattr(test_district, resource) == value
