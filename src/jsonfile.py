import os
import json
import sys
from json import JSONDecodeError


class JsonFile:
        """
        A class for finding the valid JSON files in a specified input folder.

        Args:
            input_filepath (str): The path to the folder containing JSON files.

        Attributes:
            input_filepath (str): The path to the folder containing JSON files.

        Methods:
            Find_inputfiles() -> list: Finds all JSON files in the input folder.

            Check_json(input_files: list) -> list: Checks and returns valid JSON files from the input folder.

            Check_header(valid_input_files: list) -> list: Finds JSON files with matching headers in terms of keys.

            Create_masterjson(valid_header_files: list) -> list: Merges JSON data from valid files for CSV conversion.

        Example:
            # Create a JsonFile instance and perform JSON file operations
            json_handler = JsonFile("input_directory")

            # Find JSON files in the input folder
            input_files = json_handler.Find_inputfiles()

            # Check and obtain valid JSON files
            valid_input_files = json_handler.Check_json(input_files)

            # Check JSON files with matching headers
            valid_header_files = json_handler.Check_header(valid_input_files)

            # Create a master JSON by merging data from valid files
            master_json = json_handler.Create_masterjson(valid_header_files)
        """

        def __init__(self, input_filepath: str):
            self.input_filepath = input_filepath

        def Find_inputfiles(self) -> list:
            """
            Finds all JSON files in the input folder.

            Returns:
                list: A list of JSON file names in the input folder.
            """
            input_files = [file_name for file_name in os.listdir(self.input_filepath) if file_name.endswith(".json")]
            if input_files:
                return input_files
            else:
                print(f"No Json file found {self.input_filepath}")
                raise IndexError

        def Check_json(self, input_files: list) -> list:
            """
            Checks and returns name of valid JSON files from the input folder.

            Args:
                input_files (list): A list of JSON file names.

            Returns:
                list: A list of valid JSON file names.
            """
            valid_input_files = []
            for input_file in input_files:
                try:
                    with open(self.input_filepath + "\\" + input_file, 'r') as json_file:
                        json_data = json.load(json_file)
                        valid_input_files.append(input_file)
                except JSONDecodeError:
                    print(f"{input_file} is invalid")
            if valid_input_files:
                return valid_input_files
            else:
                print(f"No valid Json file found {self.input_filepath}")
                raise IndexError

        def Check_header(self, valid_input_files: list) -> list:
            """
            Finds JSON files with matching headers in terms of keys.

            Args:
                valid_input_files (list): A list of valid JSON file names.

            Returns:
                list: A list of valid JSON file names with matching headers.
            """
            json_fields = {}
            valid_header_files = []
            for valid_input_file in valid_input_files:
                with open(self.input_filepath + "\\" + valid_input_file, 'r') as json_file:
                    json_data = json.load(json_file)
                    if len(json_fields) == 0:
                        json_fields = json_data[0].keys()
                        valid_header_files.append(valid_input_file)
                    elif json_data[0].keys() == json_fields:
                        print(f"{valid_input_file} has the same keys as the first JSON")
                        valid_header_files.append(valid_input_file)
                    else:
                        print(
                            f"{valid_input_file} has different keys from other JSONs and cannot be converted to CSV with them")
            return valid_header_files

        def Create_masterjson(self, valid_header_files: list) -> list:
            """
            Merges JSON data from valid files for CSV conversion.

            Args:
                valid_header_files (list): A list of valid JSON file names with matching headers.

            Returns:
                list: A list containing merged JSON data from valid files.
            """
            master_json = []
            for valid_header_file in valid_header_files:
                with open(self.input_filepath + "\\" + valid_header_file, 'r') as json_file:
                    master_json.extend(json.load(json_file))
            return master_json
