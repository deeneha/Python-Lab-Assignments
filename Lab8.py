##Nehashri Prakash Dusa
##Python Lab8 Assignment

1. Write a Python program to count the occurrences of each word in a given sentence
string = “To change the overall look of your document. To change the look available in the gallery”
#Solution
string = "To change the overall look of your document. To change the look available in the gallery"
word_count = {}
for word in string.split():
    word = word.strip('.').lower()  # Remove punctuation and convert to lowercase
    word_count[word] = word_count.get(word, 0) + 1
print("Word occurrences:")
for word, count in word_count.items():
    print(f"{word}: {count}")
#Output
Word occurrences:
to: 2
change: 2
the: 3
overall: 1
look: 2
of: 1
your: 1
document: 1
available: 1
in: 1
gallery: 1

2. Write a Python program to remove a newline in Python
String = "\nBest \nDeeptech \nPython \nTraining\n"
#Solution
string = "\nBest \nDeeptech \nPython \nTraining\n"
cleaned_string = string.replace("\n", " ")
print("Original String:")
print(string)
print("\nString after removing newlines:")
print(cleaned_string)
#Output
Original String:
Best 
Deeptech 
Python 
Training

String after removing newlines:
 Best  Deeptech  Python  Training 

3. Write a Python program to reverse words in a string
String = “Deeptech Python Training”
#Solution
string = "Deeptech Python Training"
reversed_string = " ".join(string.split()[::-1])
print("Original String:", string)
print("Reversed String:", reversed_string)
#Output
Original String: Deeptech Python Training
Reversed String: Training Python Deeptech

4. Write a Python program to count and display the vowels of a given text
String=”Welcome to python Training”
#Solution
string = "Welcome to python Training"
vowels = "aeiou"
vowel_count = {v: 0 for v in vowels}
for char in string.lower():
    if char in vowels:
        vowel_count[char] += 1
print("Vowel counts:")
for vowel, count in vowel_count.items():
    print(f"{vowel}: {count}")
#Output
Vowel counts:
a: 1
e: 3
i: 2
o: 3
u: 0

