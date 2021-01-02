from backend.districts.dam import Dam
import pytest

@pytest.fixture(scope="function")
def setup_district():
    dist = Dam()
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
    ('housing', 3),
    ('citizen_slot', 0),
    ('power', 0),
    ('powered', False),
    ('maintenance', 0),
    ('building_list', None),
    ('hydroelectric_dam', False),
]
@pytest.mark.parametrize("resource, value", testdata)
def test_init(setup_district, resource, value):
    test_district = setup_district
    assert getattr(test_district, resource) == value

# Hydroelectric Dam
testdata = [
    ('maintenance', 1),
    ('housing', 3),
    ('power', 0),
    ('powered', True),
    ('maintenance', 1),
    ('building_list', [
        'hydroelectric_dam',
    ]),
    ('hydroelectric_dam', True),
]
@pytest.mark.parametrize("resource, value", testdata)
def test_hydroelectric_dam(setup_district, resource, value):
    test_district = setup_district
    test_district.set_buildings('hydroelectric_dam')
    test_district.calculate_specialist_yield()
    assert getattr(test_district, resource) == value

# Final check
testdata = [
    ('food', 0),
    ('production', 0),
    ('gold', 0),
    ('science', 0),
    ('culture', 0),
    ('faith', 0),
    ('population', 0),
    ('housing', 3),
    ('citizen_slot', 0),
    ('power', 0),
    ('powered', True),
    ('maintenance', 1),
    ('building_list', [
        'hydroelectric_dam',
    ]),
    ('hydroelectric_dam', True),
]
@pytest.mark.parametrize("resource, value", testdata)
def test_final_check(setup_district, resource, value):
    test_district = setup_district
    test_district.set_buildings()
    test_district.calculate_specialist_yield()
    assert getattr(test_district, resource) == value
