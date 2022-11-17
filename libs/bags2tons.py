# takes a number of bags of coffee and returns the metric tonnage as a number

def bags2tonnes(bags):

    # set weight constants
    kg2mt = 1000 # kg per metric tonne
    bags2kg = 60 # kg per bag of coffee
    th2m = 1000 # the ICO data is expressed in 'thousands of bags'

    # calculation
    return bags * th2m * bags2kg / kg2mt
