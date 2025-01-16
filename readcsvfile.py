import pandas as pd

file_path = "people_data.csv"

df = pd.read_csv(file_path)

print(df.to_string())