### loops ###

from data.countries import countries
from data.countries_data import countries_data


'''
Exercises: Level 1
Iterate 0 to 10 using for loop, do the same using while loop.
Iterate 10 to 0 using for loop, do the same using while loop.
Write a loop that makes seven calls to print(), so we get on the output the following triangle:

  #
  ##
  ###
  ####
  #####
  ######
  #######
Use nested loops to create the following:

# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
Print the following pattern:

0 x 0 = 0
1 x 1 = 1
2 x 2 = 4
3 x 3 = 9
4 x 4 = 16
5 x 5 = 25
6 x 6 = 36
7 x 7 = 49
8 x 8 = 64
9 x 9 = 81
10 x 10 = 100
Iterate through the list, ['Python', 'Numpy','Pandas','Django', 'Flask'] using a for loop and print out the items.

Use for loop to iterate from 0 to 100 and print only even numbers

Use for loop to iterate from 0 to 100 and print only odd numbers

Exercises: Level 2
Use for loop to iterate from 0 to 100 and print the sum of all numbers.
The sum of all numbers is 5050.
Use for loop to iterate from 0 to 100 and print the sum of all evens and the sum of all odds.

The sum of all evens is 2550. And the sum of all odds is 2500.
Exercises: Level 3
Go to the data folder and use the countries.py file. Loop through the countries and extract all the countries containing the word land.
This is a fruit list, ['banana', 'orange', 'mango', 'lemon'] reverse the order using loop.
Go to the data folder and use the countries_data.py file.
What are the total number of languages in the data
Find the ten most spoken languages from the data
Find the 10 most populated countries in the world
🎉 CONGRATULATIONS ! 🎉
'''

# for i in range (11):
#     print(i)

# i = 0
# while i <= 10:
#     print(i)
#     i += 1

# for i in range (10, -1, -1):
#     print(i)

# i = 10
# while i != 0:
#     print(i)
#     i -= 1

# str = '#'
# for i in range (7):
#     print(str)
#     str += '#'

# for i in range (8):
#     for j in range(8):
#         print('# ', end='')
#     print()

# for i in range (11):
#     print(f'{i} x {i} = {i*i}')

# my_list = ['Python', 'Numpy','Pandas','Django', 'Flask'] 
# for i in my_list:
#     print(i)

# for i in range (101):
#     if i % 2 == 0:
#         print(i)

# for i in range (101):
#     if i % 2 != 0:
#         print(i)

sum = 0
for i in range (101):
    sum += i
print(f'The sum of all numbers is {sum}.')

sum_even = 0
sum_odd = 0
for i in range (101):
    if i % 2 == 0:
        sum_even += i
    else:
        sum_odd += i
print(f'The sum of all evens is {sum_even}. And the sum of all odds is {sum_odd}.')

for country in countries:
    if 'land' in country:
        print(country)

fruits = ['banana', 'orange', 'mango', 'lemon']
for i in range(len(fruits)-1, -1, -1):
    print(fruits[i])

# Languages
languages = list()
for country in countries_data:
    languages.append(country['languages'])
# print(languages)

# Unique languages
languages_set = set()
languages_item_list = list()
for language in languages:
    for item in language:
        languages_set.add(item)
        languages_item_list.append(item)

# Ten languages more spoken
language_counts = {}
for lang in languages_item_list:
    language_counts[lang] = language_counts.get(lang, 0) + 1

sorted_languages = sorted(language_counts.items(), key=lambda item: item[1], reverse=True)
top_10_languages = sorted_languages[:10]

print("Ten languages more spoken:")
for lang, count in top_10_languages:
    print(f"- {lang}: {count} countries")

# 10 most populated countries in the world
country_population = {}
counter = 0
for country in countries_data:
    country_population[country['name']] = country['population']   
print(country_population)

sorted_country_population = sorted(country_population.items(), key=lambda item: item[1], reverse=True)
top_10_population = sorted_country_population[:10]
print("Ten most populated countries:")
for country, count in top_10_population:
     print(f"- {country}: {count}")
    

# # Ten languages more spoken
# language_counts = {}
# for lang in languages_item_list:
#     language_counts[lang] = language_counts.get(lang, 0) + 1

# sorted_languages = sorted(language_counts.items(), key=lambda item: item[1], reverse=True)
# top_10_languages = sorted_languages[:10]

# print("Ten languages more spoken:")
# for lang, count in top_10_languages:
#     print(f"- {lang}: {count} countries")