### Functions ###

'''
Exercises: Level 1
Declare a function add_two_numbers. It takes two parameters and it returns a sum.
Area of a circle is calculated as follows: area = π x r x r. Write a function that calculates area_of_circle.
Write a function called add_all_nums which takes arbitrary number of arguments and sums all the arguments. Check if all 
the list items are number types. If not do give a reasonable feedback.
Temperature in °C can be converted to °F using this formula: °F = (°C x 9/5) + 32. Write a function which converts °C to °F, 
convert_celsius_to-fahrenheit.
Write a function called check-season, it takes a month parameter and returns the season: Autumn, Winter, Spring or Summer.
Write a function called calculate_slope which return the slope of a linear equation
Quadratic equation is calculated as follows: ax² + bx + c = 0. Write a function which calculates solution set of a 
quadratic equation, solve_quadratic_eqn.
Declare a function named print_list. It takes a list as a parameter and it prints out each element of the list.
'''

from data.countries import countries
from data.countries_data import countries_data
import math

def add_two_numbers(number_one, number_two):
    sum = number_one + number_two
    return sum
# print(add_two_numbers(2,3))

def area_of_circle(radio):
    area = math.pi * radio**2
    return area
# print(area_of_circle(2))

def add_all_nums(*nums):
    is_number = True
    sum = 0
    for i in nums:
        if not isinstance(i, int):
            print('All the values must be numbers')
            is_number = False
    if is_number:
        for i in nums:
            sum += i
        return sum
# print(add_all_nums(1,2,3))

def convert_celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * (9/5)) + 32
    return fahrenheit
# print(convert_celsius_to_fahrenheit(2))

def check_season(month):
    if month == 'September' or month == 'October' or month == 'November':
        return 'The season is Autumn'
    elif month == 'December' or month == 'January' or month == 'February':
        return 'The season is Winter'
    elif month == 'March' or month == 'April' or month == 'May':
        return 'The season is Spring'
    elif month == 'June' or month == 'July' or month == 'August':
        return 'The season is Summer'
# print(check_season('January'))

def calculate_slope(a, b):
    slope = -a/b
    return slope
# print(calculate_slope(10, 2))

def solve_quadratic_eqn(a, b, c):
    x1 = ((-b) + (b**2 -4*a*c)**0.5) / (2 * a)
    x2 = ((-b) - (b**2 -4*a*c)**0.5) / (2 * a)
    return x1, x2
# print(solve_quadratic_eqn(1,2,3))

def print_list(list):
    for i in list:
        print(i)
# print_list(['Hola', 'Chau'])


'''
Declare a function named reverse_list. It takes an array as a parameter and it returns the reverse of the array (use loops).
Declare a function named capitalize_list_items. It takes a list as a parameter and it returns a capitalized list of items
Declare a function named add_item. It takes a list and an item parameters. It returns a list with the item added at the end.
Declare a function named remove_item. It takes a list and an item parameters. It returns a list with the item removed from it.
Declare a function named sum_of_numbers. It takes a number parameter and it adds all the numbers in that range.
Declare a function named sum_of_odds. It takes a number parameter and it adds all the odd numbers in that range.
Declare a function named sum_of_even. It takes a number parameter and it adds all the even numbers in that - range.
'''

def reverse_list(my_list):
    my_list.sort(reverse=True)   
    return my_list
# print(reverse_list([1,2,3]))

def capitalize_list_items(my_list):
    counter = 0
    for i in my_list:
        my_list[counter] = i.capitalize()
        counter += 1
    return my_list
# print(capitalize_list_items(['hello', 'bye']))

def add_item(my_list, item):
    my_list.append(item)
    return my_list
# print(add_item(['Potato', 'Tomato', 'Mango', 'Milk'], 'Soap'))

def remove_item(my_list, item):
    counter = 0
    for i in my_list:
        if i == item:
            my_list.remove(my_list[counter])
        counter += 1
    return my_list
# print(remove_item([1,2,3], 2))

def sum_of_numbers(range):
    sum = 0
    counter = 0
    while counter <= range:
        sum += counter
        counter += 1
    return sum
# print(sum_of_numbers(5))

def sum_of_odds(range):
    sum = 0
    counter = 0
    while counter <= range:
        if counter % 2 != 0:
            sum += counter
        counter += 1
    return sum
# print(sum_of_odds(5))

def sum_of_even(range):
    sum = 0
    counter = 0
    while counter <= range:
        if counter % 2 == 0:
            sum += counter
        counter += 1
    return sum
# print(sum_of_even(5))

'''
Exercises: Level 2
Declare a function named evens_and_odds . It takes a positive integer as parameter and it counts number of evens and odds in the number.
Call your function factorial, it takes a whole number as a parameter and it return a factorial of the number
Call your function is_empty, it takes a parameter and it checks if it is empty or not
Write different functions which take lists. They should calculate_mean, 
calculate_median, calculate_mode, calculate_range, calculate_variance, calculate_std (standard deviation).
'''

def evens_and_odds(range):
    even_counter = 0
    odd_counter = 0
    counter = 0
    while counter <= range:
        if counter % 2 == 0:
            even_counter += 1
        else:
            odd_counter += 1
        counter += 1
    return {f'Even numbers: {even_counter}. Odd numbers: {odd_counter}'}
# print(evens_and_odds(100))

def factorial(number):
    counter = 1
    factorial = 1 
    while counter <= number:
        factorial = factorial * counter
        counter += 1
    return factorial
# print(factorial(4))

def is_empty(string):
    if string == '':
        return 'Is empty'
    else:
        return 'is not empty'
# print(is_empty(''))

def calculate_mean(my_list):
    mean = 0
    for i in my_list:
        mean += i
    mean = mean / len(my_list)
    return mean
# print(calculate_mean([1,2,3]))

def calculate_median(my_list):
    median = (len(my_list) + 1) / 2
    return median
# print(calculate_mean([1,2,3]))

def calculate_mode(my_list):
    frequency = {}
    numbers = []
    higher = 0

    my_list.sort(reverse=True)

    for i in my_list:
        if i not in numbers:
            frequency[i] = my_list.count(i)
            numbers.append(i)
    
    for i in frequency:
        if frequency.get(i) > higher:
            higher = frequency.get(i)
    mode = higher
    return mode
# print(calculate_mode([1,2,3,3,3]))
        
def calculate_variance(my_list): 
    mean = calculate_mean(my_list)
    sum_diff = 0

    for i in my_list:
        diff = (i - mean)**2
        sum_diff += diff
    diff = sum_diff / (len(my_list)-1)

    return diff
# print(calculate_variance([1,2,6]))

def calculate_std(my_list):
    variance = calculate_variance(my_list)
    std = variance ** 0.5
    return std
# print(calculate_std([1,2,3]))

'''
Exercises: Level 3
Write a function called is_prime, which checks if a number is prime.
Write a functions which checks if all items are unique in the list.
Write a function which checks if all the items of the list are of the same data type.
Go to the data folder and access the countries-data.py file.
Create a function called the most_spoken_languages in the world. It should return 10 or 20 most spoken languages in the world in descending order
Create a function called the most_populated_countries. It should return 10 or 20 most populated countries in descending order.
🎉 CONGRATULATIONS ! 🎉
'''

def is_prime(number):
    amount_of_divisors = 0
    counter = 1
    while counter <= number:
        if number % counter == 0:
            amount_of_divisors += 1
        counter += 1
    if amount_of_divisors != 2:
        return 'The number is not prime'
    else:
        return 'The number is prime'
# print(is_prime(8))

def unique_item(my_list):
    my_set = set(my_list)
    if len(my_list) != len(my_set):
        return 'The items are not unique'
    else:
        return 'The items are unique'
# print(unique_item([1,2,3,4,4]))

def same_data_type(my_list):
    same = True
    data_type = type(my_list[0])
    for i in my_list:
        if type(i) != data_type:
            same = False
    if same:
        return 'Items are the same data type'
    else:
        return 'Items are not the same data type'
# print(same_data_type([1,2,3]))

def most_spoken_languages():
    # Languages
    languages = list()
    for country in countries_data:
        languages.append(country['languages'])

    # Unique languages
    languages_set = set()
    languages_item_list = list()
    for language in languages:
        for item in language:
            languages_set.add(item)
            languages_item_list.append(item)


    language_counts = {}
    for lang in languages_item_list:
        language_counts[lang] = language_counts.get(lang, 0) + 1

    sorted_languages = sorted(language_counts.items(), key=lambda item: item[1], reverse=True)
    top_10_languages = sorted_languages[:10]

    print("Ten languages more spoken:")
    for lang, count in reversed(top_10_languages):
        print(f"- {lang}: {count} countries")

# most_spoken_languages()

def most_populated_countries():
    country_population = {}
    counter = 0
    for country in countries_data:
        country_population[country['name']] = country['population']   

    sorted_country_population = sorted(country_population.items(), key=lambda item: item[1], reverse=True)
    top_10_population = sorted_country_population[:10]
    print("Ten most populated countries:")
    for country, count in reversed(top_10_population):
        print(f"- {country}: {count}")

# most_populated_countries()