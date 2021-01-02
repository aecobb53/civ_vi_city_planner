from backend.districts.entertainment_complex import EntertainmentComplex
import pytest

@pytest.fixture(scope="function")
def setup_district():
    dist = EntertainmentComplex()
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
    ('arena', False),
    ('zoo', False),
    ('stadium', False),
]
@pytest.mark.parametrize("resource, value", testdata)
def test_init(setup_district, resource, value):
    test_district = setup_district
    assert getattr(test_district, resource) == value

# Arena
testdata = [
    ('amenities', 2),
    ('power', 0),
    ('powered', False),
    ('maintenance', 2),
    ('building_list', [
        'arena',
    ]),
    ('arena', True),
    ('zoo', False),
    ('stadium', False),
]
@pytest.mark.parametrize("resource, value", testdata)
def test_arena(setup_district, resource, value):
    test_district = setup_district
    test_district.set_buildings('arena')
    test_district.calculate_specialist_yield()
    assert getattr(test_district, resource) == value

# Zoo
testdata = [
    ('amenities', 3),
    ('power', 0),
    ('powered', False),
    ('maintenance', 4),
    ('building_list', [
        'arena',
        'zoo',
    ]),
    ('arena', True),
    ('zoo', True),
    ('stadium', False),
]
@pytest.mark.parametrize("resource, value", testdata)
def test_zoo(setup_district, resource, value):
    test_district = setup_district
    test_district.set_buildings('zoo')
    test_district.calculate_specialist_yield()
    assert getattr(test_district, resource) == value

# Unpowered Stadium
testdata = [
    ('amenities', 4),
    ('power', 0),
    ('powered', False),
    ('maintenance', 7),
    ('building_list', [
        'arena',
        'zoo',
        'stadium',
    ]),
    ('arena', True),
    ('zoo', True),
    ('stadium', True),
]
@pytest.mark.parametrize("resource, value", testdata)
def test_unpowered_stadium(setup_district, resource, value):
    test_district = setup_district
    test_district.set_buildings('stadium', False)
    test_district.calculate_specialist_yield()
    assert getattr(test_district, resource) == value

# Powered Stadium
testdata = [
    ('amenities', 6),
    ('power', 2),
    ('powered', True),
    ('maintenance', 7),
    ('building_list', [
        'arena',
        'zoo',
        'stadium',
    ]),
    ('arena', True),
    ('zoo', True),
    ('stadium', True),
]
@pytest.mark.parametrize("resource, value", testdata)
def test_unpowered_stadium(setup_district, resource, value):
    test_district = setup_district
    test_district.set_buildings('stadium', True)
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
    ('housing', 0),
    ('amenities', 6),
    ('citizen_slot', 0),
    ('power', 2),
    ('powered', True),
    ('maintenance', 7),
    ('building_list', [
        'arena',
        'zoo',
        'stadium',
    ]),
    ('arena', True),
    ('zoo', True),
    ('stadium', True),
]
@pytest.mark.parametrize("resource, value", testdata)
def test_final_check(setup_district, resource, value):
    test_district = setup_district
    test_district.set_buildings()
    test_district.calculate_specialist_yield()
    assert getattr(test_district, resource) == value
