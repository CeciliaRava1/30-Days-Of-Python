empty_dict = {}
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
print(dct['key1']) 
print(dct['key4']) 
dct.pop('key1')
print(dct)

keys = dct.keys()
print(keys)
values = dct.values()
print(values)

person = {
    'first_name':'Asabeneh',
    'last_name':'Yetayeh',
    'age':250,
    'country':'Finland',
    'is_marred':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
    }
print(person.get('first_name'))
person['job_title'] = 'Instructor'
person['skills'].append('HTML')
print(person)

'''
Create an empty dictionary called dog
Add name, color, breed, legs, age to the dog dictionary
Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address 
as keys for the dictionary
Get the length of the student dictionary
Get the value of skills and check the data type, it should be a list
Modify the skills values by adding one or two skills
Get the dictionary keys as a list
Get the dictionary values as a list
Change the dictionary to a list of tuples using items() method
Delete one of the items in the dictionary
Delete one of the dictionaries
🎉 CONGRATULATIONS ! 🎉
'''

dog = {}
dog = {'name':'Coco', 'color':'Black','breed':'Pointer', 'legs':4, 'age':1}
student = {
    'first_name':'Paola', 
    'last_name':'Lopez', 
    'gender':'female', 
    'age': 20, 
    'marital_status':'married',
    'skills': ['Python', 'SQL', 'Javascript'],
    'country':'Spain',
    'city':'Galicia'}

print(len(student))
print(student['skills'])
student['skills'].append('HTML')
student['skills'].append('CSS')
student_keys = student.keys()
student_values = student.values()

dict_list = dct.items()
student.pop('last_name')
del student

