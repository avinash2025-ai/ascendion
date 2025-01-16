import pandas as pd

file_path = "people_data.csv"

df = pd.read_csv(file_path)
df = df.rename(columns={"Date of birth" : "DOB"})

print(df.to_string())