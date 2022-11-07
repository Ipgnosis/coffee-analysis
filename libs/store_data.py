'''read and write json files to path provided'''
import json


# read a json data file
def read_json_data(fname):
    '''Takes a file path and returns a file or an error'''

    try:
        with open(fname, "r", encoding="utf-8") as json_file:
            data = json.load(json_file)
        return data
    except OSError as error:
        print(error)
        print(f"File {fname} cannot be read")
        return False


# write a json data file
def write_json_data(fname, wdata):
    '''Takes a file path and data and writes data to the file'''

    try:
        with open(fname, 'w', encoding='utf-8') as outfile:
            # json.dump(wdata, outfile, indent=4)
            json.dump(wdata, outfile, indent=4, ensure_ascii=False)

        return True
    except OSError as error:
        print(error)
        print(f"File {fname} cannot be saved")
        return False
