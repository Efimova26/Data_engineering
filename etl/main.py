import argparse
from etl.extract import extract_data, save_raw
from etl.transform import transform_data
from etl.validate import validate_df
from etl.load import save_parquet, load_to_db

def main():
    parser = argparse.ArgumentParser(description="ETL pipeline")
    parser.add_argument("file_id", help="FILE_ID CSV на Google Drive")
    args = parser.parse_args()

    # === Extract ===
    df = extract_data(args.file_id)
    save_raw(df)

    # === Transform ===
    df = transform_data(df)

    # === Validate ===
    validate_df(df)

    # === Load ===
    save_parquet(df)

    # Параметры подключения к базе данных (подставь свои)
    db_config = {
        "user": "ваш_user",
        "password": "ваш_pass",
        "url": "ваш_url",
        "port": 5432,
        "database": "homeworks"
    }
    load_to_db(df, db_config, max_rows=100)

if __name__ == "__main__":
    main()

