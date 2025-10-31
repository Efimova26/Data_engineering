import argparse
from etl.extract import load_csv, save_raw
from etl.transform import transform_types
from etl.load import save_parquet, load_to_db
from etl.validate import validate_df
from etl.db_config import DB_CONFIG  # импорт конфигурации базы

def main():
    parser = argparse.ArgumentParser(description="ETL pipeline")
    parser.add_argument(
        "--source", required=True, help="URL или путь к исходному CSV файлу"
    )
    parser.add_argument(
        "--table",
        default="efimova",
        help="Название таблицы для записи в PostgreSQL",
    )
    parser.add_argument(
        "--parquet",
        default="data/processed/processed_dataset.parquet",
        help="Путь для сохранения parquet файла",
    )
    parser.add_argument(
        "--validate", action="store_true", help="Включить валидацию данных"
    )

    args = parser.parse_args()

    # Загрузка и сохранение raw данных
    df = load_csv(args.source)
    save_raw(df)

    # Трансформации
    df = transform_types(df)

    # Валидация (если указан флаг)
    if args.validate:
        validate_df(df)

    # Сохранение parquet
    save_parquet(df, args.parquet)

    # Запись в базу PostgreSQL
    load_to_db(df, db_config=DB_CONFIG, max_rows=100)

    print("ETL pipeline выполнен успешно!")

if __name__ == "__main__":
    main()

