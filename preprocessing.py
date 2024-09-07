import pandas as pd

file_path = 'E:\\Programming\\AIProject\\hypothyroid.csv'
df = pd.read_csv(file_path, na_values='?')

# Calculate total missing values
total_missing_values = df.isnull().sum().sum()

# Calculate total rows that contain missing values
rows_with_missing_values = df.isnull().any(axis=1).sum()

totalRows=df.shape[0]

# print(f"Total missing values: {total_missing_values}")
# print(f"Total number of rows:{totalRows}")
# print(f"Total rows with missing values: {rows_with_missing_values}")

# for column in df.columns:
#     has_na = df[column].isnull().any()
#     print(f"Does the column '{column}' have any NA values? {has_na}")
#     numberOfMissingValuesInEachColumn=df[column].isnull().sum()
#     print(f"Number of missing values in column:{numberOfMissingValuesInEachColumn}")

df_cleaned = df.dropna(subset=['Sex'])
if 'Unnamed: 0' in df_cleaned.columns:
    df_cleaned.rename(columns={'Unnamed: 0': 'result'}, inplace=True)

cleaned_file_path = 'E:\\Programming\\AIProject\\hypothyroidWithoutMissingValuesOfSexColmn.csv'
df_cleaned.to_csv(cleaned_file_path, index=False)
print("\n\n")

for column in df_cleaned.columns:
    has_na = df_cleaned[column].isnull().any()
    print(f"Does the column '{column}' have any NA values? {has_na}")
    numberOfMissingValuesInEachColumn=df_cleaned[column].isnull().sum()
    print(f"Number of missing values in column:{numberOfMissingValuesInEachColumn}")