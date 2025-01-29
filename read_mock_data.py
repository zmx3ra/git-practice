import pandas as pd
import matplotlib.pyplot as plt
import chardet

# First detect the encoding
with open('MOCK_DATA.csv', 'rb') as file:
    raw_data = file.read()
    result = chardet.detect(raw_data)
    encoding = result['encoding']
    print(f"File encoding: {encoding}")

# Read the CSV file with the detected encoding
df = pd.read_csv('MOCK_DATA.csv', encoding=encoding)

# Remove rows where last_name is empty or null
df = df.dropna(subset=['last_name'])
df = df[df['last_name'].str.strip() != '']

# Remove rows where height is missing, empty, or null
df = df.dropna(subset=['height'])
print(f"Number of rows after removing empty last names and invalid heights: {len(df)}")

# Display the first few rows of the DataFrame
print("\nFirst 5 rows of the data:")
print(df.head())

# Display basic information about the DataFrame
print("\nDataFrame info:")
print(df.info())

# Display basic statistical summary
print("\nBasic statistical summary:")
print(df.describe())

# Create a histogram for height distribution
plt.figure(figsize=(10, 6))
plt.hist(df['height'], bins=30, edgecolor='black')
plt.title('Distribution of Heights')
plt.xlabel('Height')
plt.ylabel('Frequency')
plt.grid(True, alpha=0.3)

# Add mean and median lines
plt.axvline(df['height'].mean(), color='red', linestyle='dashed', linewidth=1, label=f'Mean: {df["height"].mean():.2f}')
plt.axvline(df['height'].median(), color='green', linestyle='dashed', linewidth=1, label=f'Median: {df["height"].median():.2f}')

plt.legend()
plt.show() 