from backend.districts.holy_site import HolySite
import pytest

@pytest.fixture(scope="function")
def setup_district():
    dist = HolySite()
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
    ('shrine', False),
    ('temple', False),
]
@pytest.mark.parametrize("resource, value", testdata)
def test_init(setup_district, resource, value):
    test_district = setup_district
    assert getattr(test_district, resource) == value

# Shrine
testdata = [
    ('faith', 4),
    ('citizen_slot', 1),
    ('power', 0),
    ('powered', False),
    ('maintenance', 2),
    ('shrine', True),
    ('temple', False),
]
@pytest.mark.parametrize("resource, value", testdata)
def test_shrine(setup_district, resource, value):
    test_district = setup_district
    test_district.set_buildings('shrine')
    test_district.calculate_specialist_yield()
    assert getattr(test_district, resource) == value

# Temple
testdata = [
    ('faith', 10),
    ('citizen_slot', 2),
    ('power', 0),
    ('powered', False),
    ('maintenance', 4),
    ('shrine', True),
    ('temple', True),
]
@pytest.mark.parametrize("resource, value", testdata)
def test_temple(setup_district, resource, value):
    test_district = setup_district
    test_district.set_buildings('temple')
    test_district.calculate_specialist_yield()
    assert getattr(test_district, resource) == value

# Final check
testdata = [
    ('food', 0),
    ('production', 0),
    ('gold', 0),
    ('science', 0),
    ('culture', 0),
    ('faith', 10),
    ('population', 0),
    ('houseing', 0),
    ('citizen_slot', 2),
    ('power', 0),
    ('powered', False),
    ('maintenance', 4),
    ('shrine', True),
    ('temple', True),
]
@pytest.mark.parametrize("resource, value", testdata)
def test_final_check(setup_district, resource, value):
    test_district = setup_district
    test_district.set_buildings()
    test_district.calculate_specialist_yield()
    assert getattr(test_district, resource) == value
