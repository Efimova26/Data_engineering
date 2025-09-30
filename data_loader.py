
import pandas as pd
import os

FILE_ID = os.getenv("FILE_ID")
file_url = f"https://drive.google.com/uc?id={FILE_ID}"

raw_data = pd.read_csv(file_url)

# преобразование категориальных столбцов
categorical_cols = [
    'Attrition', 'BusinessTravel', 'Department', 'EducationField',
    'Gender', 'JobRole', 'MaritalStatus', 'OverTime'
]

# применяем преобразование к типу 'category'
for col in categorical_cols:
    raw_data[col] = raw_data[col].astype('category')

# проверка наличия пропусков
missing_by_column = raw_data.isnull().sum()

#Сохраняем в Parquet
os.makedirs("data", exist_ok=True)
raw_data.to_parquet("data/processed_dataset.parquet", engine="pyarrow", index=False)

print(missing_by_column)
print(raw_data.dtypes)
print(raw_data.head(10))