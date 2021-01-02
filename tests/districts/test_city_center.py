from backend.districts.city_center import CityCenter
import pytest

@pytest.fixture(scope="function")
def setup_district():
    dist = CityCenter()
    return dist

# Init
testdata = [
    ('food', 0),
    ('production', 0),
    ('gold', 0),
    ('science', 0),
    ('culture', 0),
    ('faith', 0),
    ('population', 0),
    ('housing', 0),
    ('citizen_slot', 0),
    ('power', 0),
    ('powered', False),
    ('maintenance', 0),
    ('building_list', None),
    ('monument', False),
    ('granary', False),
    ('water_mill', False),
    ('sewer', False),
    ('flood_barrier', False),
    ('ancient_walls', False),
    ('medival_walls', False),
    ('renaissance_walls', False),
]
@pytest.mark.parametrize("resource, value", testdata)
def test_init(setup_district, resource, value):
    test_district = setup_district
    assert getattr(test_district, resource) == value

# Monument
testdata = [
    ('food', 0),
    ('production', 0),
    ('culture', 2),
    ('housing', 0),
    ('power', 0),
    ('powered', False),
    ('maintenance', 0),
    ('building_list', [
        'monument',
    ]),
    ('monument', True),
    ('granary', False),
    ('water_mill', False),
    ('sewer', False),
    ('flood_barrier', False),
]
@pytest.mark.parametrize("resource, value", testdata)
def test_monument(setup_district, resource, value):
    test_district = setup_district
    test_district.set_buildings('monument')
    test_district.calculate_specialist_yield()
    assert getattr(test_district, resource) == value

# Granary
testdata = [
    ('food', 1),
    ('production', 0),
    ('culture', 2),
    ('housing', 2),
    ('power', 0),
    ('powered', False),
    ('maintenance', 0),
    ('building_list', [
        'monument',
        'granary',
    ]),
    ('monument', True),
    ('granary', True),
    ('water_mill', False),
    ('sewer', False),
    ('flood_barrier', False),
]
@pytest.mark.parametrize("resource, value", testdata)
def test_granary(setup_district, resource, value):
    test_district = setup_district
    test_district.set_buildings('granary')
    test_district.calculate_specialist_yield()
    assert getattr(test_district, resource) == value

# Water Mill
testdata = [
    ('food', 2),
    ('production', 1),
    ('culture', 2),
    ('housing', 2),
    ('power', 0),
    ('powered', False),
    ('maintenance', 0),
    ('building_list', [
        'monument',
        'granary',
        'water_mill',
    ]),
    ('monument', True),
    ('granary', True),
    ('water_mill', True),
    ('sewer', False),
    ('flood_barrier', False),
]
@pytest.mark.parametrize("resource, value", testdata)
def test_water_mill(setup_district, resource, value):
    test_district = setup_district
    test_district.set_buildings('water_mill')
    test_district.calculate_specialist_yield()
    assert getattr(test_district, resource) == value

# Sewer
testdata = [
    ('food', 2),
    ('production', 1),
    ('culture', 2),
    ('housing', 4),
    ('power', 0),
    ('powered', False),
    ('maintenance', 2),
    ('building_list', [
        'monument',
        'granary',
        'water_mill',
        'sewer',
    ]),
    ('monument', True),
    ('granary', True),
    ('water_mill', True),
    ('sewer', True),
    ('flood_barrier', False),
]
@pytest.mark.parametrize("resource, value", testdata)
def test_sewer(setup_district, resource, value):
    test_district = setup_district
    test_district.set_buildings('sewer')
    test_district.calculate_specialist_yield()
    assert getattr(test_district, resource) == value

# Flood Barrier
testdata = [
    ('food', 2),
    ('production', 1),
    ('culture', 2),
    ('housing', 4),
    ('power', 0),
    ('powered', False),
    ('maintenance', 2),
    ('building_list', [
        'monument',
        'granary',
        'water_mill',
        'sewer',
        'flood_barrier',
    ]),
    ('monument', True),
    ('granary', True),
    ('water_mill', True),
    ('sewer', True),
    ('flood_barrier', True),
]
@pytest.mark.parametrize("resource, value", testdata)
def test_flood_barrier(setup_district, resource, value):
    test_district = setup_district
    test_district.set_buildings('flood_barrier')
    test_district.calculate_specialist_yield()
    assert getattr(test_district, resource) == value

# Final check
testdata = [
    ('food', 2),
    ('production', 1),
    ('gold', 0),
    ('science', 0),
    ('culture', 2),
    ('faith', 0),
    ('population', 0),
    ('housing', 4),
    ('citizen_slot', 0),
    ('power', 0),
    ('powered', False),
    ('maintenance', 2),
    ('building_list', [
        'monument',
        'granary',
        'water_mill',
        'sewer',
        'flood_barrier',
    ]),
    ('monument', True),
    ('granary', True),
    ('water_mill', True),
    ('sewer', True),
    ('flood_barrier', True),
]
@pytest.mark.parametrize("resource, value", testdata)
def test_final_check(setup_district, resource, value):
    test_district = setup_district
    test_district.set_buildings()
    test_district.calculate_specialist_yield()
    assert getattr(test_district, resource) == value
