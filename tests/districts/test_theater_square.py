from backend.districts.theater_square import TheaterSquare
import pytest

@pytest.fixture(scope="function")
def setup_district():
    dist = TheaterSquare()
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
    ('amphitheater', False),
    ('archaeological_museum', False),
    ('art_museum', False),
    ('broadcast_center', False),
]
@pytest.mark.parametrize("resource, value", testdata)
def test_init(setup_district, resource, value):
    test_district = setup_district
    assert getattr(test_district, resource) == value

# Amphitheater
testdata = [
    ('culture', 4),
    ('citizen_slot', 1),
    ('power', 0),
    ('powered', False),
    ('maintenance', 2),
    ('amphitheater', True),
    ('archaeological_museum', False),
    ('art_museum', False),
    ('broadcast_center', False),
]
@pytest.mark.parametrize("resource, value", testdata)
def test_amphitheater(setup_district, resource, value):
    test_district = setup_district
    test_district.set_buildings('amphitheater')
    test_district.calculate_specialist_yield()
    assert getattr(test_district, resource) == value

# Archaeological Museum
testdata = [
    ('culture', 8),
    ('citizen_slot', 2),
    ('power', 0),
    ('powered', False),
    ('maintenance', 4),
    ('amphitheater', True),
    ('archaeological_museum', True),
    ('art_museum', False),
    ('broadcast_center', False),
]
@pytest.mark.parametrize("resource, value", testdata)
def test_archealogical_museum(setup_district, resource, value):
    test_district = setup_district
    test_district.set_buildings('archaeological_museum')
    test_district.calculate_specialist_yield()
    assert getattr(test_district, resource) == value

# Art Museum
testdata = [
    ('culture', 8),
    ('citizen_slot', 2),
    ('power', 0),
    ('powered', False),
    ('maintenance', 4),
    ('amphitheater', True),
    ('archaeological_museum', False),
    ('art_museum', True),
    ('broadcast_center', False),
]
@pytest.mark.parametrize("resource, value", testdata)
def test_art_museum(setup_district, resource, value):
    test_district = setup_district
    test_district.set_buildings('art_museum')
    test_district.calculate_specialist_yield()
    assert getattr(test_district, resource) == value

# Unpowered Broadcast Center
testdata = [
    ('culture', 12),
    ('citizen_slot', 3),
    ('power', 0),
    ('powered', False),
    ('maintenance', 7),
    ('amphitheater', True),
    ('archaeological_museum', False),
    ('art_museum', True),
    ('broadcast_center', True),
]
@pytest.mark.parametrize("resource, value", testdata)
def test_unpowered_broadcast_center(setup_district, resource, value):
    test_district = setup_district
    test_district.set_buildings('broadcast_center', False)
    test_district.calculate_specialist_yield()
    assert getattr(test_district, resource) == value

# Powered Research Lab
testdata = [
    ('culture', 19),
    ('citizen_slot', 3),
    ('power', 3),
    ('powered', True),
    ('maintenance', 7),
    ('amphitheater', True),
    ('archaeological_museum', False),
    ('art_museum', True),
    ('broadcast_center', True),
]
@pytest.mark.parametrize("resource, value", testdata)
def test_powered_broadcast_center(setup_district, resource, value):
    test_district = setup_district
    test_district.set_buildings('broadcast_center', True)
    test_district.calculate_specialist_yield()
    assert getattr(test_district, resource) == value

# Final check
testdata = [
    ('food', 0),
    ('production', 0),
    ('gold', 0),
    ('science', 0),
    ('culture', 19),
    ('faith', 0),
    ('population', 0),
    ('houseing', 0),
    ('citizen_slot', 3),
    ('power', 3),
    ('powered', True),
    ('maintenance', 7),
    ('amphitheater', True),
    ('archaeological_museum', False),
    ('art_museum', True),
    ('broadcast_center', True),
]
@pytest.mark.parametrize("resource, value", testdata)
def test_final_check(setup_district, resource, value):
    test_district = setup_district
    test_district.set_buildings()
    test_district.calculate_specialist_yield()
    assert getattr(test_district, resource) == value
