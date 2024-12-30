##Nehashri Prakash Dusa
##Python Lab2 Assignment

Q.1 Write a program for arithmatic operators
#Solution
a = 10
b = 5
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Modulus:", a % b)
print("Exponentiation:", a ** b)
print("Floor Division:", a // b)
#Output
Addition: 15
Subtraction: 5
Multiplication: 50
Division: 2.0
Modulus: 0
Exponentiation: 100000
Floor Division: 2

Q.2 Write a program for assignment operators
#Solution
x = 10
print("Initial value:", x)
x += 5
print("After x += 5:", x)
x -= 3
print("After x -= 3:", x)
x *= 2
print("After x *= 2:", x)
x /= 4
print("After x /= 4:", x)
x %= 3
print("After x %= 3:", x)
x **= 2
print("After x **= 2:", x)
#Output
Initial value: 10
After x += 5: 15
After x -= 3: 12
After x *= 2: 24
After x /= 4: 6.0
After x %= 3: 0.0
After x **= 2: 0.0

Q.3Write a program for Bitwise operators 
#Solution
x = 5  # Binary: 0101
y = 3  # Binary: 0011
print("Bitwise AND:", x & y)  # 0101 & 0011 = 0001 -> 1
print("Bitwise OR:", x | y)   # 0101 | 0011 = 0111 -> 7
print("Bitwise XOR:", x ^ y)  # 0101 ^ 0011 = 0110 -> 6
print("Bitwise NOT (~x):", ~x) # ~0101 = -0110 -> -6
print("Left Shift x << 2:", x << 2)  # 0101 << 2 = 10100 -> 20
print("Right Shift x >> 2:", x >> 2) # 0101 >> 2 = 0001 -> 1
#Output
Bitwise AND: 1
Bitwise OR: 7
Bitwise XOR: 6
Bitwise NOT (~x): -6
Left Shift x << 2: 20
Right Shift x >> 2: 1

Q.4 Write a program to calculate greatest of three numbers.
#Solution
a = 10
b = 15
c = 8
if a > b and a > c:
    print("Greatest number is:", a)
elif b > c:
    print("Greatest number is:", b)
else:
    print("Greatest number is:", c)
#Output
Greatest number is: 15

1.Calculate the area of a circle.
#Solution
import math
radius = 7
area_circle = math.pi * radius ** 2
print("Area of the circle:", area_circle)
#Output
Area of the circle: 153.93804002589985

2.Calculate the area of a triangle.
#Solution
base = 10
height = 5
area_triangle = 0.5 * base * height
print("Area of the triangle:", area_triangle)
#Output
Area of the triangle: 25.0

3.Calculate the area of a rectangle.
#Solution
length = 8
width = 4
area_rectangle = length * width
print("Area of the rectangle:", area_rectangle)
#Output
Area of the rectangle: 32

4.Calculate the area of a square.
#Solution
side = 6
area_square = side ** 2
print("Area of the square:", area_square)
#Output
Area of the square: 36




