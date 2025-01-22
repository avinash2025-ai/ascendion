import pandas as pd

#Dictionary
student = {
    "name" : "Avinash",
    "subj" : ["Math","Phy","Chem"],
    "Marks": [98,97,92]
}

df = pd.DataFrame(student)
print(df)
print(df.loc[[0,1]])

#csv file read
import pandas as pd
csvdf = pd.read_csv("people_data.csv")
print(csvdf)