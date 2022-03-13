
import pandas as pd

# load car_models data into dataframe, then cast to python's list
car_models = list(pd.read_csv("1-unit-testing-assert-statement/exercises/data/car_models.csv"))

print(car_models)


# create new list
list_1 = [x for x in car_models] 

# iterate all new list elements using index
for i in range(0, len(list_1)): 
    print(list_1[i]) 


# iterate all new list elements 
for i in list_1: 
    print(i)


# check if the model existed 
"D150"  in list_1 


# check if the model existed 
"Mustang" in list_1 


