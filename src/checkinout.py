import sys
import os

class CheckInOutFolder:
    """
    A class for checking the existence of input and output file paths.

    This class provides methods to check if the specified input and output file
    paths exist. If a file path does not exist, it raises an OSError and provides
    an error message.

    :param input_filepath: The path to the input file.
    :type input_filepath: str
    :param output_filepath: The path to the output file.
    :type output_filepath: str
    """

    def __init__(self, input_filepath: str, output_filepath: str):
        """
        Initialize a new CheckInOutFolder instance with input and output file paths.

        :param input_filepath: The path to the input file.
        :type input_filepath: str
        :param output_filepath: The path to the output file.
        :type output_filepath: str
        """
        self.input_filepath = input_filepath
        self.output_filepath = output_filepath

    def check_filepaths(self):
        """
        Check the existence of input and output file paths.

        This method checks if the specified input and output file paths exist.
        If either file path does not exist, it raises an OSError and provides
        an error message.
        """
        if not os.path.exists(self.input_filepath):
            print(f"Unable to open {self.input_filepath}")
            raise OSError(f"Unable to open: {self.input_filepath}")

        if not os.path.exists(self.output_filepath):
            print(f"Unable to open {self.output_filepath}")
            raise OSError(f"Unable to open: {self.output_filepath}")



