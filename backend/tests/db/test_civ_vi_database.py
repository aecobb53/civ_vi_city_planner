from backend.db.civ_vi_database import CivVIDatabase
import pytest
import os

@pytest.fixture(scope="function")
def setup_database():
    db = CivVIDatabase()
    db.remove_from_cities_database({})
    return db

def test_read_empty_city_database(setup_database):
    test_db = setup_database
    data = test_db.find_in_cities_database({})
    for i in data:
        raise ValueError('there should not have been any data found')

def test_add_dict_to_city_database(setup_database):
    test_db = setup_database
    data_to_add = [{
        'example':'dct',
        'of':'information',
    }]
    test_db.write_to_cities_database(data_to_add)
    data = test_db.find_in_cities_database({})
    for i in data:
        assert i == data_to_add[0]

def test_remove_dict_from_city_database(setup_database):
    test_db = setup_database
    data_to_add = [{
        'example':'dct',
        'of':'information',
    }]
    test_db.write_to_cities_database(data_to_add)
    data = test_db.find_in_cities_database({})
    for i in data:
        assert i == data_to_add[0]
    test_db.remove_from_cities_database(data_to_add[0])
    data = test_db.find_in_cities_database({})
    for i in data:
        raise ValueError('there should not have been any data found')
