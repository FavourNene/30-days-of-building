# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]
print("Length of the set it_companies:", len(it_companies))
it_companies.add('Twitter')
it_companies.update(['LinkedIn', 'Snapchat'])
it_companies.remove('IBM')
print("Updated set it_companies:", it_companies)
C = A.union(B)
c = A.intersection(B)
print("Is A disjoint from B?", A.isdisjoint(B))
D = B.union(A)

print("Symmetric difference of C and D:", C.symmetric_difference(D))
del A
del B
ages = set(age)
print("Is the length of the list age equal to the length of the set ages?", len(age) == len(ages))
sentence = "I am a teacher and I love to inspire and teach people."
words = sentence.split()
unique_words = set(words)
print("Number of unique words in the sentence:", len(unique_words))