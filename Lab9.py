##Nehashri Prakash Dusa
##Python Lab9 Assignment

1. Write a Python program to Count all letters, digits, and special symbols from the given string
Input = “P@#yn26at^&i5ve” 
Output: Chars = 8 Digits = 3 Symbol = 4 
#Solution
input_str = "P@#yn26at^&i5ve"
chars = digits = symbols = 0
for char in input_str:
    if char.isalpha():
        chars += 1
    elif char.isdigit():
        digits += 1
    else:
        symbols += 1
print(f"Chars = {chars}, Digits = {digits}, Symbols = {symbols}")
#Output
Chars = 8, Digits = 3, Symbols = 4

2. Write a Python program to remove duplicate characters of a given string.
Input = “String and String Function” 
Output: String and Function 
#Solution
input_str = "String and String Function"
result = ""
for char in input_str:
    if char not in result:
        result += char
print("Output:", result)
#Output
Output: String and Function

3. Write a Python program to count Uppercase, Lowercase, special character and numeric values in a given string
Input = “Hell0 W0rld ! 123 * # welcome to pYtHoN” 
Output: UpperCase : 5 LowerCase : 18 NumberCase : 5 SpecialCase : 11 
#Solution
input_str = "Hell0 W0rld ! 123 * # welcome to pYtHoN"
uppercase = lowercase = numbers = special = 0
for char in input_str:
    if char.isupper():
        uppercase += 1
    elif char.islower():
        lowercase += 1
    elif char.isdigit():
        numbers += 1
    else:
        special += 1
print(f"UpperCase: {uppercase}, LowerCase: {lowercase}, NumberCase: {numbers}, SpecialCase: {special}")
#Output
UpperCase: 5, LowerCase: 18, NumberCase: 5, SpecialCase: 11

4. Write a Python Count vowels in a string 
input= “Welcome to Python Assignment” 
Output: Total vowels are: 8
#Solution
input_str = "Welcome to Python Assignment"
vowels = "aeiou"
vowel_count = 0
for char in input_str.lower():
    if char in vowels:
        vowel_count += 1
print(f"Total vowels are: {vowel_count}")
#Output
Total vowels are: 8
