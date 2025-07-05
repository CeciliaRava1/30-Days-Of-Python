"""
Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.
Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.
Declare a variable named company and assign it to an initial value "Coding For All".
Print the variable company using print().
Print the length of the company string using len() method and print().
Change all the characters to uppercase letters using upper() method.
Change all the characters to lowercase letters using lower() method.
Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.
Cut(slice) out the first word of Coding For All string.
Check if Coding For All string contains a word Coding using the method index, find or other methods.
Replace the word coding in the string 'Coding For All' to Python.
Change Python for Everyone to Python for All using the replace method or other methods.
Split the string 'Coding For All' using space as the separator (split()) .
"Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.
"""

singleString = 'Thirty' + ' days' + ' of' + ' Python'
singleStringTwo = 'Coding' + ' for' + ' all'
company = "Coding For All"
# print(company)
# print(len(company))
# company = company.upper()
# company = company.lower()
# company = company.capitalize()
# company = company.title()
# company = company.swapcase()
# # print(company[0:1])
# print(company.find('Coding'))
company= company.replace("Coding", "python")
# print(company)
# newString = 'Python for Everyone'
# newString = newString.replace("Everyone", "all")
# print(newString)
company = 'Coding For All'
# print(company.split())
# string = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
# print(string.split(','))

"""
What is the character at index 0 in the string Coding For All.
What is the last index of the string Coding For All.
What character is at index 10 in "Coding For All" string.
Create an acronym or an abbreviation for the name 'Python For Everyone'.
Create an acronym or an abbreviation for the name 'Coding For All'.
Use index to determine the position of the first occurrence of C in Coding For All.
Use index to determine the position of the first occurrence of F in Coding For All.
Use rfind to determine the position of the last occurrence of l in Coding For All People.
Use index or find to find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a 
sentence with because because because is a conjunction'
Use rindex to find the position of the last occurrence of the word because in the following sentence: 'You cannot end a 
sentence with because because because is a conjunction'
"""

# print(company[0:1])
# print(company[-1])
# print(company[10])
# string = 'Python For Everyone'
# words = string.split() 
# acronym = ''.join(word[0] for word in words)
# print(words)
# print(acronym)
# string = 'Coding For All'
# words = string.split() 
# acronym = ''.join(word[0] for word in words)
# print(words)
# print(acronym)

# print(string.find('C'))  
# print(string.find('F')) 
# print(string.rfind('l'))  

sentence = 'You cannot end a sentence with because because because is a conjunction'
# print(sentence.find('because'))  
# print(sentence.rfind('because'))

"""
Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because 
is a conjunction'
Does ''Coding For All' start with a substring Coding?
Does 'Coding For All' end with a substring coding?
'   Coding For All      '  , remove the left and right trailing spaces in the given string.
Which one of the following variables return True when we use the method isidentifier():
30DaysOfPython
thirty_days_of_python
The following list contains the names of some of python libraries: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Join the list 
with a hash with space string.
Use the new line escape sequence to separate the following sentences.
I am enjoying this challenge.
I just wonder what is next.
Use a tab escape sequence to write the following lines.
Name      Age     Country   City
Asabeneh  250     Finland   Helsinki
Use the string formatting method to display the following:
radius = 10
area = 3.14 * radius ** 2
The area of a circle with radius 10 is 314 meters square.
Make the following using string formatting methods:
8 + 6 = 14
8 - 6 = 2
8 * 6 = 48
8 / 6 = 1.33
8 % 6 = 2
8 // 6 = 1
8 ** 6 = 262144
🎉 CONGRATULATIONS ! 🎉
"""

# words = sentence.split()
# print(sentence)
newString = ''
# for word in words:
#     if word != 'because':
#         newString += word + ' '
# print(newString)

# print(company.startswith('Coding')) 
# print(company.endswith('coding')) 

string = '   Coding For All      '
words = string.split()
for word in words:
    newString += word + ' '
print(newString)

stringOne = '30DaysOfPython'
stringTwo = 'thirty_days_of_python'
print(stringOne.isidentifier())
print(stringTwo.isidentifier())

list = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
newList = ' '.join(list)
print(newList)

print('I am enjoying this challenge. \nI just wonder what is next.')
print('Name \t\tAge \tCountry \tCity \nAsabeneh \t250 \tFinland \tHelsinki')

radius = 10
area = 3.14 * radius ** 2
print(f'The area of a circle with radius {radius} is {area} meters square')
print('8 + 6 = 14 \n8 - 6 = 2 \n8 * 6 = 48 \n8 / 6 = 1.33 \n8 % 6 = 2 \n8 // 6 = 1 \n8 ** 6 = 262144')
