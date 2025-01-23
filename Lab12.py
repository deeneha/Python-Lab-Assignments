##Nehashri Prakash Dusa
##Python Lab12 Assignment

1. Write a Python program to sum all the items in a list.
#Solution
def sum_of_list(lst):
    return sum(lst)
my_list = [10, 20, 30, 40]
result = sum_of_list(my_list)
print(result)
#Output
100

2.Write a Python program to traverse a given list in reverse order, and print the elements with the original index. 
Original list: ['red', 'green', 'white', 'black'] Traverse the said list in reverse order: black white green red
#Solution
def traverse_reverse(lst):
    for index, value in enumerate(reversed(lst)):
        print(f"Original Index: {len(lst) - 1 - index}, Element: {value}")
my_list = ['red', 'green', 'white', 'black']
traverse_reverse(my_list)
#Output
Original Index: 3, Element: black
Original Index: 2, Element: white
Original Index: 1, Element: green
Original Index: 0, Element: red
