import os
import pandas as pd
from io import StringIO
import requests

def extract_data(file_id: str) -> pd.DataFrame:
    """
    Загружает CSV с Google Drive по FILE_ID и возвращает DataFrame.
    """
    url = f"https://drive.google.com/uc?id={file_id}"
    response = requests.get(url)
    if response.status_code != 200:
        raise ConnectionError(f"Не удалось скачать файл: {url}")
    df = pd.read_csv(StringIO(response.text))
    if df.empty:
        raise ValueError("CSV пустой!")
    return df

def save_raw(df: pd.DataFrame, filename: str = "raw_data.csv", output_dir: str = "data/raw"):
    """
    Сохраняет исходные данные CSV в папку data/raw.
    """
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, filename)
    df.to_csv(path, index=False)
    print(f"Сырые данные сохранены: {path}")
