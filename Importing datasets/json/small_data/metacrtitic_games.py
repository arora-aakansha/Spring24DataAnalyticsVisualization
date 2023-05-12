import json
import pandas as pd
import numpy as np

# Open the JSON file
with open('metacritic_games.json', 'r') as file:
    # Load the JSON data from the file
    data = json.load(file)

# Print the loaded data
# print(data)

#loading json file with pandas
df = pd.read_json('metacritic_games.json')

# Print the DataFrame
print(df.head())

#clean json file

# Drop any rows with missing values
df.dropna(inplace=True)

# Set the 'name' column as the index
df.set_index('name', inplace=True)

# Print the cleaned DataFrame
print(df.tail())

#finding all columns in dataset
print(df.columns)

# print the value of the 'metascore' column for the 3rd row using loc
print(df['metascore'])

# replace 'tbd' values with NaN in the 'user_score' column
df['user_score'] = df['user_score'].replace('tbd', np.nan)

# convert the 'metascore' column to integers
df['metascore'] = df['metascore'].astype(int)

# convert the 'metascore' column to integers
df['user_score'] = df['user_score'].astype(float)

#creating new column for good bad or average

# create a new column called 'score_category'
df['score_category'] = ''

# loop through each row of the DataFrame
for index, row in df.iterrows():
    # calculate the average of the 'score' and 'performance' columns for the current row
    average = (row['metascore'] + row['user_score']) / 2
    
    # determine the category based on the average value
    if average >= 8:
        category = 'good'
    elif average >= 5:
        category = 'average'
    else:
        category = 'bad'
    
    # update the 'score_category' column for the current row
    df.at[index, 'score_category'] = category
    
# save the updated DataFrame to the original JSON file
df.to_json('metacritic_games.json', orient='records')

#print updaated df
print(df)
    
