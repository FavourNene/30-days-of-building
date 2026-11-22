countries = ['Finland', 'Sweden', 'Norway', 'Denmark', 'Iceland']
for index, i in enumerate(countries):
    if i == 'Finland':
        print(f'The country {i} has been found at index {index}')
    position = index+ 1
    position = str(position)
    if position.endswith('1') and position != '11':
        print(f'The country {i} is at the {position}st position') 

names = ['Finland', 'Sweden', 'Norway','Denmark','Iceland', 'Estonia','Russia']
*nordic_countries, es, ru = names   # nordic_countries gets the first five

print(nordic_countries)  # ['Finland', 'Sweden', 'Norway', 'Denmark', 'Iceland']
print(es)                # Estonia
print(ru)                # Russia
