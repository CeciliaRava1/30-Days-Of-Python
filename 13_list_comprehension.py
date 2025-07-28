### list comprehension ###

# Meaning: Create new list from a sequence - [i for i in iterable if expression]

'''
💻 Exercises: Day 13
Filter only negative and zero in the list using list comprehension
Flatten the following list of lists of lists to a one dimensional list :
Using list comprehension create the following list of tuples:
Flatten the following list to a new list:
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
Change the following list to a list of dictionaries:
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]

Change the following list of lists to a list of concatenated strings:
names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
output
['Asabeneh Yetaeyeh', 'David Smith', 'Donald Trump', 'Bill Gates']

🎉 CONGRATULATIONS ! 🎉
'''

numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
filteredList = [i for i in numbers if i <= 0]
# print(filteredList)


list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
oneDimensionalList = [number for sublist_of_sublists in list_of_lists
                      for sublist in sublist_of_sublists
                      for number in sublist]
# print(oneDimensionalList)


newList = [(n, 1, n**1, n**2, n**3, n**4, n**5)
           for n in range(11)]
# for element in newList:
#     print(element)


countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
newCountriesList = [ [country.upper(), country[0:3].upper(), capital.upper()]
                     for sublist_of_sublist in countries 
                    for country, capital in sublist_of_sublist]
# print(newCountriesList)


countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
newDict = [ {'country': country.upper(), 'city': capital.upper()}
            for sublist_of_sublist in countries 
                    for country, capital in sublist_of_sublist]

# for element in newDict:
#     print(element)


names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
concatenatedList = [ (name + ' ' + surname)
                    for sublist in names
                    for name, surname in sublist]
# print(concatenatedList)

