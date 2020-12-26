from backend.districts.industrial_zone import IndustrialZone
import pytest

@pytest.fixture(scope="function")
def setup_district():
    dist = IndustrialZone()
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
    ('maintenance', 1),
    ('building_list', None),
    ('workshop', False),
    ('factory', False),
    ('coal_power_plant', False),
    ('oil_power_plant', False),
    ('nuclear_power_plant', False),
]
@pytest.mark.parametrize("resource, value", testdata)
def test_init(setup_district, resource, value):
    test_district = setup_district
    assert getattr(test_district, resource) == value

# Workshop
testdata = [
    ('production', 5),
    ('science', 0),
    ('citizen_slot', 1),
    ('power', 0),
    ('powered', False),
    ('maintenance', 2),
    ('building_list', [
        'workshop',
    ]),
    ('workshop', True),
    ('factory', False),
    ('coal_power_plant', False),
    ('oil_power_plant', False),
    ('nuclear_power_plant', False),
]
@pytest.mark.parametrize("resource, value", testdata)
def test_workshop(setup_district, resource, value):
    test_district = setup_district
    test_district.set_buildings('workshop')
    test_district.calculate_specialist_yield()
    assert getattr(test_district, resource) == value

# Unpowered Factory
testdata = [
    ('production', 10),
    ('science', 0),
    ('citizen_slot', 2),
    ('power', 0),
    ('powered', False),
    ('maintenance', 4),
    ('building_list', [
        'workshop',
        'factory',
    ]),
    ('workshop', True),
    ('factory', True),
    ('coal_power_plant', False),
    ('oil_power_plant', False),
    ('nuclear_power_plant', False),
]
@pytest.mark.parametrize("resource, value", testdata)
def test_unpowered_factory(setup_district, resource, value):
    test_district = setup_district
    test_district.set_buildings('factory', False)
    test_district.calculate_specialist_yield()
    assert getattr(test_district, resource) == value

# Powered Factory
testdata = [
    ('production',13),
    ('science', 0),
    ('citizen_slot', 2),
    ('power', 2),
    ('powered', True),
    ('maintenance', 4),
    ('building_list', [
        'workshop',
        'factory',
    ]),
    ('workshop', True),
    ('factory', True),
    ('coal_power_plant', False),
    ('oil_power_plant', False),
    ('nuclear_power_plant', False),
]
@pytest.mark.parametrize("resource, value", testdata)
def test_powered_factory(setup_district, resource, value):
    test_district = setup_district
    test_district.set_buildings('factory', True)
    test_district.calculate_specialist_yield()
    assert getattr(test_district, resource) == value

# Unspecified Factory
testdata = [
    ('production', 13),
    ('science', 0),
    ('citizen_slot', 2),
    ('power', 2),
    ('powered', True),
    ('maintenance', 4),
    ('building_list', [
        'workshop',
        'factory',
    ]),
    ('workshop', True),
    ('factory', True),
    ('coal_power_plant', False),
    ('oil_power_plant', False),
    ('nuclear_power_plant', False),
]
@pytest.mark.parametrize("resource, value", testdata)
def test_unspecified_powered_factory(setup_district, resource, value):
    test_district = setup_district
    test_district.set_buildings('factory')
    test_district.calculate_specialist_yield()
    assert getattr(test_district, resource) == value

# Coal Power Plant
testdata = [
    ('production', 18),
    ('science', 0),
    ('citizen_slot', 3),
    ('power', 2),
    ('powered', True),
    ('maintenance', 7),
    ('building_list', [
        'workshop',
        'factory',
        'coal_power_plant',
    ]),
    ('workshop', True),
    ('factory', True),
    ('coal_power_plant', True),
    ('oil_power_plant', False),
    ('nuclear_power_plant', False),
]
@pytest.mark.parametrize("resource, value", testdata)
def test_coal_power_plant(setup_district, resource, value):
    test_district = setup_district
    test_district.set_buildings('coal_power_plant')
    test_district.calculate_specialist_yield()
    assert getattr(test_district, resource) == value

# Oil Power Plant
testdata = [
    ('production', 21),
    ('science', 0),
    ('citizen_slot', 3),
    ('power', 2),
    ('powered', True),
    ('maintenance', 7),
    ('building_list', [
        'workshop',
        'factory',
        'oil_power_plant',
    ]),
    ('workshop', True),
    ('factory', True),
    ('coal_power_plant', False),
    ('oil_power_plant', True),
    ('nuclear_power_plant', False),
]
@pytest.mark.parametrize("resource, value", testdata)
def test_oil_power_plant(setup_district, resource, value):
    test_district = setup_district
    test_district.set_buildings('oil_power_plant')
    test_district.calculate_specialist_yield()
    assert getattr(test_district, resource) == value

# Coal Power Plant
testdata = [
    ('production', 22),
    ('science', 3),
    ('citizen_slot', 3),
    ('power', 2),
    ('powered', True),
    ('maintenance', 7),
    ('building_list', [
        'workshop',
        'factory',
        'nuclear_power_plant',
    ]),
    ('workshop', True),
    ('factory', True),
    ('coal_power_plant', False),
    ('oil_power_plant', False),
    ('nuclear_power_plant', True),
]
@pytest.mark.parametrize("resource, value", testdata)
def test_nuclear_power_plant(setup_district, resource, value):
    test_district = setup_district
    test_district.set_buildings('nuclear_power_plant')
    test_district.calculate_specialist_yield()
    assert getattr(test_district, resource) == value

# Final check
testdata = [
    ('food', 0),
    ('production', 22),
    ('gold', 0),
    ('science', 3),
    ('culture', 0),
    ('faith', 0),
    ('population', 0),
    ('housing', 0),
    ('citizen_slot', 3),
    ('power', 2),
    ('powered', True),
    ('maintenance', 7),
    ('building_list', [
        'workshop',
        'factory',
        'nuclear_power_plant',
    ]),
    ('workshop', True),
    ('factory', True),
    ('coal_power_plant', False),
    ('oil_power_plant', False),
    ('nuclear_power_plant', True),
]
@pytest.mark.parametrize("resource, value", testdata)
def test_final_check(setup_district, resource, value):
    test_district = setup_district
    test_district.set_buildings()
    test_district.calculate_specialist_yield()
    assert getattr(test_district, resource) == value
