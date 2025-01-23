##Nehashri Prakash Dusa
##Python Lab13 Assignment

1. Write a Python script to concatenate the following dictionaries to create a new one. Sample Dictionary : dic1={1:10, 2:20} dic2={3:30, 4:40} dic3={5:50,6:60} Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
#Solution
def concatenate_dicts(*dicts):
    result = {}
    for dic in dicts:
        result.update(dic)
    return result
dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}
result = concatenate_dicts(dic1, dic2, dic3)
print(result)
#Output
{1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

2. Write a Python program to get the key, value and item in a dictionary. 
input: dict_num = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
#Solution
def print_dict_details(dic):
    for key, value in dic.items():
        print(f"Key: {key}, Value: {value}, Item: ({key}, {value})")
dict_num = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
print_dict_details(dict_num)
#Output
Key: 1, Value: 10, Item: (1, 10)
Key: 2, Value: 20, Item: (2, 20)
Key: 3, Value: 30, Item: (3, 30)
Key: 4, Value: 40, Item: (4, 40)
Key: 5, Value: 50, Item: (5, 50)
Key: 6, Value: 60, Item: (6, 60)