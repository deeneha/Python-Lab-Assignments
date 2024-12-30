##Nehashri Prakash Dusa
##Python Lab3 Assignment

1. Using input() function take one number from the user and using ternary operators check whether the number is even or odd 
#Solution
number = int(input("Enter a number: "))
result = "Even" if number % 2 == 0 else "Odd"
print(f"The number {number} is {result}.")
#Sample Input:
Enter a number: 4
The number 4 is Even.
#Output
Enter a number: 7
The number 7 is Odd.

2. Using input function take two number and then swap the number 
#Solution
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num1, num2 = num2, num1
print("After swapping:")
print("First number:", num1)
print("Second number:", num2)
#Output
Enter the first number: 10
Enter the second number: 20
After swapping:
First number: 20
Second number: 10

3. Write a Program to Convert Kilometers to Miles 
#Solution
kilometers = float(input("Enter distance in kilometers: "))
conversion_factor = 0.621371
miles = kilometers * conversion_factor
print(f"{kilometers} kilometers is equal to {miles:.2f} miles.")
#Output
Enter distance in kilometers: 5
5.0 kilometers is equal to 3.11 miles.

4. Find the Simple Interest on Rs. 200 for 5 years at 5% per year.
#Solution
principal = 200  # Rs. 200
rate = 5         # 5% per year
time = 5         # 5 years
simple_interest = (principal * rate * time) / 100
print(f"The Simple Interest on Rs. {principal} for {time} years at {rate}% per year is Rs. {simple_interest}.")
#Output
The Simple Interest on Rs. 200 for 5 years at 5% per year is Rs. 50.0.
