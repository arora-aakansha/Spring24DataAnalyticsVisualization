#importing readFile
import readFile
import cleanFile
import manupulatingData

def workingWithJson():
    #reading json
    df = readFile.readJson()
    
    #print first 5 rows of dataFrame
    print(df.head())
    return df

dataFrame=workingWithJson()
