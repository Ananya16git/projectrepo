This file contain the information for the POC JSON to CSV conversion

Information about the code 
1. All source code is written in SRC folder
2. __main__.py is the starting point of the code
3. There are total three classes are like below
    
    i. JsonFile.py' - Check the if the Json files are valid
                      Check for the input and output folder    
    ii. CsvFile.py - Check the header of the Jsons if all header s are of same structure , JSONs having different structure header is not converted together with other JSONS

    iii. JsonFile.py - prepare the output CSV
4. All test files are kept inside Data folder
5. All test cases are kept in the test folder

Information about the code run

1. Input the input folder name where all the JSON files are stored for conversion
2. Input the output folder name where newly created CSV file will be stored

Assumption for code run

1. Only valid JSON files will be converted to CSV
2. JSONs with same keys will be converted to CSV , rest of the JSONs will not be converted

