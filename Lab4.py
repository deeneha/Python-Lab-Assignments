##Nehashri Prakash Dusa
##Python Lab4 Assignment

1.Write a Python program that takes a number as input and prints "Even" if the number is even and "Odd" if it's odd.
#Solution
number = int(input("Enter a number: "))
if number % 2 == 0:
    print(f"The number {number} is Even.")
else:
    print(f"The number {number} is Odd.")
#Sample Input:
Enter a number: 4
The number 4 is Even.
#Output
Enter a number: 7
The number 7 is Odd.

2.Create a Python program that checks whether a person is eligible to vote (18 years or older) based on their age.
#Solution
age = int(input("Enter your age: "))
if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")
#Sample Input
Enter your age: 20
You are eligible to vote.
#Output
Enter your age: 16
You are not eligible to vote.

3.Write a Python program that determines if a given year is a leap year or not.
#Solution
year = int(input("Enter a year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")
#Sample Input
Enter a year: 2024
2024 is a leap year.
#Output
Enter a year: 2023
2023 is not a leap year.

4.Create a Python program that checks if a user-given number is positive, negative, or zero.
#Solution
number = float(input("Enter a number: "))
if number > 0:
    print(f"The number {number} is Positive.")
elif number < 0:
    print(f"The number {number} is Negative.")
else:
    print("The number is Zero.")
#Sample Input:
Enter a number: 5
The number 5.0 is Positive.
Enter a number: -3
The number -3.0 is Negative.
#Output
Enter a number: 0
The number is Zero.

5.Write a Python program that determines the largest of three numbers entered by the user.
#Solution
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))
if num1 >= num2 and num1 >= num3:
    print(f"The largest number is {num1}.")
elif num2 >= num1 and num2 >= num3:
    print(f"The largest number is {num2}.")
else:
    print(f"The largest number is {num3}.")
#Output
Enter the first number: 10
Enter the second number: 20
Enter the third number: 15
The largest number is 20.0.
