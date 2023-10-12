import csv
class CsvFile:
    """
    A class for converting a list of dictionaries (master_json) into a CSV file.

    Args:
        output_filepath (str): The path where the CSV file will be saved.

    Attributes:
        output_filepath (str): The path where the CSV file will be saved.

    Methods:
        Convert_tocsv(master_json: list): Converts the provided list of dictionaries into a CSV file.

    Example:
        # Create a CsvFile instance and convert a list of dictionaries to a CSV file
        csv_file = CsvFile("output_directory")
        data_to_convert = [
            {"Name": "John", "Age": 30, "City": "New York"},
            {"Name": "Alice", "Age": 25, "City": "Los Angeles"},
        ]
        csv_file.Convert_tocsv(data_to_convert)
    """

    def __init__(self, output_filepath: str):
        self.output_filepath = output_filepath

    def Convert_tocsv(self, master_json: list):
        """
        Converts a list of dictionaries into a CSV file.

        Args:
            master_json (list of dict): A list of dictionaries containing data to be converted to CSV.

        Returns:
            None

        The CSV file is created at the specified output_filepath with the header row
        containing the keys from the first dictionary in master_json.

        Example:
            csv_file = CsvFile("output_directory")
            data_to_convert = [
                {"Name": "John", "Age": 30, "City": "New York"},
                {"Name": "Alice", "Age": 25, "City": "Los Angeles"},
            ]
            csv_file.Convert_tocsv(data_to_convert)
        """
        master_json_fields = master_json[0].keys()
        with open(self.output_filepath + "\\output.csv", 'a', newline='') as csv_file:
            csv_writer_object = csv.DictWriter(csv_file, fieldnames=master_json_fields)
            csv_writer_object.writeheader()
            for csv_rec in master_json:
                csv_writer_object.writerow(csv_rec)
        print("CSV file has been created")
