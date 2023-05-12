#cleaning CSV
import pandas as pd

#function to calculate the interquartile range (IQR) of a column:
def get_iqr(col):
    Q1 = col.quantile(0.25)
    Q3 = col.quantile(0.75)
    IQR = Q3 - Q1
    return IQR

#function to filter outliers from a column based on its IQR:
def filter_outliers(col):
    IQR = get_iqr(col)
    upper_limit = col.quantile(0.75) + 1.5 * IQR
    lower_limit = col.quantile(0.25) - 1.5 * IQR
    return (col > lower_limit) & (col < upper_limit)


def cleanCSV(df):
    #step 1 : Identifying the missing values
    '''.sum() method after applying .isnull(), this will return 
    the sum of missing values within each column in the data frame.
    '''
    missingCount = df.isnull().sum()
    print("Missing values are", missingCount)
    
    #Size of original dataset
    print("size of dataframe",df.shape)
    
    #Dropping the missing rows.
    '''df.dropna() – Drop all rows that have any NaN values
       df.dropna(how=’all’) – Drop only if ALL columns are NaN
       df.dropna(thresh=2) – Drop row if it does not have at least two values that are not NaN
       df.dropna(subset=[1]) – Drop only if NaN in specific column'''  
    df_dropped = df.dropna(how = 'any')
    
    #create copy of new dataframe
    df_copy = df_dropped
    
    #printing the update dataframe to check the missing values 
    print("New dataframe")
    print(df_copy.isna().sum())
    print(df_copy.isna().sum())
    
    #replace the missing values for int or float cloumns with mean values
    num_cols = df_copy.select_dtypes(include=['int64', 'float64'])
    means = num_cols.mean()
    df_copy = df_copy.fillna(means)
    
    #Dealing with outliners
    filtered = num_cols.apply(filter_outliers)
    '''Use the all() method to create a boolean mask to filter the original 
    dataframe to exclude all rows with outlier values:'''
    mask = filtered.all(axis=1)
    df_copy = df_copy[mask]
    
    #removing duplicate entries
    #finding duplicate eentries
    dulpicateEntries=df_copy.duplicated().sum()
    print("Duplicate entries are", dulpicateEntries)
    
    #Duplicate entries aren't in this dataframe but in case if it existed
    df1 = df_copy.drop_duplicates()
    
    # replace all occurrences of '..' with 0
    df1 = df1.replace('..', 0)
    
    
    #removing , from all values to make manipulation easy
    df1 = df1.applymap(lambda x: x.replace(',', '') if isinstance(x, str) else x)
    
    
    
    return df1
