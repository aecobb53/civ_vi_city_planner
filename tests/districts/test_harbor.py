from backend.districts.harbor import Harbor
import pytest

@pytest.fixture(scope="function")
def setup_district():
    dist = Harbor()
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
    ('maintenance', 0),
    ('building_list', None),
    ('lighthouse', False),
    ('shipyard', False),
    ('seaport', False),
]
@pytest.mark.parametrize("resource, value", testdata)
def test_init(setup_district, resource, value):
    campus = setup_district
    assert getattr(campus, resource) == value

# Lighthouse
testdata = [
    ('food', 2),
    ('gold', 3),
    ('houseing', 1),
    ('citizen_slot', 1),
    ('power', 0),
    ('powered', False),
    ('maintenance', 0),
    ('building_list', [
        'lighthouse',
    ]),
    ('lighthouse', True),
    ('shipyard', False),
    ('seaport', False),
]
@pytest.mark.parametrize("resource, value", testdata)
def test_lighthouse(setup_district, resource, value):
    campus = setup_district
    campus.set_buildings('lighthouse')
    campus.calculate_specialist_yield()
    assert getattr(campus, resource) == value

# Shipyard
testdata = [
    ('food', 3),
    ('gold', 5),
    ('houseing', 1),
    ('citizen_slot', 2),
    ('power', 0),
    ('powered', False),
    ('maintenance', 2),
    ('building_list', [
        'lighthouse',
        'shipyard',
    ]),
    ('lighthouse', True),
    ('shipyard', True),
    ('seaport', False),
]
@pytest.mark.parametrize("resource, value", testdata)
def test_shipyard(setup_district, resource, value):
    campus = setup_district
    campus.set_buildings('shipyard')
    campus.calculate_specialist_yield()
    assert getattr(campus, resource) == value

# Seaport
testdata = [
    ('food', 9),
    ('gold', 9),
    ('houseing', 2),
    ('citizen_slot', 3),
    ('power', 0),
    ('powered', False),
    ('maintenance', 2),
    ('building_list', [
        'lighthouse',
        'shipyard',
        'seaport',
    ]),
    ('lighthouse', True),
    ('shipyard', True),
    ('seaport', True),
]
@pytest.mark.parametrize("resource, value", testdata)
def test_seaport(setup_district, resource, value):
    campus = setup_district
    campus.set_buildings('seaport', False)
    campus.calculate_specialist_yield()
    assert getattr(campus, resource) == value

# Final check
testdata = [
    ('food', 9),
    ('production', 0),
    ('gold', 9),
    ('science', 0),
    ('culture', 0),
    ('faith', 0),
    ('population', 0),
    ('houseing', 2),
    ('citizen_slot', 3),
    ('power', 0),
    ('powered', False),
    ('maintenance', 2),
    ('building_list', [
        'lighthouse',
        'shipyard',
        'seaport',
    ]),
    ('lighthouse', True),
    ('shipyard', True),
    ('seaport', True),
]
@pytest.mark.parametrize("resource, value", testdata)
def test_final_check(setup_district, resource, value):
    campus = setup_district
    campus.set_buildings()
    campus.calculate_specialist_yield()
    assert getattr(campus, resource) == value
