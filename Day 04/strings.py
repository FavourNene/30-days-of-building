strings = ['Thirty', 'Days', 'Of', 'Python']
result = ' '.join(strings)
print(result)
strings2 = ['Coding', 'For', 'All']
company = ' '.join(strings2)
print(company)
print(len(company))
print(company.upper())
print(company.lower())
print(company.capitalize())
print(company.title())
print(company.swapcase())
space_index = company.find(" ")
first_word = company[:space_index]
print(first_word)
print(company.find('Coding'))
print(company.replace('Python', 'Coding'))
text2 = "Python For Everyone"
print(text2.replace('Everyone', 'All'))
print(company.split(" "))
text3 = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(text3.split(","))
print(company[0])
print(len(company)-1)
print(company[10])
words = text2.replace('All', 'Everyone').split()
acronym = ""
for word in words:
    acronym += word[0]
print(acronym)
acronym2= ""
for word in strings2:
    acronym2 += word[0]
print(acronym2)
print(company.index('C'))
print(company.index('F'))
the_text = 'Coding For All People'
print(the_text.rfind('l'))
text = "Coding For All People"
sentence = 'You cannot end a sentence with because because because is a conjunction'
position = sentence.find('because')
print(position)
print(sentence.rfind('because'))