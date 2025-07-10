fruits = set()
fruits = {'banana', 'orange', 'mango', 'lemon'}
fruits.add('apple')
fruits.update(['kiwi','strawberry','cherry'])
# print(fruits)

numbers = {1, 2, 3, 4, 5}
other_numbers = {4, 5, 6, 7}
# print(numbers.intersection(other_numbers))

st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
st2.issubset(st1) 
st1.issuperset(st2) 
# print(st2.difference(st1))
# print(st1.difference(st2))
# print(st2.symmetric_difference(st1))

'''
Exercises: Level 1
Find the length of the set it_companies
Add 'Twitter' to it_companies
Insert multiple IT companies at once to the set it_companies
Remove one of the companies from the set it_companies
What is the difference between remove and discard
Exercises: Level 2
Join A and B
Find A intersection B
Is A subset of B
Are A and B disjoint sets
Join A with B and B with A
What is the symmetric difference between A and B
Delete the sets completely
Exercises: Level 3
Convert the ages to a set and compare the length of the list and the set, which one is bigger?
Explain the difference between the following data types: string, list, tuple and set
I am a teacher and I love to inspire and teach people. How many unique words have been used in the sentence? Use the split 
methods and set to get the unique words.
🎉 CONGRATULATIONS ! 🎉
'''

it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

print(len(it_companies))
it_companies.add('Twitter')
it_companies.update(['Tesla', 'Meta'])
it_companies.remove('Tesla')
# Remove: If item is not in set, error. With discard there are no error

print(A.union(B))
print(A.symmetric_difference(B))
del A, B

my_set = set(age)
print(len(age) == len(my_set))
print(age)
print(my_set) # Unique items

# String: Chain of characters
# List: Mutable, ordered, repeated items
# Tuple: Immutable, ordered, repeated items
# Set: unique items, mutable

string = 'I am a teacher and I love to inspire and teach people'
print(string)
new_string = string.split()
print(new_string)
my_new_set = set(new_string)
print(my_new_set)
