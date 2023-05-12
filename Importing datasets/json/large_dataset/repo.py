import pandas as pd

#loading json file with pandas
df = pd.read_json('repo_metadata.json')

# Print the DataFrame
print(df.head())