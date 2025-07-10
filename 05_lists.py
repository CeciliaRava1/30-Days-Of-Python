"""
List:  collection ordered and modifiable. Allows duplicate members.
Tuple: collection ordered and immutable. Allows duplicate members.
Set:   collection unordered, un-indexed and unmodifiable, but we can add new items to the set. Duplicate members are not allowed.
Dictionary: collection unordered, modifiable and indexed. No duplicate members.
"""


my_list = list() 
my_other_list =  ['Asabeneh', 250, True, {'country':'Finland', 'city':'Helsinki'}] 
# print(my_other_list[1:2])

my_list.append('hello')
my_list.append('world')
my_list.insert(0, 'bye')
my_list.remove('hello')
my_list.pop()
# print(my_list)

my_new_list = my_list.copy()
# print(my_new_list)
my_list.clear()
del my_list

list1 = ['item1', 'item2']
list2 = ['item3', 'item4', 'item5']
list1.extend(list2)
list1.reverse()
# print(list1)

ages = [22, 19, 24, 25, 26, 24, 25, 24]
# print(ages.count(24))           
ages = [22, 19, 24, 25, 26, 24, 25, 24]
# print(ages.index(24))     

# ages.sort()                
# print(ages)
ages.sort(reverse=True)    
# print(ages)



"""
Exercises: Level 1
Declare an empty list
Declare a list with more than 5 items
Find the length of your list
Get the first item, the middle item and the last item of the list
Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
Print the list using print()
Print the number of companies in the list
Print the first, middle and last company
Print the list after modifying one of the companies
Add an IT company to it_companies
Insert an IT company in the middle of the companies list
Change one of the it_companies names to uppercase (IBM excluded!)
Join the it_companies with a string '#;  '
Check if a certain company exists in the it_companies list.
Sort the list using sort() method
Reverse the list in descending order using reverse() method
Slice out the first 3 companies from the list
Slice out the last 3 companies from the list
Slice out the middle IT company or companies from the list
Remove the first IT company from the list
Remove the middle IT company or companies from the list
Remove the last IT company from the list
Remove all IT companies from the list
Destroy the IT companies list
Join the following lists:
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
After joining the lists. Copy the joined list and assign it to a variable full_stack, then insert Python and SQL after Redux.
"""

list = list()
list = [1, 2, 3, 4, 5, 6]
# print(len(list))
# print(f'First item: {list[0]}')
# print(f'Middle item: {list[round(len(list)/2)]}')
# print(f'Last item: {list[-1]}')

mixed_data_types = ['micaela', 18, 150, 'married', 'adress']
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
# print(it_companies)
# print(len(it_companies))
# print(f'First company: {it_companies[0]}')
# print(f'Middle company: {it_companies[round(len(list)/2)]}')
# print(f'Last company: {it_companies[-1]}')

it_companies.pop()
it_companies.append('Dell')
it_companies.insert(round(len(list)/2), 'Meta')
it_companies[0] = it_companies[0].upper()
# it_companies.extend('#;  ')
# print('Google' in it_companies)
it_companies.sort()
it_companies.sort(reverse=True)   

# print(it_companies) 
# print(it_companies[0:3])
# print(it_companies[5:8])
# print(it_companies[round(len(list)/2)])
it_companies.remove(it_companies[0])
it_companies.remove(it_companies[round(len(list)/2)])
it_companies.remove(it_companies[-1])
it_companies.clear()
del it_companies

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
front_end.extend(back_end)

full_stack = front_end.copy()
full_stack.insert(full_stack.index('Redux')+1,'Python')
full_stack.insert(full_stack.index('Redux')+2, 'SQL')
# print(full_stack)

"""
Exercises: Level 2
The following is a list of 10 students ages:
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
Sort the list and find the min and max age
Add the min age and the max age again to the list
Find the median age (one middle item or two middle items divided by two)
Find the average age (sum of all items divided by their number )
Find the range of the ages (max minus min)
Compare the value of (min - average) and (max - average), use abs() method
Find the middle country(ies) in the countries list
Divide the countries list into two equal lists if it is even if not one more country for the first half.
['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']. Unpack the first three countries and the rest as scandic countries.
🎉 CONGRATULATIONS ! 🎉
"""

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
minAge = ages[0]
maxAge = ages[-1]
print(minAge, maxAge)
ages.append(minAge)
ages.append(maxAge)
print(ages)

medianAge = ages[round(len(ages)/2)]/2
print(f'Median age: {medianAge}')
averageAge = 0
for i in ages:
    averageAge += i
averageAge = averageAge / len(ages)
print(f'Average age: {averageAge}')
rangeAges = maxAge - minAge
print({abs(minAge-averageAge)} == {abs(maxAge-averageAge)})

countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Cape Verde',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombi',
  'Comoros',
  'Congo (Brazzaville)',
  'Congo',
  'Costa Rica',
  "Cote d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor Timur)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia, The',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Macedonia',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia and Montenegro',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Swaziland',
  'Sweden',
  'Switzerland',
  'Syria',
  'Taiwan',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe',
]

middle = round(len(countries)/2)
print(countries[middle])
new_list = countries[0:middle]
countries = countries[middle:-1]\

countriesEven = len(countries) % 2 == 0
if countriesEven != True:
    new_list.append(countries[0])
    countries.remove(countries[0])

print(new_list)
print(' ')
print(countries)

countriesTwo = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
scandic_countries = countriesTwo[3:]
print(scandic_countries)