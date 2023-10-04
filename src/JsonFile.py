import os
import json
from json import JSONDecodeError

class JsonFile:
    def __init__(self,input_filepath):
        self.input_filepath = input_filepath

    def Find_inputfiles(self)-> list: #Find JSONs in the input folder
        input_files = [file_name for file_name in os.listdir(self.input_filepath) if file_name.endswith(".json")]
        return input_files

    def Check_json(self,input_files)-> list:  # Find JSONs in the input folder which are valid
        valid_input_files = []
        for input_file in input_files:
            try:
                with open(self.input_filepath + "\\"+input_file, 'r') as json_file:
                    json_data = json.load(json_file)
                    valid_input_files.append(input_file)
            except JSONDecodeError:
                print(f"{input_file} is invalid")
        return valid_input_files

    def Check_header(self,valid_input_files)-> list: # Find the JSONs in the input folder with matching headers
            json_fields = {}
            valid_header_files = []
            for valid_input_file in valid_input_files:
                with open(self.input_filepath + "\\" + valid_input_file, 'r') as json_file:
                     json_data = json.load(json_file)
                     if len(json_fields) == 0:
                         json_fields = json_data[0].keys()
                         valid_header_files.append(valid_input_file)
                     elif json_data[0].keys() == json_fields:
                         print(f"{valid_input_file} has same keys as first jsons")
                         valid_header_files.append(valid_input_file)
                     else:
                         print(f"{valid_input_file} has different keys from other jsons, can't be converted to csv with other jsons")
            return valid_header_files

    def Create_masterjson(self,valid_header_files)-> list: # Merge JSON data for converting to csv
        master_json = []
        for valid_header_file in valid_header_files:
            with open(self.input_filepath + "\\" + valid_header_file, 'r') as json_file:
                master_json.extend(json.load(json_file))
        return master_json