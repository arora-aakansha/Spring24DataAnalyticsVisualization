#read file 
import pandas as pd
import json
from pprint import pprint

#read csv file

def readCSV():
    fileName=input("enter file name with extension ")
    df= pd.read_csv(fileName)
    return df

#read json
def readJson():
    '''Since our json doesn't have equal number of columns we need to fix to perform further actions
    Missing column was manually identified i.e days
    It was extracted with help of keys and update with pprint
    this all was done in dictionary, later this dictionary is converted to datframe for further usage'''
    
    fileName=input("enter file name with extension ")
    with open(fileName) as fp:
        iceberg_locations = fp.read()

    iceberg_locations = json.loads(iceberg_locations)

    update_days = list(iceberg_locations.keys())
    if update_days:
        pprint(iceberg_locations[update_days[0]][:3])
    cleaned_location_data = []

    for date, iceberge_details in iceberg_locations.items():
        for detail in iceberge_details:
            detail['date'] = date
            cleaned_location_data.append(detail)

    df = pd.DataFrame(cleaned_location_data)
    return df
        

#read excel

#read webscrap

