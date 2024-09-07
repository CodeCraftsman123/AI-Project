import pandas as pd
from sklearn.preprocessing import LabelEncoder

file_path = 'E:\\Programming\\AIProject\\hypothyroid_mean_imputed_shuffled.csv'

df = pd.read_csv(file_path)

for column in df.columns:
    has_na = df[column].isnull().any()
    print(f"Does the column '{column}' have any NA values? {has_na}")
    numberOfMissingValuesInEachColumn=df[column].isnull().sum()
    print(f"Number of missing values in column:{numberOfMissingValuesInEachColumn}")


# List of categorical columns to be label encoded
categorical_columns = [
    'Sex','on_thyroxine','query_on_thyroxine','on_antithyroid_medication','thyroid_surgery','query_hypothyroid','query_hyperthyroid',
'pregnant','sick','tumor','lithium','goitre','TSH_measured','T3_measured','TT4_measured','T4U_measured','FTI_measured','TBG_measured']

# Apply label encoding to each categorical column
label_encoders = {}
for column in categorical_columns:
    label_encoders[column] = LabelEncoder()
    df[column] = label_encoders[column].fit_transform(df[column])


target_column = 'result'  
if target_column in df.columns:
    label_encoders[target_column] = LabelEncoder()
    df[target_column] = label_encoders[target_column].fit_transform(df[target_column])

# Save the encoded DataFrame to a new CSV file
encoded_file_path = 'E:\\Programming\\AIProject\\hypothyroid_label_encoded_mean_imputed_shuffled.csv'  # Update with the correct file path
df.to_csv(encoded_file_path, index=False)
