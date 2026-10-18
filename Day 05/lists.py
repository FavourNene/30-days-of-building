lst = []
fruits = ['apple', 'banana', 'banana', 'date', 'pear', 'orange']
print(len(fruits))
print(fruits[0])
print(fruits[int(len(fruits)/2)-1])
print(fruits[-1])
mixed_data_types = ['Favour', 26, 1.62, False, 'Nigeria']
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
print(it_companies)
print(len(it_companies))
print(it_companies[0])
print(it_companies[int(len(it_companies)/2)-1])
print(it_companies[-1])
it_companies[0] = 'Meta'
print(it_companies)
print(it_companies.append('Twitter'))
it_companies[0] = it_companies[0].upper()
print(' # '.join(it_companies))
print('Facebook' in it_companies)
print(it_companies.sort())
print(it_companies.sort(reverse=True))
print(it_companies[0:3])
companies_length = len(it_companies)
if companies_length % 2 == 0:
    middle_index = companies_length // 2
    middle_companies = it_companies[middle_index - 1:middle_index + 1]
else:
    middle_index = companies_length // 2
    middle_companies = [it_companies[middle_index]]
print(middle_companies)
