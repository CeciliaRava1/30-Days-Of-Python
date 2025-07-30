### higher order functions ###

from data.countries import countries
from data.countries_data import countries_data


# countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

'''
Exercises: Level 1
Explain the difference between map, filter, and reduce.
    - Map: Transform items in an iterable
    - Filter: Filter items in an iterable with a condition
    - Reduce: Applies a function to the items of a iterable

Explain the difference between higher order function, closure and decorator
    - Higher order function: Takes a function as an argument or returns a function
    - Closure: Function that has access to its own scope, even when the function is executed outside that scope
    - Decorator: Type of higher order function used to modify or extend the behavior of another function without changing its 
    original code

Define a call function before map, filter or reduce, see examples.
Use for loop to print each country in the countries list.
'''

def sum_one(number):
    return number + 1
numbers_sum = map(sum_one, numbers)
# print(list(numbers_sum))


# for country in countries:
#     print(country)

'''

Exercises: Level 2
Use map to create a new list by changing each country to uppercase in the countries list
Use map to create a new list by changing each number to its square in the numbers list
Use map to change each name to uppercase in the names list
Use filter to filter out countries containing 'land'.
Use filter to filter out countries having exactly six characters.
Use filter to filter out countries containing six letters and more in the country list.
Use filter to filter out countries starting with an 'E'
Chain two or more list iterators (eg. arr.map(callback).filter(callback).reduce(callback))
'''

def to_upper(country):
    return country.upper()
uppercase_countries = map(to_upper, countries)
# print(list(uppercase_countries))

def squared(number):
    return number ** 2
squared_numbers = map(squared, numbers)
# print(list(squared_numbers))

def name_to_upper(name):
    return name.upper()
uppercase_names = map(name_to_upper, names)
# print(list(uppercase_names))

def have_land(country):
    if 'land' in country:
        return True
    else:
        return False
countries_with_land = filter(have_land, countries)
# print(list(countries_with_land))

def is_six_char(country):
    if len(country) == 6:
        return True
    else:
        return False
countries_six_char = filter(is_six_char, countries)
# print(list(countries_six_char))

def is_six_or_more_char(country):
    if is_six_char(country) or len(country) > 6:
        return True
    else:
        return False
countries_six_or_more_char = filter(is_six_or_more_char, countries)
# print(list(countries_six_or_more_char))


def start_with_e(country):
    if country[0] == 'E':
        return True
    else:
        return False
countries_start_with_e = filter(start_with_e, countries)
# print(list(countries_start_with_e))

numbers_higher_two = list(map(squared, filter(lambda x: x > 2, numbers))) # 1. Filter, 2. Map
# print(numbers_higher_two)


'''
Declare a function called get_string_lists which takes a list as a parameter and then returns a list containing only string items.
Use reduce to sum all the numbers in the numbers list.
Use reduce to concatenate all the countries and to produce this sentence: 
Estonia, Finland, Sweden, Denmark, Norway, and Iceland are north European countries
Declare a function called categorize_countries that returns a list of countries with some common pattern 
Create a function returning a dictionary, where keys stand for starting letters of countries and values are the number 
of country names starting with that letter.
Declare a get_first_ten_countries function - it returns a list of first ten countries from the countries.js list in the data folder.
Declare a get_last_ten_countries function that returns the last ten countries in the countries list.
'''


from functools import reduce

def get_string_list(element):
    if type(element) == str:
        return True
    else:
        return False

my_list = [1, 2, 'hello', 'bye', 5]
string_list = filter(get_string_list, my_list)
# print(list(string_list))


sum = reduce(lambda x, y: x + y, numbers)
# print(sum)


# countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
concatenated_countries = reduce(lambda x, y: x + ', ' + y, countries)
# print(concatenated_countries)


def categorize_countries(country):
    if 'land' in country:
        return True
    else:
        return False
countries_with_land = filter(categorize_countries, countries)
# print(list(countries_with_land))


def starts_with(countries):
    newDict = {}
    counter = 0
    alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    for letter in alphabet:
        counter = 0
        for country in countries:
            firstLetter = country.startswith(letter)
            if firstLetter:
                counter += 1
        newDict[letter] = counter
    return newDict  
# print(starts_with(countries))


def get_first_ten_countries(countries):
    for country in countries[0:10]:
        print(country)
# (get_first_ten_countries(countries))


def get_last_ten_countries(countries):
    for country in countries[-10:]:
        print(country)
# get_last_ten_countries(countries)


'''
Exercises: Level 3
Sort countries
    by capital
    by population
🎉 CONGRATULATIONS ! 🎉
'''


def sort_capital(countries):
    capitals = {}
    for country in countries_data:
        if country['capital'] != '':
            capitals[country['capital']] = country['name']
    sorted_dict = dict(sorted(capitals.items()))
    return sorted_dict
# print(sort_capital(countries_data))

def sort_population(countries):
    population = {}
    for country in countries_data:
        population[country['population']] = country['name']
    sorted_dict = dict(sorted(population.items(), reverse=True))
    return sorted_dict
# print(sort_population(countries_data))


