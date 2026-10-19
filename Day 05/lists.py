lst = []
fruits = ['apple', 'banana', 'banana', 'date', 'pear', 'orange']
print(len(fruits))
print(fruits[0])
middle_index = len(fruits) // 2
if len(fruits) % 2 == 0:
    print(fruits[middle_index - 1:middle_index + 1])
else:
    print(fruits[middle_index])
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
it_companies.append('Twitter')
print(it_companies)
it_companies[0] = it_companies[0].upper()
print(' # '.join(it_companies))
print('Facebook' in it_companies)
it_companies.sort()
print(it_companies)
it_companies.sort(reverse=True)
print(it_companies)
print(it_companies.sort(reverse=True))
print(it_companies[0:3])
print(it_companies[-3:])
companies_length = len(it_companies)
if companies_length % 2 == 0:
    middle_index = companies_length // 2
    middle_companies = it_companies[middle_index - 1:middle_index + 1]
    del it_companies[middle_index - 1:middle_index + 1]
else:
    middle_index = companies_length // 2
    middle_companies = [it_companies[middle_index]]
    del it_companies[middle_index]

print(it_companies)

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
fullstack = front_end + back_end
print(fullstack)
fullstack.insert(5, 'Python')
fullstack.insert(6, 'SQL')

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

max_age = sorted(ages)[-1]
min_age = sorted(ages)[0]
ages.append(max_age)
ages.append(min_age)
if len(ages) % 2 == 0:
    middle_index = len(ages) // 2
    median = (sorted(ages)[middle_index - 1] + sorted(ages)[middle_index]) / 2
else:
    middle_index = len(ages) // 2
    median = sorted(ages)[middle_index]
print(f"The median age is: {median}")
avg = sum(ages) / len(ages)
print(f"The average age is: {avg}")
age_range = max_age - min_age
print(f"The range of ages is: {age_range}")
comp = abs((min_age - avg) - (max_age - avg))
countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cabo Verde',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombia',
  'Comoros',
  'Congo, Democratic Republic of the',
  'Congo, Republic of the',
  'Costa Rica',
  "Côte d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor-Leste)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Eswatini',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Montenegro',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'North Macedonia',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Palestine',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent and the Grenadines',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'South Sudan',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Sweden',
  'Switzerland',
  'Syria',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe'
];
if len(countries) % 2 == 0:
    middle_index = len(countries) // 2
    middle_countries = countries[middle_index - 1:middle_index + 1]
else:
    middle_index = len(countries) // 2
    middle_countries = [countries[middle_index]]    
print(middle_countries)

first_half = countries[:len(countries)//2]
second_half = countries[len(countries)//2:]
lst2 =['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
ch, rs, us, sc = lst2
