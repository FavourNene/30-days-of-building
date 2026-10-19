empty_tuple = ()
sis=( 'Gift', 'Regina')
bro =('Emmanuel', 'David', 'Isaac')
siblings = sis + bro
print(len(siblings))
family_members = siblings + ('Grace', 'Karimu', 'Zeenat')  
print(family_members)
*siblings, parent1, parent2, parent3 = family_members
fruits = ('Mango', 'Banana', 'Pineapple', 'Orange')
vegetables = ('Carrot', 'Cabbage', 'Spinach', 'Tomato', 'Pepper')
animal_products = ('Milk', 'Cheese', 'Yogurt', 'Butter')
food_stuff_tp = fruits + vegetables + animal_products
food_stuff_list = list(food_stuff_tp)
length = len(food_stuff_list)
mid = length //2
if length % 2 == 0:
    median = food_stuff_list[(mid -1): (mid+1)]
else:
    median = food_stuff_list[(mid-1)]
print(median)
first_three_last_three = food_stuff_list[0:3] + food_stuff_list[-3:]
print(first_three_last_three)