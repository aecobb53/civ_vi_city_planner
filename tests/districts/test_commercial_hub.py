from backend.districts.commercial_hub import CommercialHub
import pytest

@pytest.fixture(scope="function")
def setup_district():
    dist = CommercialHub()
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
    ('market', False),
    ('bank', False),
    ('stock_exchange', False),
]
@pytest.mark.parametrize("resource, value", testdata)
def test_init(setup_district, resource, value):
    campus = setup_district
    assert getattr(campus, resource) == value

# Market
testdata = [
    ('gold', 7),
    ('citizen_slot', 1),
    ('power', 0),
    ('powered', False),
    ('building_list', [
        'market',
    ]),
    ('market', True),
    ('bank', False),
    ('stock_exchange', False),
]
@pytest.mark.parametrize("resource, value", testdata)
def test_market(setup_district, resource, value):
    campus = setup_district
    campus.set_buildings('market')
    campus.calculate_specialist_yield()
    assert getattr(campus, resource) == value

# Bank
testdata = [
    ('gold', 16),
    ('citizen_slot', 2),
    ('power', 0),
    ('powered', False),
    ('building_list', [
        'market',
        'bank',
    ]),
    ('market', True),
    ('bank', True),
    ('stock_exchange', False),
]
@pytest.mark.parametrize("resource, value", testdata)
def test_bank(setup_district, resource, value):
    campus = setup_district
    campus.set_buildings('bank')
    campus.calculate_specialist_yield()
    assert getattr(campus, resource) == value

# Unpowered Stock Exchange
testdata = [
    ('gold', 24),
    ('citizen_slot', 3),
    ('power', 0),
    ('powered', False),
    ('building_list', [
        'market',
        'bank',
        'stock_exchange',
    ]),
    ('market', True),
    ('bank', True),
    ('stock_exchange', True),
]
@pytest.mark.parametrize("resource, value", testdata)
def test_unpowered_stock_exchange(setup_district, resource, value):
    campus = setup_district
    campus.set_buildings('stock_exchange', False)
    campus.calculate_specialist_yield()
    assert getattr(campus, resource) == value

# Powered Stock Exchange
testdata = [
    ('gold', 37),
    ('citizen_slot', 3),
    ('power', 3),
    ('powered', True),
    ('building_list', [
        'market',
        'bank',
        'stock_exchange',
    ]),
    ('market', True),
    ('bank', True),
    ('stock_exchange', True),
]
@pytest.mark.parametrize("resource, value", testdata)
def test_powered_stock_exchange(setup_district, resource, value):
    campus = setup_district
    campus.set_buildings('stock_exchange', True)
    campus.calculate_specialist_yield()
    assert getattr(campus, resource) == value

# Final check
testdata = [
    ('food', 0),
    ('production', 0),
    ('gold', 37),
    ('science', 0),
    ('culture', 0),
    ('faith', 0),
    ('population', 0),
    ('houseing', 0),
    ('citizen_slot', 3),
    ('power', 3),
    ('powered', True),
    ('maintenance', 0),
    ('building_list', [
        'market',
        'bank',
        'stock_exchange',
    ]),
    ('market', True),
    ('bank', True),
    ('stock_exchange', True),
]
@pytest.mark.parametrize("resource, value", testdata)
def test_final_check(setup_district, resource, value):
    campus = setup_district
    campus.set_buildings()
    campus.calculate_specialist_yield()
    assert getattr(campus, resource) == value
