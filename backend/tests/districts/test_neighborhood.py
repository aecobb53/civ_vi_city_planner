from backend.districts.neighborhood import Neighborhood
import pytest

@pytest.fixture(scope="function")
def setup_district():
    dist = Neighborhood()
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
    ('amenities', 0),
    ('citizen_slot', 0),
    ('power', 0),
    ('powered', False),
    ('maintenance', 0),
    ('building_list', None),
    ('food_market', False),
    ('shopping_mall', False),
]
@pytest.mark.parametrize("resource, value", testdata)
def test_init(setup_district, resource, value):
    test_district = setup_district
    assert getattr(test_district, resource) == value

# Unpowered Food Market
testdata = [
    ('food', 4),
    ('power', 0),
    ('powered', False),
    ('maintenance', 1),
    ('building_list', [
        'food_market',
    ]),
    ('food_market', True),
    ('shopping_mall', False),
]
@pytest.mark.parametrize("resource, value", testdata)
def test_unpowered_food_market(setup_district, resource, value):
    test_district = setup_district
    test_district.set_buildings('food_market', False)
    test_district.calculate_specialist_yield()
    assert getattr(test_district, resource) == value

# Powered Food Market
testdata = [
    ('food', 6),
    ('power', 1),
    ('powered', True),
    ('maintenance', 1),
    ('building_list', [
        'food_market',
    ]),
    ('food_market', True),
    ('shopping_mall', False),
]
@pytest.mark.parametrize("resource, value", testdata)
def test_unpowered_food_market(setup_district, resource, value):
    test_district = setup_district
    test_district.set_buildings('food_market', True)
    test_district.calculate_specialist_yield()
    assert getattr(test_district, resource) == value

# Unpowered Shopping Mall
testdata = [
    ('gold', 2),
    ('amenities', 1),
    ('power', 0),
    ('powered', False),
    ('maintenance', 1),
    ('building_list', [
        'shopping_mall',
    ]),
    ('food_market', False),
    ('shopping_mall', True),
]
@pytest.mark.parametrize("resource, value", testdata)
def test_unpowered_food_market(setup_district, resource, value):
    test_district = setup_district
    test_district.set_buildings('shopping_mall', False)
    test_district.calculate_specialist_yield()
    assert getattr(test_district, resource) == value

# Powered Shopping Mall
testdata = [
    ('gold', 4),
    ('amenities', 2),
    ('power', 1),
    ('powered', True),
    ('maintenance', 1),
    ('building_list', [
        'shopping_mall',
    ]),
    ('food_market', False),
    ('shopping_mall', True),
]
@pytest.mark.parametrize("resource, value", testdata)
def test_powered_food_market(setup_district, resource, value):
    test_district = setup_district
    test_district.set_buildings('shopping_mall', True)
    test_district.calculate_specialist_yield()
    assert getattr(test_district, resource) == value

# Final check
testdata = [
    ('food', 0),
    ('production', 0),
    ('gold', 4),
    ('science', 0),
    ('culture', 0),
    ('faith', 0),
    ('population', 0),
    ('housing', 0),
    ('amenities', 2),
    ('citizen_slot', 0),
    ('power', 1),
    ('powered', True),
    ('maintenance', 1),
    ('building_list', [
        'shopping_mall',
    ]),
    ('food_market', False),
    ('shopping_mall', True),
]
@pytest.mark.parametrize("resource, value", testdata)
def test_final_check(setup_district, resource, value):
    test_district = setup_district
    test_district.set_buildings()
    test_district.calculate_specialist_yield()
    assert getattr(test_district, resource) == value
