import os

class CheckInOut:
    def __init__(self,input_filepath,output_filepath):
        self.input_filepath = input_filepath
        self.output_filepath = output_filepath

    def Check_filepath(self): # Check if the input and output folder exits

        if os.path.exists(self.input_filepath):
            input_filepath_found = True
            print("Input JSON folder found")
        else:
            input_filepath_found = False
            print("Input JSON folder is not found, rerun the code and enter correct path")
            exit()

        if os.path.exists(self.output_filepath):
            output_filepath_found = True
            print("Output CSV folder is found")
        else:
            output_filepath_found = False
            print("Output folder is not found, rerun the code and enter correct path")
            exit()