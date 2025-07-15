### hello world ###

# Single line comment

"""This is multiline comment
multiline comment takes multiple lines.
python is eating the world
"""

# Day 1 - 30DaysOfPython Challenge

print(2 + 3)             # addition(+)
print(3 - 1)             # subtraction(-)
print(2 * 3)             # multiplication(*)
print(3 / 2)             # division(/)
print(3 ** 2)            # exponential(**)
print(3 % 2)             # modulus(%)
print(3 // 2)            # Floor division operator(//)

# Checking data types
print(type(10))          # Int
print(type(3.14))        # Float
print(type(1 + 3j))      # Complex number
print(type('Asabeneh'))  # String
print(type([1, 2, 3]))   # List
print(type({'name':'Asabeneh'})) # Dictionary
print(type({9.8, 3.14, 2.7}))    # Set
print(type((9.8, 3.14, 2.7)))    # Tuple

"""Exercise: Level 2
1. Check the python version you are using
2. Open the python interactive shell and do the following operations. The operands are 
3 and 4.
    addition(+)
    subtraction(-)
    multiplication(*)
    modulus(%)
    division(/)
    exponential(**)
    floor division operator(//)
3. Write strings on the python interactive shell. The strings are the following:
    Your name
    Your family name
    Your country
    I am enjoying 30 days of python
4. Check the data types of the following data:
    10
    9.8
    3.14
    4 - 4j
    ['Asabeneh', 'Python', 'Finland']
    Your name
    Your family name
    Your country"""

numberOne = 3
numberTwo = 4

addition = numberOne + numberTwo
subtraction = numberOne - numberTwo
multiplication = numberOne * numberTwo
modulus = numberOne % numberTwo
division = numberOne / numberTwo
exponential = numberOne ** numberTwo
floorDivision = numberOne // numberTwo

print('Lia')
print('family name')
print('Brasil')
print('I am enjoying 30 days of python')

print(type(10))
print(type(9.8))
print(type(3.14))
print(type(4 - 4j))
print(type(['Asabeneh', 'Python', 'Finland']))
print(type('Lia'))
print(type('family name'))
print(type('Brasil'))

# - - - - - - - - - - - - - - - - - - - - - - - - - - - -

"""Exercise: Level 3
Write an example for different Python data types such as Number(Integer, Float, Complex), String, Boolean, 
List, Tuple, Set and Dictionary.
Find an Euclidian distance between (2, 3) and (10, 8)"""

integer = 1
float = 1.1
complex = 4 - 4j
string = 'hi'
boolean = False
list = [1, 2, 3, False] # Different data types
tuple = (1, 2, '3') # Different and immutable data types
set = {1, 2, 3} # Store unique items, different data types
dictionary = {
    'name': 'Lucia',
    'age': 21
}

# Euclidian distance

x1 = 2
y1 = 3
x2 = 10
y2 = 8
euclidianDistance = ((x2-x1)**2 + (y2-y1)**2)**0.5
print(euclidianDistance)