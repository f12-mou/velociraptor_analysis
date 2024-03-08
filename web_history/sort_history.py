import pandas as pd

# dataframe loaded
df = pd.read_csv('input.csv')

# Visited column refers to last visiting time
df['Visited'] = pd.to_datetime(df['Visited'])

# We want the newest first
df_sorted = df.sort_values(by='Visited', ascending=False)

# Listing according to mostly newer websites first
df_sorted.to_csv('sorted_browsing_history.csv', index=False)

