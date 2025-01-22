import pandas as pd

print(pd.options.display.max_rows)
df = pd.read_csv("people_data.csv")
print(df.to_string())
