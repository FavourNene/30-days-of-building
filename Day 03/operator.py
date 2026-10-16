'''age = 26

height = 1.62
complex_number = 3 + 4j
base =float(input("Enter the base of the triangle:"))
height=float(input("Enter the height of the triangle:"))
print("Area of the triangle is:", 0.5 * base * height)
side_a = float(input("Enter side a: "))
side_b = float(input("Enter side b: "))
side_c = float(input("Enter side c: "))
print("The perimeter of the triangle is", side_a + side_b + side_c)

length= float(input('Enter the length of the rectangle: '))
width = float(input('Enter the width of the rectangle: '))
print("The perimeter of the rectangle is:", 2 *(length + width))
print("The area of the rectangle is:", length * width)
radius = float(input("Enter the radius of the circle: "))
print( "The area of the circle is:", 3.14 * radius**2)
print("The circumference of the circle is:", 2 * 3.14 * radius)


slope8= 2
x_intercept = 1
y_intercept = -2

print("Slope 8:", slope8)
print("X-intercept:", x_intercept)
print("Y-intercept:", y_intercept)

import math

x1, y1 = 2, 2
x2, y2 = 6, 10

slope9 = (y2 - y1) / (x2 - x1)
distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
print("Slope 9:", slope9)
print("Euclidean distance:", distance)
print(slope9 > slope8)

print("The length of the word 'python' is: " ,len("python"))
print("The length of the word 'dragon' is: " ,len("dragon"))
print(len("python") < len("dragon"))
statement = "I hope this course is not full of jargon."
print("Is 'jargon' in the statement? ", "jargon" in statement)
print("Is 'on' in 'python' and 'dragon'? ", "on" in "python" and "on" in "dragon")
python_length = len("python")
python_length = float(python_length)
python_length = str(python_length)
print(type(python_length))
if num % 2 == 0:
    print(num, "is an even number.")
'''
f'''loor_div = 7//3
print(floor_div == 2.7)
print(type('10')==int(10))
print(int(9.8)==10)
hours = float(input("Enter hours: "))
rate_per_hour = float(input("Enter rate per hour: "))
weekly_earning = hours * rate_per_hour
print("Your weekly earning is", weekly_earning)
years = float(input("Enter number of years you have lived: "))
print("You have lived for", years * 365 * 24 * 60 * 60 * years,2"seconds.")'''

for n in range(1, 6):
    print(n, 1, n, n**2, n**3)