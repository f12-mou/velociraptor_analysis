import pandas as pd

# dataframe loaded
df = pd.read_csv('input.csv')

# filtered domains starting with https
filtered_df = df[df['URL'].str.startswith('https')]

# further filtering for domain detection
filtered_df['Domain'] = filtered_df['URL'].apply(lambda x: x.split("//")[1].split("/")[0])

# counting domains and sorting in descending order
domain_counts = filtered_df['Domain'].value_counts().sort_values(ascending=False)
print(domain_counts)
# Saving in CSV
# print("Writing in CSV files")
domain_counts.to_csv('sorted_domain_counts.csv')
