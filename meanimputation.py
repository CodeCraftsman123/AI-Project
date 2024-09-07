import pandas as pd

file_path = 'E:\\Programming\\AIProject\\hypothyroidWithoutMissingValuesOfSexColmn.csv'
df = pd.read_csv(file_path, na_values=' ')

df_shuffled = df.sample(frac=1, random_state=42).reset_index(drop=True)

numeric_columns = ['Age', 'TSH', 'T3', 'TT4', 'T4U', 'FTI', 'TBG']

for column in numeric_columns:
    if column in df_shuffled.columns:
        # Calculate the mean of the column excluding NA values
        mean_value = df_shuffled[column].mean(skipna=True)
        mean_value = round(mean_value, 2)
        df_shuffled[column].fillna(mean_value, inplace=True)

cleaned_file_path = 'E:\\Programming\\AIProject\\hypothyroid_mean_imputed_shuffled.csv'
df_shuffled.to_csv(cleaned_file_path, index=False)