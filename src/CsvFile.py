import csv
class CsvFile:
    def __init__(self,output_filepath):
        self.output_filepath = output_filepath

    def Convert_tocsv(self,master_json): # Convert to csv
        master_json_fields = master_json[0].keys()
        with open(self.output_filepath + "\\output.csv", 'a', newline='') as csv_file:
            csv_writer_object = csv.DictWriter(csv_file, fieldnames=master_json_fields)
            csv_writer_object.writeheader()
            for csv_rec in master_json:
                csv_writer_object.writerow(csv_rec)
        print("CSV file has been created")