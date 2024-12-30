##Nehashri Prakash Dusa
##Python Lab6 Assignment

1. Write a python program to reverse a number using a while loop. 
#Solution
number = int(input("Enter a number: "))
reversed_number = 0
while number > 0:
    digit = number % 10
    reversed_number = reversed_number * 10 + digit
    number = number // 10
print("Reversed Number:", reversed_number)
#Output
Enter a number: 1234
Reversed Number: 4321

2. Write a python program to check whether a number is palindrome or not? 
#Solution
number = int(input("Enter a number: "))
original_number = number
reversed_number = 0
while number > 0:
    digit = number % 10
    reversed_number = reversed_number * 10 + digit
    number = number // 10
if original_number == reversed_number:
    print(f"{original_number} is a Palindrome.")
else:
    print(f"{original_number} is not a Palindrome.")
#Output
Enter a number: 121
121 is a Palindrome.

3. Write a python program finding the factorial of a given number using a while loop. 
#Solution
number = int(input("Enter a number: "))
factorial = 1
while number > 0:
    factorial *= number
    number -= 1
print("Factorial:", factorial)
#Output
Enter a number: 5
Factorial: 120

4. Accept numbers using input() function until the user enters 0. If user input 0 then break the while loop and display the sum of all the numbers.
#Solution
total_sum = 0
while True:
    num = int(input("Enter a number (enter 0 to stop): "))
    if num == 0:
        break
    total_sum += nu
print("Total Sum:", total_sum)
#Output
Enter a number (enter 0 to stop): 5
Enter a number (enter 0 to stop): 10
Enter a number (enter 0 to stop): 0
Total Sum: 15

5. Program to check whether the given number is Armstrong or not.
#Solution
number = int(input("Enter a number: "))
original_number = number
sum_of_powers = 0
while number > 0:
    digit = number % 10
    sum_of_powers += digit ** 3
    number = number // 10
if original_number == sum_of_powers:
    print(f"{original_number} is an Armstrong number.")
else:
    print(f"{original_number} is not an Armstrong number.")
#Output
Enter a number: 153
153 is an Armstrong number.

6. Program to find the factorial of a number.
#Solution
number = int(input("Enter a number: "))
factorial = 1
for i in range(1, number + 1):
    factorial *= i
print(f"Factorial of {number} is {factorial}.")
#Output
Enter a number: 5
Factorial of 5 is 120.

7. Create a code that describe the use of break statement in while loop
#Solution
count = 1
while count <= 10:
    if count == 5:
        print("Breaking the loop at count =", count)
        break
    print("Count =", count)
    count += 1
#Output
Count = 1
Count = 2
Count = 3
Count = 4
Breaking the loop at count = 5

8. Write a Python program using a while loop to iterate through each character of the string "Python" and print each character on a new line. Additionally, calculate and print the length of the string.
#Solution
string = "Python"
index = 0
length = len(string)
print("Characters in the string:")
while index < length:
    print(string[index])
    index += 1
print("Length of the string:", length)
#Output
Characters in the string:
P
y
t
h
o
n
Length of the string: 6

9. Write a Python program that takes an integer input from the user and calculates its factorial using a while loop. Display the result as the factorial of the entered number.
#Solution
number = int(input("Enter a number: "))
factorial = 1
temp = number
while temp > 0:
    factorial *= temp
    temp -= 1
print(f"The factorial of {number} is {factorial}.")
#Output
Enter a number: 5
The factorial of 5 is 120.
