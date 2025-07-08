my_tuple = tuple()
my_other_tuple = ()
fruits = ('banana', 'orange', 'mango', 'lemon')
all_items = fruits[0:]
print(all_items)

fruitsList = list(fruits)
print('banana' in fruits)

"""
Exercises: Level 1
Create an empty tuple
Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
Join brothers and sisters tuples and assign it to siblings
How many siblings do you have?
Modify the siblings tuple and add the name of your father and mother and assign it to family_members
Exercises: Level 2
Unpack siblings and parents from family_members
Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.
Change the about food_stuff_tp tuple to a food_stuff_lt list
Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
Slice out the first three items and the last three items from food_staff_lt list
Delete the food_staff_tp tuple completely
Check if an item exists in tuple:
Check if 'Estonia' is a nordic country
Check if 'Iceland' is a nordic country
"""

empty_tuple = tuple()
brothers = ('Manuel', 'Francisco')
sisters = ('Ludmila', 'Lucia')
siblings = brothers + sisters
print(len(siblings))

siblings += ('Fernando', 'Micaela')
family_members = siblings
print(family_members)

siblings = family_members[0:3]
parents_tuple = family_members[4:]
print(f'Siblings {siblings}')
print(f'Parents {parents_tuple}')

fruits = ('banana', 'apple')
vegetables = ('lettuce', 'potato')
animal_products = ('meal', 'milk')
food_stuff_tp = fruits + vegetables + animal_products
list_food = list(food_stuff_tp)
print(food_stuff_tp[round(len(food_stuff_tp)/2)])
print(list_food[0:3])
print(list_food[-3:])
del food_stuff_tp

nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print('Estonia' in nordic_countries)
print('Iceland' in nordic_countries)