import os

def save_parquet(df, filename="processed_dataset.parquet", output_dir="data"):
    """
    Сохраняет DataFrame в Parquet.
    """
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, filename)
    df.to_parquet(path, engine="pyarrow", index=False)
    print(f"Данные сохранены в Parquet: {path}")

def print_summary(df):
    """
    Выводит пропуски, типы данных и первые 10 строк.
    """
    print("Пропуски по колонкам:\n", df.isnull().sum())
    print("\nТипы данных:\n", df.dtypes)
    print("\nПервые 10 строк:\n", df.head(10))
