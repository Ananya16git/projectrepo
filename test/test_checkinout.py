import pytest
import sys
from src.checkinout import CheckInOutFolder

def test_Check_filepath_negative_test():
    """
    Test the CheckInOutFolder class with incorrect input and output file paths.

    This test checks the behavior of the CheckInOutFolder class when provided
    with incorrect input and output file paths. It uses the pytest framework to
    verify that an OSError is raised during the check_filepaths method.

    """

    checkinout = CheckInOutFolder("dummy", "dummy")
    with pytest.raises(OSError):
        checkinout.check_filepaths()

def test_Check_filepath_correctin_wrongout():
    """
    Test the CheckInOutFolder class with correct input and incorrect output file paths.

    This test checks the behavior of the CheckInOutFolder class when provided
    with a correct input file path and an incorrect output file path. It uses the
    pytest framework to verify that an OSError is raised during the check_filepaths method.

    """

    input_file_path = str(sys.path[0]) + "\\data\\json"
    checkinout = CheckInOutFolder(str(input_file_path), "dummy")
    with pytest.raises(OSError):
        checkinout.check_filepaths()

def test_Check_filepath_wrongin_correctout():
    """
    Test the CheckInOutFolder class with incorrect input and correct output file paths.

    This test checks the behavior of the CheckInOutFolder class when provided
    with an incorrect input file path and a correct output file path. It uses the
    pytest framework to verify that an OSError is raised during the check_filepaths method.

    """

    output_file_path = str(sys.path[0]) + "\\data\\csv"
    checkinout = CheckInOutFolder("dummy", output_file_path)
    with pytest.raises(OSError):
        checkinout.check_filepaths()

def test_Check_filepath_positive_test():
    """
    Test the CheckInOutFolder class with correct input and output file paths.

    This test checks the behavior of the CheckInOutFolder class when provided
    with correct input and output file paths. It uses a try-except block to ensure
    that no OSError is raised during the check_filepaths method.

    """

    input_file_path = str(sys.path[0]) + "\\data\\json"
    output_file_path = str(sys.path[0]) + "\\data\\csv"
    checkinout = CheckInOutFolder(input_file_path, output_file_path)

    try:
        checkinout.check_filepaths()
    except OSError:
        assert False, "OSError is raised"






