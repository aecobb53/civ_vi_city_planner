from backend.districts.government_plaza import GovernmentPlaza
import pytest

@pytest.fixture(scope="function")
def setup_district():
    dist = GovernmentPlaza()
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
    ('ancestral_hall', False),
    ('audience_chamber', False),
    ('warlords_throne', False),
    ('foreign_ministry', False),
    ('grand_masters_chapel', False),
    ('intelligence_agency', False),
    ('national_history_museum', False),
    ('royal_society', False),
    ('war_department', False),
]
@pytest.mark.parametrize("resource, value", testdata)
def test_init(setup_district, resource, value):
    test_district = setup_district
    assert getattr(test_district, resource) == value

# Tier I
# Ancestral Hall
testdata = [
    ('maintenance', 2),
    ('power', 0),
    ('powered', False),
    ('building_list', [
        'ancestral_hall',
    ]),
    ('ancestral_hall', True),
    ('audience_chamber', False),
    ('warlords_throne', False),
]
@pytest.mark.parametrize("resource, value", testdata)
def test_ancestral_hall(setup_district, resource, value):
    test_district = setup_district
    test_district.set_buildings('ancestral_hall')
    test_district.calculate_specialist_yield()
    assert getattr(test_district, resource) == value

# Audience Chamber
testdata = [
    ('maintenance', 2),
    ('power', 0),
    ('powered', False),
    ('building_list', [
        'audience_chamber',
    ]),
    ('ancestral_hall', False),
    ('audience_chamber', True),
    ('warlords_throne', False),
]
@pytest.mark.parametrize("resource, value", testdata)
def test_audience_chamber(setup_district, resource, value):
    test_district = setup_district
    test_district.set_buildings('audience_chamber')
    test_district.calculate_specialist_yield()
    assert getattr(test_district, resource) == value

# Warlords Throne
testdata = [
    ('maintenance', 2),
    ('power', 0),
    ('powered', False),
    ('building_list', [
        'warlords_throne',
    ]),
    ('ancestral_hall', False),
    ('audience_chamber', False),
    ('warlords_throne', True),
]
@pytest.mark.parametrize("resource, value", testdata)
def test_warlords_throne(setup_district, resource, value):
    test_district = setup_district
    test_district.set_buildings('warlords_throne')
    test_district.calculate_specialist_yield()
    assert getattr(test_district, resource) == value

# Tier II
# Foreign Ministry
testdata = [
    ('maintenance', 4),
    ('power', 0),
    ('powered', False),
    ('building_list', [
        'warlords_throne',
        'foreign_ministry',
    ]),
    ('foreign_ministry', True),
    ('grand_masters_chapel', False),
    ('intelligence_agency', False),
]
@pytest.mark.parametrize("resource, value", testdata)
def test_foreign_ministry(setup_district, resource, value):
    test_district = setup_district
    test_district.set_buildings('foreign_ministry')
    test_district.calculate_specialist_yield()
    assert getattr(test_district, resource) == value

# Grand Masters Chapel
testdata = [
    ('maintenance', 4),
    ('faith', 5),
    ('power', 0),
    ('powered', False),
    ('building_list', [
        'warlords_throne',
        'grand_masters_chapel',
    ]),
    ('foreign_ministry', False),
    ('grand_masters_chapel', True),
    ('intelligence_agency', False),
]
@pytest.mark.parametrize("resource, value", testdata)
def test_grand_masters_chapel(setup_district, resource, value):
    test_district = setup_district
    test_district.set_buildings('grand_masters_chapel')
    test_district.calculate_specialist_yield()
    assert getattr(test_district, resource) == value

# Intelligence Agency
testdata = [
    ('maintenance', 4),
    ('power', 0),
    ('powered', False),
    ('building_list', [
        'warlords_throne',
        'intelligence_agency',
    ]),
    ('foreign_ministry', False),
    ('grand_masters_chapel', False),
    ('intelligence_agency', True),
]
@pytest.mark.parametrize("resource, value", testdata)
def test_intelligence_agency(setup_district, resource, value):
    test_district = setup_district
    test_district.set_buildings('intelligence_agency')
    test_district.calculate_specialist_yield()
    assert getattr(test_district, resource) == value

# Tier III
# National History Museum
testdata = [
    ('maintenance', 7),
    ('power', 0),
    ('powered', False),
    ('building_list', [
        'warlords_throne',
        'intelligence_agency',
        'national_history_museum',
    ]),
    ('national_history_museum', True),
    ('royal_society', False),
    ('war_department', False),
]
@pytest.mark.parametrize("resource, value", testdata)
def test_national_history_museum(setup_district, resource, value):
    test_district = setup_district
    test_district.set_buildings('national_history_museum')
    test_district.calculate_specialist_yield()
    assert getattr(test_district, resource) == value

# Royal Society
testdata = [
    ('maintenance', 7),
    ('power', 0),
    ('powered', False),
    ('building_list', [
        'warlords_throne',
        'intelligence_agency',
        'royal_society',
    ]),
    ('national_history_museum', False),
    ('royal_society', True),
    ('war_department', False),
]
@pytest.mark.parametrize("resource, value", testdata)
def test_royal_society(setup_district, resource, value):
    test_district = setup_district
    test_district.set_buildings('royal_society')
    test_district.calculate_specialist_yield()
    assert getattr(test_district, resource) == value

# War Department
testdata = [
    ('maintenance', 7),
    ('power', 0),
    ('powered', False),
    ('building_list', [
        'warlords_throne',
        'intelligence_agency',
        'war_department',
    ]),
    ('national_history_museum', False),
    ('royal_society', False),
    ('war_department', True),
]
@pytest.mark.parametrize("resource, value", testdata)
def test_war_department(setup_district, resource, value):
    test_district = setup_district
    test_district.set_buildings('war_department')
    test_district.calculate_specialist_yield()
    assert getattr(test_district, resource) == value


# # Library
# testdata = [
#     ('science', 4),
#     ('housing', 0),
#     ('citizen_slot', 1),
#     ('power', 0),
#     ('powered', False),
#     ('maintenance', 2),
#     ('building_list', [
#         'ancestral_hall',
#         'audience_chamber',
#         'warlords_throne',
#         'foreign_ministry',
#         'grand_masters_chapel',
#         'intelligence_agency',
#         'national_history_museum',
#         'royal_society',
#         'war_department',
#     ]),
#     ('ancestral_hall', None),
#     ('audience_chamber', None),
#     ('warlords_throne', None),
#     ('foreign_ministry', None),
#     ('grand_masters_chapel', None),
#     ('intelligence_agency', None),
#     ('national_history_museum', None),
#     ('royal_society', None),
#     ('war_department', None),
# ]
# @pytest.mark.parametrize("resource, value", testdata)
# def test_library(setup_district, resource, value):
#     test_district = setup_district
#     test_district.set_buildings.set_buildings('library')
#     test_district.calculate_specialist_yield()
#     assert getattr(test_district, resource) == value

# # University
# testdata = [
#     ('science', 10),
#     ('housing', 1),
#     ('citizen_slot', 2),
#     ('power', 0),
#     ('powered', False),
#     ('maintenance', 4),
#     ('building_list', [
#         'library',
#         'university',
#     ]),
#     ('library', True),
#     ('university', True),
#     ('research_lab', False),
# ]
# @pytest.mark.parametrize("resource, value", testdata)
# def test_university(setup_district, resource, value):
#     test_district = setup_district
#     test_district.set_buildings.set_buildings('university')
#     test_district.calculate_specialist_yield()
#     assert getattr(test_district, resource) == value

# # Unpowered Research Lab
# testdata = [
#     ('science', 15),
#     ('housing', 1),
#     ('citizen_slot', 3),
#     ('power', 0),
#     ('powered', False),
#     ('maintenance', 7),
#     ('building_list', [
#         'library',
#         'university',
#         'research_lab',
#     ]),
#     ('library', True),
#     ('university', True),
#     ('research_lab', True),
# ]
# @pytest.mark.parametrize("resource, value", testdata)
# def test_unpowered_research_lab(setup_district, resource, value):
#     test_district = setup_district
#     test_district.set_buildings.set_buildings('research_lab', False)
#     test_district.calculate_specialist_yield()
#     assert getattr(test_district, resource) == value

# # Powered Research Lab
# testdata = [
#     ('science', 23),
#     ('housing', 1),
#     ('citizen_slot', 3),
#     ('power', 3),
#     ('powered', True),
#     ('maintenance', 7),
#     ('building_list', [
#         'library',
#         'university',
#         'research_lab',
#     ]),
#     ('library', True),
#     ('university', True),
#     ('research_lab', True),
# ]
# @pytest.mark.parametrize("resource, value", testdata)
# def test_powered_research_lab(setup_district, resource, value):
#     test_district = setup_district
#     test_district.set_buildings.set_buildings('research_lab', True)
#     test_district.calculate_specialist_yield()
#     assert getattr(test_district, resource) == value

# # Final check
# testdata = [
#     ('food', 0),
#     ('production', 0),
#     ('gold', 0),
#     ('science', 23),
#     ('culture', 0),
#     ('faith', 0),
#     ('population', 0),
#     ('housing', 1),
#     ('citizen_slot', 3),
#     ('power', 3),
#     ('powered', True),
#     ('maintenance', 7),
#     ('building_list', [
#         'library',
#         'university',
#         'research_lab',
#     ]),
#     ('library', True),
#     ('university', True),
#     ('research_lab', True),
# ]
# @pytest.mark.parametrize("resource, value", testdata)
# def test_final_check(setup_district, resource, value):
#     test_district = setup_district
#     test_district.set_buildings.set_buildings()
#     test_district.calculate_specialist_yield()
#     assert getattr(test_district, resource) == value
