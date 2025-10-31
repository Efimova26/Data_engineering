import os
import pandas as pd
from sqlalchemy import create_engine, text
from db_config import DB_CONFIG  # Импортируем конфигурацию из файла, который в .gitignore

def save_parquet(df: pd.DataFrame, output_dir: str = "data/processed", filename: str = "processed_dataset.parquet"):
    """
    Сохраняет DataFrame в Parquet
    """
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, filename)
    df.to_parquet(path, engine="pyarrow", index=False)
    print(f"Данные сохранены в Parquet: {path}")

def load_to_db(df: pd.DataFrame, db_config: dict, max_rows: int = 100):
    """
    Загружает до max_rows строк в PostgreSQL в таблицу efimova.
    
    db_config = {
        "user": ...,
        "password": ...,
        "url": ...,
        "port": ...,
        "database": ...
    }
    """
    # Подключаемся к PostgreSQL
    engine = create_engine(
        f"postgresql+psycopg2://{db_config['user']}:{db_config['password']}"
        f"@{db_config['url']}:{db_config['port']}/{db_config['database']}"
    )

    # Ограничиваем количество строк
    df_subset = df.head(max_rows)

    # Загружаем в таблицу efimova
    df_subset.to_sql(
        name="efimova",
        con=engine,
        schema="public",
        if_exists="replace",
        index=True
    )

    # Добавляем первичный ключ по индексу
    with engine.begin() as conn:
        conn.execute(text('ALTER TABLE public.efimova ADD PRIMARY KEY (index)'))

    print(f"Выгружено {len(df_subset)} строк в таблицу efimova")

# Пример вызова функций
if __name__ == "__main__":
    df = pd.read_csv("data/raw/raw_data.csv")  # Путь к сырому CSV
    save_parquet(df)
    load_to_db(df, db_config=DB_CONFIG)
