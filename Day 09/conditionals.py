'''age = input("Enter your age: ")
if int(age) >= 18:
    print("You are old enough to drive.")
else:
    remaining_years = 18 - int(age)
    print(f"You need {remaining_years} more years to learn todrive.")

my_age = 26
your_age = input("Enter your age: ")
if int(my_age) > int(your_age):
    age_difference = int(my_age) - int(your_age)
    print(f"I am {age_difference} years older than you.")   
elif int(my_age) == int(your_age):
    print("Wow, we are the same age.")
elif int(my_age) < int(your_age):
    age_difference = int(your_age) - int(my_age)
    print(f"You are {age_difference} years older than me.") 
else:
    print("Invalid input. Please enter a valid age.")

num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")
if int(num1) > int(num2):
    print(f"{num1} is greater than {num2}.")
elif int(num1) < int(num2):
    print(f"{num1} is less than {num2}.")
else:
    print(f"{num1} is equal to {num2}.")
grades ={

range(90, 101): "A",
range(80, 90): "B",
range(70, 80): "C",
range(60, 70): "D",
range(0, 60): "F"
}

score = int(input("Enter your score: "))
for grade_range, grade in grades.items():
    if score in grade_range:
        print(f"Your grade is: {grade}")
        break
'''
seasons = {
    'Autumn' : ['September', 'October', 'November'],
    'Winter' :['December', 'January', 'February'],
    'Spring' : ['March', 'April', 'May'],
    'Summer': ['June', 'July', 'August']
}
'''month = input("Enter the month and I will tell you what season it is in: ")
month = month.title()
for key, value in seasons.items():
    if month in value:
        print(f'{month} is in {key}')

fruits = ['banana', 'orange', 'mango', 'lemon']
fruit = input("Enter a fruit name: ")
fruit = fruit.lower()
if fruit not in fruits:
    fruits.append(fruit)
else:
    print(f"{fruit} already exists")
print(fruits)
'''

person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
    }

'''if 'skills' in person:
        print("There is a key called 'Skills'.")
length = len(person['skills'])
mid = length // 2
if length % 2 == 0:
 print(f"The middle skills are:{person['skills'][mid -1]} and {person['skills'][mid]}")
else:
    print(f"The middle skill is: {person['skills'][mid]}")
if 'Python' in person['skills']:
    print("Python is present in the skills.")
'''

front_end = ["Javascript", "React"]
back_end = ["MongoDB","Node", "Python"]
full_stack =["React", "Node", "MongoDB"]

skills = person['skills']

skills = set(person['skills'])

if skills == {'JavaScript', 'React'}:
    print('He is a front end developer')
elif skills == {'Node', 'Python', 'MongoDB'}:
    print('He is a backend developer')
elif skills == {'React', 'Node', 'MongoDB'}:
    print('He is a fullstack developer')
else:
    print('unknown title')

if person['is_married'] and person['country'] == 'Finland':
    print(f'{person["first_name"]} {person["last_name"]} lives in {person["country"]}. He is married.')
else:
    print(f'{person["first_name"]} {person["last_name"]} lives in {person["country"]}. He is not married.')