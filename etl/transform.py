def transform_data(df):
    """
    Преобразует указанные колонки в тип 'category'.
    """
    categorical_cols = [
        'Attrition', 'BusinessTravel', 'Department', 'EducationField',
        'Gender', 'JobRole', 'MaritalStatus', 'OverTime'
    ]
    for col in categorical_cols:
        if col in df.columns:
            df[col] = df[col].astype('category')

    print("Категориальные колонки преобразованы")
    return df
