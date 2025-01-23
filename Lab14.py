##Nehashri Prakash Dusa
##Python Lab14 Assignment

1.Write a python program and iterate the given tuples Input: employee1 = ("John Doe", 101, "Human Resources", 60000) employee2 = ("Alice Smith", 102, "Marketing", 55000) employee3 = ("Bob Johnson", 103, "Engineering", 75000)
#Solution
def iterate_tuples(*employees):
    for employee in employees:
        print(f"Name: {employee[0]}, ID: {employee[1]}, Department: {employee[2]}, Salary: {employee[3]}")
employee1 = ("John Doe", 101, "Human Resources", 60000)
employee2 = ("Alice Smith", 102, "Marketing", 55000)
employee3 = ("Bob Johnson", 103, "Engineering", 75000)
iterate_tuples(employee1, employee2, employee3)
#Output
Name: John Doe, ID: 101, Department: Human Resources, Salary: 60000
Name: Alice Smith, ID: 102, Department: Marketing, Salary: 55000
Name: Bob Johnson, ID: 103, Department: Engineering, Salary: 75000

2.Write a Python program to convert a list to a tuple. 
Input: listx = [5, 10, 7, 4, 15, 3]
Output: (5, 10, 7, 4, 15, 3)
#Solution
def list_to_tuple(lst):
    return tuple(lst)

# Input list
listx = [5, 10, 7, 4, 15, 3]
result = list_to_tuple(listx)
print(result)
#Output
(5, 10, 7, 4, 15, 3)

