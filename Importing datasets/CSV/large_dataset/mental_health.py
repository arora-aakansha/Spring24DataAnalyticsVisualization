#importing CSV file with  CSV module
import pandas as pd
import numpy as np
#Code to check files in directory
# import os
# print(os.getcwd())

# Read the CSV file into a pandas DataFrame
df = pd.read_csv("MentalHealth4Weeks.csv")

# Print the first 5 rows of the DataFrame
print(df.head())

#print total missing values
print(df.isna().sum())


#filling missing values with mean
df=df.fillna(0)

# Print the last 5 rows of the DataFrame
print(df.tail())

#custom convert for range to whole value
def convert_range(val):
    try:
        return round(float(str(val).split('-')[0]))
    except ValueError:
        return 'NA'

#raning Quartile
df['Quartile Range']=df['Quartile Range'].apply(convert_range)

#print dataframe
print(df)


