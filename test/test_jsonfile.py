import pytest
import sys
from src.jsonfile import JsonFile

def test_jsonfile_operations():
    """
    Test suite for JsonFile class operations.

    This test suite covers various test cases related to the JsonFile class, including
    finding input JSON files, checking for valid JSON files, checking headers,
    creating a master JSON, and more. Each test case is documented separately.

    Test Cases:
    1. test_Find_inputfiles_nojson_found - Test behavior when no JSON files are found.
    2. test_Find_inputfiles_json_found - Test behavior when JSON files are found.
    3. test_Check_json_novalidjson_found - Test behavior when no valid JSON files are found.
    4. test_Check_json_validjson_found - Test behavior when valid JSON files are found.
    5. test_Check_header_header_found - Test behavior when a valid header file is found.
    6. test_Create_masterjson_validmaster - Test behavior when creating a valid master JSON.

    Each test case is documented with its purpose, steps, and expected behavior.
    """
def test_Find_inputfiles_nojson_found():
    with pytest.raises(IndexError):
        input_filepath = str(sys.path[0]) + "\\data\\empty_json"
        filepath = JsonFile(input_filepath)
        filepath.Find_inputfiles()

def test_Find_inputfiles_json_found():
    input_filepath = str(sys.path[0]) + "\\data\\json"
    filepath = JsonFile(input_filepath)
    json_files = filepath.Find_inputfiles()
    assert json_files == ['userjson1.json','userjson2.json','userjson3.json','userjson4.json','userjson5.json','userjson6.json']

def test_Check_json_novalidjson_found():
    with pytest.raises(IndexError):
        input_filepath = str(sys.path[0]) + "\\data\\invalid_json"
        filepath = JsonFile(input_filepath)
        json_files = ['userjson3.json', 'userjson4.json', 'userjson6.json']
        filepath.Check_json(json_files)

def test_Check_json_validjson_found():
    input_filepath = str(sys.path[0]) + "\\data\\json"
    filepath = JsonFile(input_filepath)
    json_files = ['userjson1.json','userjson2.json','userjson3.json','userjson4.json','userjson5.json','userjson6.json']
    valid_input_files = filepath.Check_json(json_files)
    assert valid_input_files == ['userjson1.json','userjson2.json','userjson5.json']

def test_Check_header_header_found():
    input_filepath = str(sys.path[0]) + "\\data\\json"
    filepath = JsonFile(input_filepath)
    valid_input_files = ['userjson1.json', 'userjson2.json', 'userjson5.json']
    valid_header = filepath.Check_header(valid_input_files)
    assert valid_header == ['userjson1.json', 'userjson2.json']

def test_Create_masterjson_validmaster():
    input_filepath = str(sys.path[0]) + "\\data\\master_json"
    filepath = JsonFile(input_filepath)
    valid_input_files = ['userjson1.json', 'userjson2.json']
    master_json = filepath.Create_masterjson(valid_input_files)
    assert master_json == [{'userId': 1, 'firstName': 'Krish', 'lastName': 'Lee', 'phoneNumber': '123456', 'emailAddress': 'krish.lee@learningcontainer.com'},
                           {'userId': 6, 'firstName': 'Anu', 'lastName': 'Lee', 'phoneNumber': '66666', 'emailAddress': 'Anu.lee@learningcontainer.com'}]
