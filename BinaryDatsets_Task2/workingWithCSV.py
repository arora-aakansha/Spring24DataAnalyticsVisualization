#usage of modules and functions 

#importing readFile
import readFile
import cleanFile
import manupulatingData

def workingWithCSV():
    df=readFile.readCSV()

#print top 10 rows of csv
print(df.head())

#cleaning dataset
df1=cleanFile.cleanCSV(df)

#last 10 values of dataframe
print(df1.tail())

#print the whole data
print(df1)

#data manipulation
df2=manupulatingData.manipulateCountryGenderData(df1)
