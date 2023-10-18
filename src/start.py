from checkinout import *
from jsonfile import *
from csvfile import *

def main():
    """
    The main function that orchestrates the conversion of JSON files to CSV.

    This function prompts the user to provide input and output folder paths for JSON and CSV files.
    It then performs the following steps:
    1. Checks the existence of input and output folders using the CheckInOutFolder class.
    2. Uses the JsonFile class to find JSON files, validate them, and check for matching headers.
    3. Creates a master JSON by merging data from valid JSON files.
    4. Converts the master JSON to a CSV file using the CsvFile class.

    Returns:
        None
    """
    input_filepath = input("Please enter the file path for input JSONs: ")
    output_filepath = input("Please enter the file path for output CSV: ")

    # Check if input and output folders exist
    checkInOut = CheckInOutFolder(input_filepath, output_filepath)
    checkInOut.check_filepaths()

    # Handle JSON files
    jsonfile = JsonFile(input_filepath)
    input_files = jsonfile.Find_inputfiles()
    valid_input_files = jsonfile.Check_json(input_files)
    valid_header_files = jsonfile.Check_header(valid_input_files)
    master_json = jsonfile.Create_masterjson(valid_header_files)

    # Convert master JSON to CSV
    csvfile = CsvFile(output_filepath)
    csvfile.Convert_tocsv(master_json)

if __name__ == "__main__":
    main()






