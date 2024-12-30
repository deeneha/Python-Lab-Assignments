##Nehashri Prakash Dusa
##Python Lab1 Assignment

Q1: Print "Hello World"
#Solution
print("Hello World")
#Output
Hello World

Q2: Describe Local Variable and Global Variable Code
#Solution 
x = "Global Variable"
def my_function():
    # Local variable
    x = "Local Variable"
    print("Inside function:", x)
my_function()
print("Outside function:", x)
#Output
Inside function: Local Variable  
Outside function: Global Variable

Q3: Write a Code to Describe Indentation Error
#Solution
def my_function():
print("Hello")  
my_function()
#Output
IndentationError: expected an indented block

Q4: Write a Code for Local and Global Variable with the Same Name
#Solution
x = "Global"
def my_function():
    x = "Local"  # Local variable
    print("Inside function:", x)
my_function()
print("Outside function:", x)
#Output
Inside function: Local  
Outside function: Global

Q5: Write a code for string, int and float input.
#Solution
name = input("Enter your name: ")
age = int(input("Enter your age: "))
height = float(input("Enter your height in meters: "))
print("Name:", name)
print("Age:", age)
print("Height:", height)
#Sample Input
Enter your name: Nehashri  
Enter your age: 22  
Enter your height in meters: 1.65
#Output
Name: Nehashri  
Age: 22  
Height: 1.65










