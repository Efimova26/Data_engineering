
import pandas as pd
import os

FILE_ID = os.getenv("FILE_ID")
file_url = f"https://drive.google.com/uc?id={FILE_ID}"

raw_data = pd.read_csv(file_url)
print(raw_data.head(10))