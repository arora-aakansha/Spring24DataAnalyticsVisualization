#importing CSV file with  CSV module
import pandas as pd
#Code to check files in directory
# import os
# print(os.getcwd())

# Read the CSV file into a pandas DataFrame
df = pd.read_csv("iris.csv")

# Print the first 5 rows of the DataFrame
print(df.head())

#print total missing values
print(df.isna().sum())

#data type filling criteria
fill_values = {'int_col': 0, 'float_col': 0.0, 'str_col': 'unknown'}

#filling missing values with mean
df.fillna(value=fill_values,inplace=True)

# Print the last 5 rows of the DataFrame
print(df.tail())

#Adding column names
df.columns = ['A', 'B', 'C', 'D', 'E']

#print dataframe
print(df)

#rounding off column A to whole values
df['A'] = df['A'].round(0)

#printig rows 10 to 20
print(df.iloc[10:21])

