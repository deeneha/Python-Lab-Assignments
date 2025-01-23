##Nehashri Prakash Dusa
##Python Lab15 Assignment

1. Write a Python program to Get Only unique items from two sets. 
Input: set1 = {10, 20, 30, 40, 50} set2 = {30, 40, 50, 60, 70} 
Output: {70, 40, 10, 50, 20, 60, 30}
#Solution
def unique_items(set1, set2):
    return set1.union(set2)

# Input sets
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

result = unique_items(set1, set2)
print(result)
#Output
{70, 40, 10, 50, 20, 60, 30}

 2. Write a Python program to Return a set of elements present in Set A or B, but not both. 
 Input: set1 = {10, 20, 30, 40, 50} set2 = {30, 40, 50, 60, 70} 
 Output: {20, 70, 10, 60}
#Solution
def symmetric_difference(set1, set2):
    return set1.symmetric_difference(set2)
# Input sets
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
result = symmetric_difference(set1, set2)
print(result)
#Output
{20, 70, 10, 60}
