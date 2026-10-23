# Day 2: 30 Days of python programming
first_name = 'Favour'
last_name = "Fache"
full_name = 'Favour Fache'
country = 'Nigeria'
city = 'Zaria'
age = 26
year = 2026
is_married = False
is_true = True
is_light_on = True
print(first_name)
a, b, c = 5, 10, 15

print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))

print(len(first_name))
print(len(last_name))
if len(first_name) > len(last_name):
    print("Your first name is longer than your last name.")
elif len(first_name) < len(last_name):
    print("Your last name is longer than your first name.")
else:
    print("Your first and last names have the same length.")

num_one = 5 
num_two = 4
total = num_one + num_two
diff = num_one - num_two
product = num_one * num_two
division = num_one / num_two
remainder = num_two % num_one
exp = num_one ** num_two
floor_division = num_one // num_two
area_of_circle = 3.14 * 30 ** 2
circum_of_circle = 2 * 3.14 * 30
radius = float(input("Enter the radius of the circle: "))
area = 3.14 * radius ** 2
print("The area of the circle is:", area)
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
country = input("Enter your country: ")
age = int(input("Enter your age: "))
