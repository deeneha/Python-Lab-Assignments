##Nehashri Prakash Dusa
##Python Lab16 Assignment

Convert the below list into numpy array then display the array
Input: my_list = [1, 2, 3, 4, 5] 
#solution
import numpy as np
my_list = np.array([1, 2, 3, 4, 5])
print(my_list)
#output
[1 2 3 4 5]

Convert the below list into a numpy array then display the array then display the first and last index and then multiply each element by 2 and display the result.
Input: my_list = [1, 2, 3, 4, 5]
#solution
import numpy as np
my_list=np.array([1,2,3,4,5])
print(my_list)
print("First element:", my_list[0])
print("Second element:",my_list[-1])
multiply = my_list * 2
print(multiply)
#output
[1 2 3 4 5]
First element: 1
Second element: 5
[ 2  4  6  8 10]