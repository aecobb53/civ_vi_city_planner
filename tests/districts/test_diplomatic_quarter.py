from backend.districts.diplomatic_quarter import DiplomaticQuarter
import pytest

@pytest.fixture(scope="function")
def setup_district():
    dist = DiplomaticQuarter()
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
    ('consulate', False),
    ('chancery', False),
]
@pytest.mark.parametrize("resource, value", testdata)
def test_init(setup_district, resource, value):
    campus = setup_district
    assert getattr(campus, resource) == value

# Consulate
testdata = [
    ('power', 0),
    ('powered', False),
    ('maintenance', 2),
    ('building_list', [
        'consulate',
    ]),
    ('consulate', True),
    ('chancery', False),
]
@pytest.mark.parametrize("resource, value", testdata)
def test_consulate(setup_district, resource, value):
    campus = setup_district
    campus.set_buildings('consulate')
    campus.calculate_specialist_yield()
    assert getattr(campus, resource) == value

# Chancery
testdata = [
    ('power', 0),
    ('powered', False),
    ('maintenance', 4),
    ('building_list', [
        'consulate',
        'chancery',
    ]),
    ('consulate', True),
    ('chancery', True),
]
@pytest.mark.parametrize("resource, value", testdata)
def test_chancery(setup_district, resource, value):
    campus = setup_district
    campus.set_buildings('chancery')
    campus.calculate_specialist_yield()
    assert getattr(campus, resource) == value

# Final check
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
    ('maintenance', 4),
    ('building_list', [
        'consulate',
        'chancery',
    ]),
    ('consulate', True),
    ('chancery', True),
]
@pytest.mark.parametrize("resource, value", testdata)
def test_final_check(setup_district, resource, value):
    campus = setup_district
    campus.set_buildings()
    campus.calculate_specialist_yield()
    assert getattr(campus, resource) == value
