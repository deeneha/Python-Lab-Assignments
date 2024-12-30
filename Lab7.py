##Nehashri Prakash Dusa
##Python Lab7 Assignment

1. Print the table of 5 using for loop
#Solution
for i in range(1, 11):
    print(f"5 x {i} = {5 * i}")
#Output
5 x 1 = 5
5 x 2 = 10
...
5 x 10 = 50

2. Print even number series by taking input from the user:
#Solution
n = int(input("Enter the range for even numbers: "))
print("Even numbers:")
for i in range(2, n + 1, 2):
    print(i, end=" ")
#Output
Enter the range for even numbers: 10
Even numbers:
2 4 6 8 10

3. Create a list and iterate through its items using a for loop:
#Solution
my_list = [10, 20, 30, 40, 50]
print("List items:")
for item in my_list:
    print(item)
#Output
List items:
10
20
30
40
50

4. Calculate the sum of numbers from 1 to 10
#Solution
total = 0
for i in range(1, 11):
    total += i
print("Sum of numbers from 1 to 10:", total)
#Output
Sum of numbers from 1 to 10: 55

5. print the pattern
*
***
*****
*******
*********
#Solution
n = 5
for i in range(1, 10, 2):
    print("*" * i)

#Output
*
***
*****
*******
*********

6. Print the first 10 natural numbers using for loop 
#Solution
for i in range(1, 11):
    print(i, end=" ")
#Output
1 2 3 4 5 6 7 8 9 10

7. Python program to check if the given string is a palindrome 
#Solution
string = input("Enter a string: ")
if string == string[::-1]:
    print(f"{string} is a Palindrome.")
else:
    print(f"{string} is not a Palindrome.")
#Output
Enter a string: madam
madam is a Palindrome.

8. Python program to check if a given number is an Armstrong number
#Solution
number = int(input("Enter a number: "))
temp = number
sum_of_cubes = 0
while temp > 0:
    digit = temp % 10
    sum_of_cubes += digit ** 3
    temp //= 10
if sum_of_cubes == number:
    print(f"{number} is an Armstrong number.")
else:
    print(f"{number} is not an Armstrong number.")
#Output
Enter a number: 153
153 is an Armstrong number.

9. Python program to get the Fibonacci series between 0 to 50 
#Solution
a, b = 0, 1
print("Fibonacci series:")
while a <= 50:
    print(a, end=" ")
    a, b = b, a + b
#Output
Fibonacci series: 0 1 1 2 3 5 8 13 21 34

10. Python program to check the validity of password input by users
#Solution
password = input("Enter a password: ")
if len(password) >= 8 and any(char.isdigit() for char in password) and any(char.isupper() for char in password):
    print("Password is valid.")
else:
    print("Password is invalid.")
#Output
Enter a password: Password123
Password is valid.

11. program to print factorial of a number.
#Solution
number = int(input("Enter a number: "))
factorial = 1
for i in range(1, number + 1):
    factorial *= i
print(f"Factorial of {number} is {factorial}.")
#Output
Enter a number: 5
Factorial of 5 is 120.

12. Program to check whether the given number is prime or not.
#Solution
number = int(input("Enter a number: "))
if number > 1:
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            print(f"{number} is not a Prime number.")
            break
    else:
        print(f"{number} is a Prime number.")
else:
    print(f"{number} is not a Prime number.")
#Output
Enter a number: 7
7 is a Prime number.

13. program to display the patterns.
1                  
1 2
1 2 3
1 2 3 4
1 2 3 4 5  

#Solution
print("Numeric pattern:")
for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()
#Output
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5

A
B C
D E F
G H I J 
K L M N O 
P Q R S T U

#Solution
print("\nAlphabet pattern:")
char = 65
for i in range(1, 7):
    for j in range(i):
        print(chr(char), end=" ")
        char += 1
    print()
#Output
A
B C
D E F
G H I J 
K L M N O 
P Q R S T U


