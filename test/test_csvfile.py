import pytest
import sys
import csv
from src.csvfile import CsvFile

def test_Convert_tocsv():
    """
    Test the CsvFile class's Convert_tocsv method.

    This test checks the behavior of the Convert_tocsv method of the CsvFile class.
    It performs the following steps:

    1. Initializes the CsvFile class with an output file path.
    2. Provides a sample JSON data (master_json) for conversion to CSV.
    3. Calls the Convert_tocsv method to generate a CSV file.
    4. Reads and processes the generated CSV file.
    5. Reads and processes a comparison (expected) CSV file.
    6. Compares the content of the generated CSV file with the expected content.

    The test will pass if the content of the generated CSV file matches the expected content.

    :raises AssertionError: If the generated CSV content is not equal to the expected content.
    """
    output_filepath = str(sys.path[0]) + "\\data\\csv"
    filepath = CsvFile(output_filepath)
    master_json = [
        {'userId': 1, 'firstName': 'Krish', 'lastName': 'Lee', 'phoneNumber': '123456',
         'emailAddress': 'krish.lee@learningcontainer.com'},
        {'userId': 6, 'firstName': 'Anu', 'lastName': 'Lee', 'phoneNumber': '66666',
         'emailAddress': 'Anu.lee@learningcontainer.com'}
    ]
    filepath.Convert_tocsv(master_json)

    csv_file = output_filepath + "\\output.csv"
    csv_list = []
    with open(csv_file, mode='r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            csv_list.append(row)

    comp_csv_file = output_filepath + "\\comp_output.csv"
    comp_csv_list = []
    with open(comp_csv_file, mode='r') as comp_file:
        comp_csv_reader = csv.reader(comp_file)
        for comp_row in comp_csv_reader:
            comp_csv_list.append(comp_row)

    assert csv_list == comp_csv_list
