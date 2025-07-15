### conditionals ###

'''
Exercises: Level 1
Get user input using input(“Enter your age: ”). If user is 18 or older, give feedback: You are old enough to drive. 
If below 18 give feedback to wait for the missing amount of years. 
Compare the values of my_age and your_age using if … else. Who is older (me or you)? Use input(“Enter your age: ”) 
to get the age as input. You can use a nested condition to print 'year' for 1 year difference in age, 'years' for bigger 
differences, and a custom text if my_age = your_age. 
Get two numbers from the user using input prompt. If a is greater than b return a is greater than b, 
if a is less b return a is smaller than b, else a is equal to b. Output:
Enter number one: 4
Enter number two: 3
4 is greater than 3
'''

# age = int(input('Enter your age: '))
# if age >= 18:
#     print('You are old enough to learn to drive.')
# else:
#     print('You need 3 more years to learn to drive.')


# my_age = int(input('Enter your age: '))
# your_age = int(input('Enter your age: '))

# if my_age > your_age:
#     difference = my_age - your_age
#     print(f'You are {difference} years younger than me.')
# else:
#     difference = your_age - my_age
#     print(f'You are {difference} years older than me.')


# number_one = int(input('Enter number one: '))
# number_two = int(input('Enter number two: '))

# if number_one > number_two:
#     print(f'{number_one} is greater than {number_two}')
# elif number_two > number_one:
#     print(f'{number_one} is smaller than {number_two}')
# else:
#     print(f'{number_one} is equal to {number_two}')


'''
Exercises: Level 2
Write a code which gives grade to students according to theirs scores:
80-100, A
70-89, B
60-69, C
50-59, D
0-49, F
Check if the season is Autumn, Winter, Spring or Summer. If the user input is: September, October or November, the season is Autumn. 
December, January or February, the season is Winter. 
March, April or May, the season is Spring 
June, July or August, the season is Summer
The following list contains some fruits:
fruits = ['banana', 'orange', 'mango', 'lemon']
If a fruit doesn't exist in the list add the fruit to the list and print the modified list. 
If the fruit exists print('That fruit already exist in the list')
'''

# student_score = int(input('Enter your score: '))
# if student_score >= 80 and student_score <= 100:
#     print('Your code is A')
# elif student_score >= 70 and student_score <= 89:
#     print('Your code is B')
# elif student_score >= 60 and student_score <= 69:
#     print('Your code is C')
# elif student_score >= 50 and student_score <= 59:
#     print('Your code is D')
# elif student_score >= 0 and student_score <= 49:
#     print('Your code is F')


# month = str(input('Type a month to know the season'))
# if month == 'September' or month == 'October' or month == 'November':
#     print('The season is Autumn')
# elif month == 'December' or month == 'January' or month == 'February':
#     print('The season is Winter')
# elif month == 'March' or month == 'April' or month == 'May':
#     print('The season is Spring')
# elif month == 'June' or month == 'July' or month == 'August':
#     print('The season is Summer')


# fruits = ['banana', 'orange', 'mango', 'lemon']
# fruit = str(input('Enter a fruit to add: '))
# if fruit in fruits:
#     print('That fruit already exist in the list')
# else:
#     fruits.append(fruit)
#     print(fruits)


'''
Exercises: Level 3
Here we have a person dictionary. Feel free to modify it!
        person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
    }
 * Check if the person dictionary has skills key, if so print out the middle skill in the skills list.
 * Check if the person dictionary has skills key, if so check if the person has 'Python' skill and print out the result.
 * If a person skills has only JavaScript and React, print('He is a front end developer'), 
 if the person skills has Node, Python, MongoDB, print('He is a backend developer'), 
 if the person skills has React, Node and MongoDB, Print('He is a fullstack developer'), 
 else print('unknown title') - for more accurate results more conditions can be nested!

 * If the person is married and if he lives in Finland, print the information in the following format:
    Asabeneh Yetayeh lives in Finland. He is married.
🎉 CONGRATULATIONS ! 🎉
'''

person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    # 'skills': ['React', 'JavaScript'],
    # 'skills': ['Node', 'Python', 'MongoDB'],
    'skills': ['Node', 'React', 'MongoDB'],
    # 'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}

if person.get('skills'):
    length = round(len(person.get('skills'))/2)
    print(person.get('skills')[length])

if 'Python' in person.get('skills'):
    print('The skills contains Python')

listLength = len(person.get('skills'))
if ('Node' in person.get('skills') and 'React' in person.get('skills') and 'MongoDB' in person.get('skills') and 'Python' in person.get('skills') and 'JavaScript' in person.get('skills')):
    print('She is a fullstack developer (con Python y JS)')
elif ('Node' in person.get('skills') and 'React' in person.get('skills') and 'MongoDB' in person.get('skills')): 
    print('She is a fullstack developer')
elif ('JavaScript' in person.get('skills') and 'React' in person.get('skills') and listLength == 2):
    print('She is a front end developer')
elif ('Node' in person.get('skills') and 'Python' in person.get('skills') and 'MongoDB' in person.get('skills')):
    print('She is a backend developer')
else:
    print('unknown title')

if person['is_marred']:
    print(f'{person['first_name']} {person["last_name"]} lives in {person['country']}. He is married')
else:
    print(f'{person['first_name']} {person["last_name"]} lives in {person['country']}.')

