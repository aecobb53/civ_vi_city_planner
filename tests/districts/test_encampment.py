from backend.districts.encampment import Encampment
import pytest

@pytest.fixture(scope="function")
def setup_district():
    dist = Encampment()
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
    ('barracks', False),
    ('stable', False),
    ('armory', False),
    ('military_academy', False),
]
@pytest.mark.parametrize("resource, value", testdata)
def test_init(setup_district, resource, value):
    test_district = setup_district
    assert getattr(test_district, resource) == value

# Barracks
testdata = [
    ('production', 2),
    ('gold', 2),
    ('houseing', 1),
    ('citizen_slot', 1),
    ('power', 0),
    ('powered', False),
    ('maintenance', 2),
    ('barracks', True),
    ('stable', False),
    ('armory', False),
    ('military_academy', False),
]
@pytest.mark.parametrize("resource, value", testdata)
def test_barracks(setup_district, resource, value):
    test_district = setup_district
    test_district.set_buildings('barracks')
    test_district.calculate_specialist_yield()
    assert getattr(test_district, resource) == value

# Stable
testdata = [
    ('production', 2),
    ('gold', 2),
    ('houseing', 1),
    ('citizen_slot', 1),
    ('power', 0),
    ('powered', False),
    ('maintenance', 2),
    ('barracks', False),
    ('stable', True),
    ('armory', False),
    ('military_academy', False),
]
@pytest.mark.parametrize("resource, value", testdata)
def test_stable(setup_district, resource, value):
    test_district = setup_district
    test_district.set_buildings('stable')
    test_district.calculate_specialist_yield()
    assert getattr(test_district, resource) == value

# Armory
testdata = [
    ('production', 6),
    ('gold', 4),
    ('houseing', 1),
    ('citizen_slot', 2),
    ('power', 0),
    ('powered', False),
    ('maintenance', 4),
    ('barracks', False),
    ('stable', True),
    ('armory', True),
    ('military_academy', False),
]
@pytest.mark.parametrize("resource, value", testdata)
def test_armory(setup_district, resource, value):
    test_district = setup_district
    test_district.set_buildings('armory')
    test_district.calculate_specialist_yield()
    assert getattr(test_district, resource) == value

# Military Academy
testdata = [
    ('production', 13),
    ('gold', 6),
    ('houseing', 2),
    ('citizen_slot', 3),
    ('power', 0),
    ('powered', False),
    ('maintenance', 6),
    ('barracks', False),
    ('stable', True),
    ('armory', True),
    ('military_academy', True),
]
@pytest.mark.parametrize("resource, value", testdata)
def test_military_academy(setup_district, resource, value):
    test_district = setup_district
    test_district.set_buildings('military_academy', False)
    test_district.calculate_specialist_yield()
    assert getattr(test_district, resource) == value

# Final check
testdata = [
    ('food', 0),
    ('production', 13),
    ('gold', 6),
    ('science', 0),
    ('culture', 0),
    ('faith', 0),
    ('population', 0),
    ('houseing', 2),
    ('citizen_slot', 3),
    ('power', 0),
    ('powered', False),
    ('maintenance', 6),
    ('barracks', False),
    ('stable', True),
    ('armory', True),
    ('military_academy', True),
]
@pytest.mark.parametrize("resource, value", testdata)
def test_final_check(setup_district, resource, value):
    test_district = setup_district
    test_district.set_buildings()
    test_district.calculate_specialist_yield()
    assert getattr(test_district, resource) == value
