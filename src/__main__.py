from CheckInOut import *
from JsonFile import *
from CsvFile import *

input_filepath = input("Please enter the file path for input Jsons")
output_filepath = input("Please enter the file path for output csv")

checkInOut = CheckInOut(input_filepath,output_filepath)
checkInOut.Check_filepath()


jsonfile = JsonFile(input_filepath)
input_files = jsonfile.Find_inputfiles()
valid_input_files = jsonfile.Check_json(input_files)
valid_header_files = jsonfile.Check_header(valid_input_files)
master_json = jsonfile.Create_masterjson(valid_header_files)

csvfile = CsvFile(output_filepath)
csvfile.Convert_tocsv(master_json)





