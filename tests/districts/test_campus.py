from backend.districts.campus import Campus
import pytest

@pytest.fixture(scope="function")
def setup_district():
    dist = Campus()
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
    ('library', False),
    ('university', False),
    ('research_lab', False),
]
@pytest.mark.parametrize("resource, value", testdata)
def test_init(setup_district, resource, value):
    campus = setup_district
    assert getattr(campus, resource) == value

# Library
testdata = [
    ('science', 4),
    ('houseing', 0),
    ('citizen_slot', 1),
    ('power', 0),
    ('powered', False),
    ('maintenance', 2),
    ('building_list', ['library']),
    ('library', True),
    ('university', False),
    ('research_lab', False),
]
@pytest.mark.parametrize("resource, value", testdata)
def test_library(setup_district, resource, value):
    campus = setup_district
    campus.set_buildings('library')
    campus.calculate_specialist_yield()
    assert getattr(campus, resource) == value

# University
testdata = [
    ('science', 10),
    ('houseing', 1),
    ('citizen_slot', 2),
    ('power', 0),
    ('powered', False),
    ('maintenance', 4),
    ('library', True),
    ('university', True),
    ('research_lab', False),
]
@pytest.mark.parametrize("resource, value", testdata)
def test_university(setup_district, resource, value):
    campus = setup_district
    campus.set_buildings('university')
    campus.calculate_specialist_yield()
    assert getattr(campus, resource) == value

# Unpowered Research Lab
testdata = [
    ('science', 15),
    ('houseing', 1),
    ('citizen_slot', 3),
    ('power', 0),
    ('powered', False),
    ('maintenance', 7),
    ('library', True),
    ('university', True),
    ('research_lab', True),
]
@pytest.mark.parametrize("resource, value", testdata)
def test_unpowered_research_lab(setup_district, resource, value):
    campus = setup_district
    campus.set_buildings('research_lab', False)
    campus.calculate_specialist_yield()
    assert getattr(campus, resource) == value

# Powered Research Lab
testdata = [
    ('science', 23),
    ('houseing', 1),
    ('citizen_slot', 3),
    ('power', 3),
    ('powered', True),
    ('maintenance', 7),
    ('library', True),
    ('university', True),
    ('research_lab', True),
]
@pytest.mark.parametrize("resource, value", testdata)
def test_powered_research_lab(setup_district, resource, value):
    campus = setup_district
    campus.set_buildings('research_lab', True)
    campus.calculate_specialist_yield()
    assert getattr(campus, resource) == value

# Final check
testdata = [
    ('food', 0),
    ('production', 0),
    ('gold', 0),
    ('science', 23),
    ('culture', 0),
    ('faith', 0),
    ('population', 0),
    ('houseing', 1),
    ('citizen_slot', 3),
    ('power', 3),
    ('powered', True),
    ('maintenance', 7),
    ('library', True),
    ('university', True),
    ('research_lab', True),
]
@pytest.mark.parametrize("resource, value", testdata)
def test_final_check(setup_district, resource, value):
    campus = setup_district
    campus.set_buildings()
    campus.calculate_specialist_yield()
    assert getattr(campus, resource) == value
