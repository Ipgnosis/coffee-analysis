from libs.store_data import read_json_data, write_json_data

# strip time zones string list down to a sorted list of floats
def timezone_to_float(tz_list):

    fl_list = []
    for tz in tz_list:

        mins = 0
        sign = tz[3]
        hrs = int(tz[4:6])
        mins_str = tz[7:9]

        if (mins_str == '00'):
            pass
        elif (mins_str == '30'):
            mins = 0.5
        elif (mins_str == '45'):
            mins = .75

        temp_fl = hrs + mins

        if (sign == '-'):
            this_tz = temp_fl * -1
        else:
            this_tz = temp_fl

        fl_list.append(this_tz)

    return sorted(fl_list, key=lambda x: float(x))


# read coffee file and create new json
def create_new_coffee_file(coffeef, countryType):

    new_file = {}
    for key, vals in coffeef.items():
        tempObj = {}
        if (len(vals['countryType']) > 1) and (countryType[0] in vals['countryType']) and (countryType[1] in vals['countryType']):
            tempObj['region'] = vals['region']
            tempObj['country'] = vals['country']
            tempObj['time_zones'] = timezone_to_float(vals['time_zone'])
            #tempObj['time_zones'] = vals['time_zones']

            new_file[key] = tempObj
        '''
        elif (len(vals['countryType']) == 1) and (countryType[0] in vals['countryType']):
            tempObj['region'] = vals['region']
            tempObj['country'] = vals['country']
            tempObj['time_zones'] = vals['time_zone']
            new_file[key] = tempObj
'''
    return new_file


# get data from db_file
def get_attributes(infile, outfile, attribute_list):

    for this_attr in attribute_list:
        for key, vals in infile.items():
            if (key in outfile) and (this_attr in vals):
                outfile[key][this_attr] = vals[this_attr]
        #        outfile[key]['time_zones'] = timezone_to_float(vals['time_zone'])

    return outfile


# params
def main():
    # output files
    prod_exp_path = 'data/prod_exp.json'
    imp_exp_path = 'data/imp_exp.json'
    importers_path = 'data/importers.json'

    # input file(s)
    db_path = 'data/db.json'
    db_file = read_json_data(db_path)
    country_path = 'data/countries.json'
    country_file = read_json_data(country_path)

    pe_list = ['P', 'E']
    i_list = ['I']
    ie_list = ['I', 'E']

    #new_attributes_list = ['countryType']

    #new_countries_file = get_attributes(db_file['countries'], country_file, new_attributes_list)
    countries_obj = db_file['countries']

    prod_exp = create_new_coffee_file(countries_obj, pe_list)
    imp_exp = create_new_coffee_file(countries_obj, ie_list)
    #importers = create_new_coffee_file(country_file, i_list)

    if (write_json_data(prod_exp_path, prod_exp)):
        print(f"{prod_exp_path} file written")

    if (write_json_data(imp_exp_path, imp_exp)):
        print(f"{imp_exp_path} file written")

'''
    if (write_json_data(country_path, new_countries_file)):
        print(f"{country_path} file written")

    if (write_json_data(importers_path, importers)):
            print(f"{importers_path} file written")
'''


# run main
if __name__ == "__main__":
    main()
