from backend.db.pymongodb_database import PymongoDBDatabase
import pytest
import os

@pytest.fixture(scope="function")
def setup_database():
    db = PymongoDBDatabase('civ_vi_' + os.getenv('MONGOENV'), 'test-cities')
    db.remove_from_database({})
    return db

def test_read_empty_database(setup_database):
    test_db = setup_database
    data = test_db.find_in_database({})
    for i in data:
        raise ValueError('there should not have been any data found')

def test_add_dict_to_database(setup_database):
    test_db = setup_database
    data_to_add = [{
        'example':'dct',
        'of':'information',
    }]
    test_db.write_to_database(data_to_add)
    data = test_db.find_in_database({})
    for i in data:
        assert i == data_to_add[0]

def test_remove_dict_from_database(setup_database):
    test_db = setup_database
    data_to_add = [{
        'example':'dct',
        'of':'information',
    }]
    test_db.write_to_database(data_to_add)
    data = test_db.find_in_database({})
    for i in data:
        assert i == data_to_add[0]
    test_db.remove_from_database(data_to_add[0])
    data = test_db.find_in_database({})
    for i in data:
        raise ValueError('there should not have been any data found')
