import pandas as pd

FILE_ID = "1BlN2qCu0WEVX6rHUBQw56wsljv7kqaJQ"
file_url = f"https://drive.google.com/uc?export=download&id={FILE_ID}"

raw_data = pd.read_csv(file_url)
raw_data.head(10) 
