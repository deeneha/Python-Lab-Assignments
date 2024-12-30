##Nehashri Prakash Dusa
##Python Lab5 Assignment

Q1 Declare a div() function with two parameters. Then call the function and pass two numbers and display their division. 
#Solution:
def div(a,b):
	return a / b
num1 = 6
num2 = 3
print("Division of" ,num1, "and" , num 2 , "=" ,div(num1, num2))
#Output:
Division of 6 and 3 = 2.0

Q2 Declare a square() function with one parameter.Then call the function and pass one number and display the square of that number
#Solution:
def square(num):
	return num * num
num = 4
print("Square = " , square(num))
#Output:
Square =  16

Q3 Using max() and min() functions display the maximum and minimum of 5 random numbers.
#Solution:
import random
def  find_max_min():
	numbers = [random.randint(1, 100) for _ in range(5)]
	print("Random numbers: ",numbers)
	print("Maximum: ", max(numbers))
	print("Minimum: ", min(numbers))
find_max_min()
#Output:
Random numbers:  [87, 39, 51, 8, 72]
Maximum:  87
Minimum:  8
Random numbers:  [40, 58, 7, 38, 100]
Maximum:  100
Minimum:  7

Q4 Accept a name from the user and display that in lower case using lower() function 
#Solution:
def to_lowercase(name):
	return name.lower()
name = input("Enter your name : ")
print("Name in lowercase: ", to_lowercase(name))
#Output:
Enter your name : ROHAN
Name in lowercase:  rohan



