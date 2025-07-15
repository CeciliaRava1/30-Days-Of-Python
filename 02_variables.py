### variables ###

"""Python Variable Name Rules
- A variable name must start with a letter or the underscore character
- A variable name cannot start with a number
- A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
- Variable names are case-sensitive (firstname, Firstname, FirstName and FIRSTNAME) are different variables)
- snake_case
"""

""" Exercises level 1
1. Inside this folder create a file named variables.py
2. Write a python comment saying 'Day 2: 30 Days of python programming'
3. Declare a first name variable and assign a value to it
4. Declare a last name variable and assign a value to it
5. Declare a full name variable and assign a value to it
6. Declare a country variable and assign a value to it
7. Declare a city variable and assign a value to it
8. Declare an age variable and assign a value to it
9. Declare a year variable and assign a value to it
10. Declare a variable is_married and assign a value to it
11. Declare a variable is_true and assign a value to it
12. Declare a variable is_light_on and assign a value to it
13. Declare multiple variable on one line
"""

# Day 2: 30 Days of python programming
first_name = 'Giuliana'
last_name = 'Hernandez'
full_name = 'Micaela Lopez'
country = 'Bolivia'
city = 'Trinidad'
age = 19
year = 2020
is_married = True
is_true = True
is_light_on = False
favoriteColor, favoriteDay = 'green', 'tuesday'
# print(favoriteColor)
# print(favoriteDay)


"""Exercises: Level 2
1. Check the data type of all your variables using type() built-in function
2. Using the len() built-in function, find the length of your first name
3. Compare the length of your first name and your last name
4. Declare 5 as num_one and 4 as num_two
5. Add num_one and num_two and assign the value to a variable total
6. Subtract num_two from num_one and assign the value to a variable diff
7. Multiply num_two and num_one and assign the value to a variable product
8. Divide num_one by num_two and assign the value to a variable division
9. Use modulus division to find num_two divided by num_one and assign the value to a variable remainder
10. Calculate num_one to the power of num_two and assign the value to a variable exp
11. Find floor division of num_one by num_two and assign the value to a variable floor_division
12. The radius of a circle is 30 meters.
13. Calculate the area of a circle and assign the value to a variable name of area_of_circle
14. Calculate the circumference of a circle and assign the value to a variable name of circum_of_circle
15. Take radius as user input and calculate the area.
16. Use the built-in input function to get first name, last name, country and age from a user and store the value to their corresponding variable names
17. Run help('keywords') in Python shell or in your file to check for the Python reserved words or keywords
"""

import math

print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_light_on))
print(type(favoriteDay))

print('Length of the name:', len(first_name))
print(len(first_name) != len(last_name))

num_one = 5
num_two = 4
total = num_one + num_two
diff = num_one - num_two
product = num_two * num_one
division = num_two / num_one
remainder = num_two % num_one
exp = num_one ** num_two
floor_division = num_one // num_two

radius = 30
area_of_circle = math.pi * radius**2
radius = int(input('Type the radius of a circle '))
print('This is the new radius:', radius)

first_name = str(input('Type your first name '))
last_name = str(input('Type your last name '))
country = str(input('Type your country '))
age = int(input('Type your age '))

import keyword
print(keyword.kwlist)

# 🎉 CONGRATULATIONS ! 🎉
