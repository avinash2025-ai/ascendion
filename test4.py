import pandas as pd

#list
numlist = [5,1,6]
num = pd.Series(numlist)

print(num)

#Dictionary

student = {
    "name" : "Avinash",
    "subj" : "Math",
    "Marks": 98
}

stud = pd.Series(student)
print(stud)
