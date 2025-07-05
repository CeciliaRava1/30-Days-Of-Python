# """
# Declare your age as integer variable
# Declare your height as a float variable
# Declare a variable that store a complex number
# Write a script that prompts the user to enter base and height of the triangle and calculate an area of this triangle (area = 0.5 x b x h).
# Write a script that prompts the user to enter side a, side b, and side c of the triangle. Calculate the perimeter of the triangle (perimeter = a + b + c).
# Get length and width of a rectangle using prompt. Calculate its area (area = length x width) and perimeter (perimeter = 2 x (length + width))
# Get radius of a circle using prompt. Calculate the area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14.
# """

# import math

# age: int = 21
# height: float = 1.23
# complexNumber = 4 + 2j

# print('Calculating the base of a triangle')
# baseTriangle = int(input('Enter base '))
# heightTriangle = int(input('Enter height '))
# areaTriangle = 0.5 * baseTriangle * height
# print('The area of the triangle is', areaTriangle)

# print('Calculating the perimeter of a triangle')
# sideA = int(input('Enter side a '))
# sideB = int(input('Enter side b '))
# sideC = int(input('Enter side c '))
# perimeterTriangle = sideA + sideB + sideC
# print('The perimeter of the triangle is', perimeterTriangle)

# print('Calculating about a rectangle')
# lengthRectangle = int(input('Enter length of a triangle'))
# widthRectangle = int(input('Enter width of a triangle'))
# areaRectangle = lengthRectangle * widthRectangle
# perimeterRectangle = 2 * (lengthRectangle + widthRectangle)
# print('The area of the rectangle is', areaRectangle)
# print('The perimeter of the rectangle is', perimeterRectangle)

# print('Calculating about a circle')
# radiusCircle = int(input('Enter radius of a circle'))
# areaCircle = math.pi * radiusCircle * radiusCircle
# circumferenceCircle = 2 * math.pi * radiusCircle
# print('The area of the circlee is', areaCircle)
# print('The circumference of the circlee is', circumferenceCircle)

# # Calculate the slope, x-intercept and y-intercept of y = 2x -2
# x = 0
# y = 2*x - 2
# slopeOne = 2

# if x == 0:
#     y_intercepto = y
# x_intercepto = -y_intercepto / slopeOne

# # Slope is (m = y2-y1/x2-x1). Find the slope and Euclidean distance between point (2, 2) and point (6,10)
# x1 = 2
# x2 = 6
# y1 = 2
# y2 = 10
# slopeTwo = (y2-y1) / (x2-x1)
# euclidianDistance = ((x2-x1)**2 + (y2-y1)**2)**0.5
# print(slopeOne == slopeTwo)

# # # Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values and figure out at what x value y is going to be 0.
# for x in range (-3,-1):
#     y = x**2 + 6*x + 9
#     print(y)

"""
Find the length of 'python' and 'dragon' and make a falsy comparison statement.
Use and operator to check if 'on' is found in both 'python' and 'dragon'
I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence.
There is no 'on' in both dragon and python
Find the length of the text python and convert the value to float and convert it to string
Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python?
"""

pythonLen = len('python')
dragonLen = len('dragon')
if pythonLen != dragonLen:
    print('The length is different')
else:
    print('The length is equal')

if 'on' in 'python' and 'dragon':
    print('On is in both words')

sentence = 'I hope this course is not full of jargon'
if 'jargon' in sentence:
    print('Jargon is in the sentence')

pythonLen = float(pythonLen)
print(type(pythonLen))
pythonLen = str(pythonLen)
print(type(pythonLen))

number = 0
if number % 2 == 0:
    print('The number is even')
else:
    print('The number is odd')

"""
Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.
Check if type of '10' is equal to type of 10
Check if int('9.8') is equal to 10
Writ a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?
Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live. Assume a person can live hundred years
Enter number of years you have lived: 100
You have lived for 3153600000 seconds.
Write a Python script that displays the following table
1 1 1 1 1
2 1 2 4 8
3 1 3 9 27
4 1 4 16 64
5 1 5 25 125
🎉 CONGRATULATIONS ! 🎉
"""

division = 7 / 3
print(division)
value = 2.7
if division == value:
    print('It is equal')
else:
    print('It is different')

if type(10) == type('10'):
    print('It is equal')
else:
    print('It is different')

hours = int(input('Enter hours'))
ratePerHour = int(input('Enter rate per hour'))
pay = hours * ratePerHour

correctInput = False
while not correctInput:
    numberOfYears = int(input('Enter number of years you have lived'))
    if numberOfYears <= 100:
        secondsPerYear = 31536000
        secondsLived = numberOfYears * secondsPerYear
        print('You have lived', secondsLived, ' seconds')
        correctInput = True
    else:
        print('You can not live more of 100 years')

# Write a Python script that displays the following table
# 1 1 1 1 1
# 2 1 2 4 8
# 3 1 3 9 27
# 4 1 4 16 64
# 5 1 5 25 125

for i in range(1, 6):
    print(i, 1, i, i**2, i**3)