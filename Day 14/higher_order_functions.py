from functools import reduce
import re
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def square(num):
    return num ** 2

result = map(square, numbers)
print(list(result))

def  is_even(num):
    return num % 2 == 0

even_numbers = list(filter(is_even, numbers))
print(even_numbers)

def add(x, y):
    return x + y

sum = reduce(add, numbers)
print(sum)

countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']

for country in countries:
    print(country)

names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
for name in names:
    print(name)

for num in numbers:
    print(num)

countries_to_uppercase = list(map(lambda x: x.upper(), countries))
print(countries_to_uppercase)

numbers_squared = list(map(lambda x: x **2, numbers ))
print(numbers_squared)

names_to_upper = list(map(lambda x: x.upper(), names))
print(names_to_upper)

def has_land(country):
    if 'land' in country:
        return True
    return False

with_land = list(filter(has_land, countries))
print(with_land)

def is_long(country):
    if len(country)  > 5:
        return True
    return False

long_ones = list(filter(is_long, countries))
print(long_ones)

def start_with_e(country):
    country = country.lower()
    if country.startswith('e'):
        return True
    return False
starts_with= list(filter(start_with_e, countries))
print(starts_with)

result = map(square, filter(is_even, numbers))
print(list(result))

new_string = numbers + names + countries

def get_strings_list(lst):
    return list(filter(lambda x: isinstance(x, str), lst))

print(get_strings_list(new_string))

final_countries = reduce(lambda x, y: x + ', ' + y, countries)
print(final_countries)

def categorize_countries(pattern):
    result = filter(lambda country: pattern in country, countries)
    return list(result)
    

print(categorize_countries('land'))
print(categorize_countries('ia'))
print(categorize_countries('island'))
print(categorize_countries('stan'))

characters = 'abcdefghijklmnopqrstuvwxyz'

def countries_start_with_countries(characters):
    sorted_countries = {}

    for char in characters:
        result = filter(lambda country: country.lower().startswith(char), countries)
        length = len(list(result))
        sorted_countries[char] = length

    return sorted_countries

print(countries_start_with_countries(characters))

def get_first_ten_countries(countries):
    return countries[:10]

def get_last_ten_countries(countries):
    return countries[-10:]

sorted_countries = sorted(countries, key=lambda country: country['name'])

for country in sorted_countries:
    print(country['name'])

sorted_capitals = sorted(countries, key=lambda country: country['capital'])

for country in sorted_capitals:
    print(country['capital'])

sorted_population = sorted(countries, key=lambda country: country['population'])

for country in sorted_population:
    print(country['name'], country['population'])

sorted_population = sorted(
    countries,
    key=lambda country: country['population'],
    reverse=True
)

from collections import Counter

languages = []

for country in countries:
    for language in country['languages']:
        languages.append(language)

language_count = Counter(languages)

top_ten_languages = language_count.most_common(10)

print(top_ten_languages)

most_populated = sorted(
    countries,
    key=lambda country: country['population'],
    reverse=True
)

for country in most_populated[:10]:
    print(country['name'], country['population'])