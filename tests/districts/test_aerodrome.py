from backend.districts.aerodrome import Aerodrome
import pytest

@pytest.fixture(scope="function")
def setup_district():
    dist = Aerodrome()
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
    ('houseing', 0),
    ('citizen_slot', 0),
    ('power', 0),
    ('powered', False),
    ('maintenance', 1),
    ('building_list', None),
    ('hanger', False),
    ('airport', False),
]
@pytest.mark.parametrize("resource, value", testdata)
def test_init(setup_district, resource, value):
    campus = setup_district
    assert getattr(campus, resource) == value

# Hanger
testdata = [
    ('production', 2),
    ('power', 0),
    ('powered', False),
    ('maintenance', 2),
    ('building_list', [
        'hanger',
    ]),
    ('hanger', True),
    ('airport', False),
]
@pytest.mark.parametrize("resource, value", testdata)
def test_hanger(setup_district, resource, value):
    campus = setup_district
    campus.set_buildings('hanger')
    campus.calculate_specialist_yield()
    assert getattr(campus, resource) == value

# Unpowered Airport
testdata = [
    ('production', 6),
    ('power', 0),
    ('powered', False),
    ('maintenance', 4),
    ('building_list', [
        'hanger',
        'airport',
    ]),
    ('hanger', True),
    ('airport', True),
]
@pytest.mark.parametrize("resource, value", testdata)
def test_unpowered_airport(setup_district, resource, value):
    campus = setup_district
    campus.set_buildings('airport', False)
    campus.calculate_specialist_yield()
    assert getattr(campus, resource) == value

# Powered Airport
testdata = [
    ('production', 8),
    ('power', 1),
    ('powered', True),
    ('maintenance', 4),
    ('building_list', [
        'hanger',
        'airport',
    ]),
    ('hanger', True),
    ('airport', True),
]
@pytest.mark.parametrize("resource, value", testdata)
def test_powered_airport(setup_district, resource, value):
    campus = setup_district
    campus.set_buildings('airport', True)
    campus.calculate_specialist_yield()
    assert getattr(campus, resource) == value

# Final check
testdata = [
    ('food', 0),
    ('production', 8),
    ('gold', 0),
    ('science', 0),
    ('culture', 0),
    ('faith', 0),
    ('population', 0),
    ('houseing', 0),
    ('citizen_slot', 0),
    ('power', 1),
    ('powered', True),
    ('maintenance', 4),
    ('building_list', [
        'hanger',
        'airport',
    ]),
    ('hanger', True),
    ('airport', True),
]
@pytest.mark.parametrize("resource, value", testdata)
def test_final_check(setup_district, resource, value):
    campus = setup_district
    campus.set_buildings()
    campus.calculate_specialist_yield()
    assert getattr(campus, resource) == value
