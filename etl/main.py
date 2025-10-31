import argparse
from etl.extract import extract_data, save_raw
from etl.transform import transform_data
from etl.load import save_parquet, print_summary

def main():
    parser = argparse.ArgumentParser(description="ETL pipeline")
    parser.add_argument("file_id", help="FILE_ID CSV на Google Drive")
    args = parser.parse_args()

    #  Extract
    df = extract_data(args.file_id)
    save_raw(df)

    #  Transform
    df = transform_data(df)

    #  Load
    save_parquet(df)
    print_summary(df)

if __name__ == "__main__":
    main()
