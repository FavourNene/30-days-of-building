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
A.isdisjoint(B)
D = B.union(A)
C.symmetric_difference(D)