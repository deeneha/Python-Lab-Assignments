##Nehashri Prakash Dusa
##Python Lab11 Assignment


1. Write a Python program to handle a ZeroDivisionError exception when dividing a number by zero. 
#Solution
def divide_numbers():
    try:
        num1 = float(input("Enter the numerator: "))
        num2 = float(input("Enter the denominator: "))
        result = num1 / num2
        print(f"Result: {result}")
    except ZeroDivisionError:
        print("Error: You cannot divide by zero.")
#If the user enters 10 for numerator and 0 for denominator:
Error: You cannot divide by zero.
#Output
Result: 5.0

2. Write a Python program that prompts the user to input an integer and raises a ValueError exception if the input is not a valid integer. 
#Solution
def input_integer():
    try:
        user_input = input("Enter an integer: ")
        number = int(user_input)
        print(f"Valid integer: {number}")
    except ValueError:
        print("Error: That's not a valid integer.")
#If the user enters abc:
Error: That's not a valid integer.
#Output
Valid integer: 10

3. Write a Python program that opens a file and handles a FileNotFoundError exception if the file does not exist. 
#Solution
def open_file():
    try:
        with open("non_existing_file.txt", "r") as file:
            print(file.read())
    except FileNotFoundError:
        print("Error: The file does not exist.")
#If the file non_existing_file.txt does not exist
Error: The file does not exist.
#Output
If the file exists, it will display the content of the file.

4. Write a Python program that prompts the user to input two numbers and raises a TypeError exception if the inputs are not numerical
#Solution
def input_numbers():
    try:
        num1 = input("Enter the first number: ")
        num2 = input("Enter the second number: ")
        num1 = float(num1)  # Convert to float
        num2 = float(num2)
        print(f"Sum: {num1 + num2}")
    except ValueError:
        print("Error: Please enter valid numbers.")
    except TypeError:
        print("Error: Invalid type of input.")
#If the user enters 10 for the first number and abc for the second:
Error: Please enter valid numbers.
#Output
Sum: 20.0
