import pandas as pd

# load csv into dataframe
ssn = list(pd.read_csv("1-unit-testing-assert-statement/exercises/data/ssn.csv"))

# print all dataframe records
print(ssn)

print("preview first record in ssn data")
print(ssn[0])

print("preview the last record ")
print(ssn[len(ssn) - 1])

print("preview the last record in ssn data")
print(ssn[-1])


print("preview starting from second to third record, just one record")
print(ssn[1:3])


print("presenting the records in reversed form starting from the record before the last.")
print(ssn[-2:])


print("presenting all records except the last two records.")
print(ssn[:-2])


print("presenting all records in reversed order including all columns except the last.")
print(ssn[-1::-1])