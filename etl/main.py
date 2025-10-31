import argparse
from etl.extract import extract_data, save_raw
from etl.transform import transform_data
from etl.load import save_parquet, load_to_db
from db_config import DB_CONFIG

def main():
    parser = argparse.ArgumentParser(description="ETL pipeline")
    parser.add_argument(
        "--file_id", required=True, help="ID Google Drive CSV файла"
    )
    args = parser.parse_args()

    # Загрузка и сохранение raw данных
    df = extract_data(args.file_id)
    save_raw(df)

    # Трансформации
    df = transform_data(df)

    # Сохранение parquet
    save_parquet(df)

    # Запись в базу PostgreSQL
    load_to_db(df, db_config=DB_CONFIG, max_rows=100)

    print("ETL pipeline выполнен успешно!")

if __name__ == "__main__":
    main()
