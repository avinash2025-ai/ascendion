import pandas as pd

print(pd.options.display.max_rows)
df = pd.read_csv("people_data.csv")
print(df.head(2))
print(df.tail(2))

print(df.info())

print(df.duplicated())
