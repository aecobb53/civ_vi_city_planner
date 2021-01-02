from backend.districts.water_park import WaterPark
import pytest

@pytest.fixture(scope="function")
def setup_district():
    dist = WaterPark()
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
    ('amenities', 1),
    ('citizen_slot', 0),
    ('power', 0),
    ('powered', False),
    ('maintenance', 1),
    ('building_list', None),
    ('ferris_wheel', False),
    ('aquarium', False),
    ('aquatics_center', False),
]
@pytest.mark.parametrize("resource, value", testdata)
def test_init(setup_district, resource, value):
    test_district = setup_district
    assert getattr(test_district, resource) == value

# Ferris Wheel
testdata = [
    ('amenities', 2),
    ('culture', 3),
    ('power', 0),
    ('powered', False),
    ('maintenance', 2),
    ('building_list', [
        'ferris_wheel',
    ]),
    ('ferris_wheel', True),
    ('aquarium', False),
    ('aquatics_center', False),
]
@pytest.mark.parametrize("resource, value", testdata)
def test_ferris_wheel(setup_district, resource, value):
    test_district = setup_district
    test_district.set_buildings('ferris_wheel')
    test_district.calculate_specialist_yield()
    assert getattr(test_district, resource) == value

# Aquarium
testdata = [
    ('amenities', 3),
    ('culture', 3),
    ('power', 0),
    ('powered', False),
    ('maintenance', 4),
    ('building_list', [
        'ferris_wheel',
        'aquarium',
    ]),
    ('ferris_wheel', True),
    ('aquarium', True),
    ('aquatics_center', False),
]
@pytest.mark.parametrize("resource, value", testdata)
def test_aquarium(setup_district, resource, value):
    test_district = setup_district
    test_district.set_buildings('aquarium')
    test_district.calculate_specialist_yield()
    assert getattr(test_district, resource) == value

# Unpowered Aquatics Center
testdata = [
    ('amenities', 4),
    ('culture', 3),
    ('power', 0),
    ('powered', False),
    ('maintenance', 7),
    ('building_list', [
        'ferris_wheel',
        'aquarium',
        'aquatics_center',
    ]),
    ('ferris_wheel', True),
    ('aquarium', True),
    ('aquatics_center', True),
]
@pytest.mark.parametrize("resource, value", testdata)
def test_unpowered_aquatics_center(setup_district, resource, value):
    test_district = setup_district
    test_district.set_buildings('aquatics_center', False)
    test_district.calculate_specialist_yield()
    assert getattr(test_district, resource) == value

# Powered Aquatics Center
testdata = [
    ('amenities', 6),
    ('culture', 3),
    ('power', 2),
    ('powered', True),
    ('maintenance', 7),
    ('building_list', [
        'ferris_wheel',
        'aquarium',
        'aquatics_center',
    ]),
    ('ferris_wheel', True),
    ('aquarium', True),
    ('aquatics_center', True),
]
@pytest.mark.parametrize("resource, value", testdata)
def test_unpowered_aquatics_center(setup_district, resource, value):
    test_district = setup_district
    test_district.set_buildings('aquatics_center', True)
    test_district.calculate_specialist_yield()
    assert getattr(test_district, resource) == value

# Final check
testdata = [
    ('food', 0),
    ('production', 0),
    ('gold', 0),
    ('science', 0),
    ('culture', 3),
    ('faith', 0),
    ('population', 0),
    ('housing', 0),
    ('amenities', 6),
    ('citizen_slot', 0),
    ('power', 2),
    ('powered', True),
    ('maintenance', 7),
    ('building_list', [
        'ferris_wheel',
        'aquarium',
        'aquatics_center',
    ]),
    ('ferris_wheel', True),
    ('aquarium', True),
    ('aquatics_center', True),
]
@pytest.mark.parametrize("resource, value", testdata)
def test_final_check(setup_district, resource, value):
    test_district = setup_district
    test_district.set_buildings()
    test_district.calculate_specialist_yield()
    assert getattr(test_district, resource) == value
