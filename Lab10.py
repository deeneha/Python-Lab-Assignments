##Nehashri Prakash Dusa
##Python Lab10 Assignment


1. Write a function in python to read the content from a text file "ABC.txt" line by line and display the same on screen. 
#Solution
def read_file():
    try:
        with open("ABC.txt", "r") as file:
            for line in file:
                print(line.strip())
    except FileNotFoundError:
        print("File not found.")
#Assuming "ABC.txt"
Hello World
Welcome to Python
This is a file
#Output
Hello World
Welcome to Python
This is a file

2. Write a function in Python to count and display the total number of words in a text file “ABC.txt”
#Solution
def count_words():
    try:
        with open("ABC.txt", "r") as file:
            word_count = 0
            for line in file:
                words = line.split()
                word_count += len(words)
            print(f"Total number of words: {word_count}")
    except FileNotFoundError:
        print("File not found.")
#Output
Total number of words: 7

3. Write a function in Python to count uppercase character in a text file “ABC.txt”
#Solution
def count_uppercase():
    try:
        with open("ABC.txt", "r") as file:
            uppercase_count = 0
            for line in file:
                uppercase_count += sum(1 for char in line if char.isupper())
            print(f"Total number of uppercase characters: {uppercase_count}")
    except FileNotFoundError:
        print("File not found.")
#Output
Total number of uppercase characters: 6

4. Write a function display_words() in python to read lines from a text file "story.txt", and display those words, which are less than 4 characters.
#Solution
def display_words():
    try:
        with open("story.txt", "r") as file:
            for line in file:
                words = line.split()
                for word in words:
                    if len(word) < 4:
                        print(word)
    except FileNotFoundError:
        print("File not found.")
#Output
is
a
is
fun
Run
