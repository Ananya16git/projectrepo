import os
import sys
class CheckInOutFolder:
    """
    A class for checking the existence of input and output folders.

    Args:
        input_filepath (str): The path to the input JSON folder.
        output_filepath (str): The path to the output CSV folder.

    Attributes:
        input_filepath (str): The path to the input JSON folder.
        output_filepath (str): The path to the output CSV folder.

    Methods:
        Check_filepath(): Checks if the input and output folders exist.

    Example:
        # Create a CheckInOutFolder instance and check folder existence
        folder_checker = CheckInOutFolder("input_directory", "output_directory")
        folder_checker.Check_filepath()
    """
    def __init__(self, input_filepath: str, output_filepath: str):
        self.input_filepath = input_filepath
        self.output_filepath = output_filepath

    def Check_filepath(self):
        """
        Checks if the input and output folders exist.

        If the input folder exists, it sets 'input_filepath_found' to True and prints a success message.
        If the input folder does not exist, it sets 'input_filepath_found' to False and prints an error message,
        prompting the user to rerun the code with the correct path.

        If the output folder exists, it sets 'output_filepath_found' to True and prints a success message.
        If the output folder does not exist, it sets 'output_filepath_found' to False and prints an error message,
        prompting the user to rerun the code with the correct path.

        Returns:
            None
        """
        if os.path.exists(self.input_filepath):
            input_filepath_found = True
            print("Input JSON folder found")
        else:
            input_filepath_found = False
            print("Input JSON folder is not found, rerun the code and enter the correct path")
            sys.exit()

        if os.path.exists(self.output_filepath):
            output_filepath_found = True
            print("Output CSV folder is found")
        else:
            output_filepath_found = False
            print("Output folder is not found, rerun the code and enter the correct path")
            sys.exit()
