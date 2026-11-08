numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
negative_numbers = [num for num in numbers if num <= 0]
print(negative_numbers)

list_of_lists =[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
the_list = [num for sublist in list_of_lists for num in sublist]
print(the_list)


nums = [(i, 1, i, i**2, i**3, i**4, i**5) for i in range(11)]
print(*nums, sep='\n')

countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
for country in countries:
    for name, city in country:
        output = [name.upper(), name[:3].upper(), city.upper()]   
        print(output) 

countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]

output = [{'country': name, 'capital': city}
          for country in countries
          for name, city in country]

print(output)

names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
output = [' '.join(name) for sublist in names for name in sublist]
print(output)
slope = lambda x1, y1, x2, y2: (y2-y1)/(x2-x1)


y_intercept = lambda x, y, m: y - (m*x)
print(y_intercept(2, 7, 2))