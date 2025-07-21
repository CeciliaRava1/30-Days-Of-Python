### Modules ###

import random, string

def random_user_id():
    chars = string.ascii_letters + string.digits
    code = ''.join(random.choice(chars) for _ in range(6))
    return code   

def user_id_gen_by_user():
    codes = []
    id_length = int(input('Type the length of the ID'))
    amount_id = int(input('Type the amount of IDs to generate'))
    chars = string.ascii_letters + string.digits

    for i in range(amount_id):
        code = ''.join(random.choice(chars) for _ in range(id_length))
        codes.append(code)

    return codes

def rgb_color_gen():
    first_rgb = random.randint(0,255)
    second_rgb = random.randint(0,255)
    third_rgb = random.randint(0,255)
    return f'rgb {first_rgb, second_rgb, third_rgb}'

'''
Write a function list_of_hexa_colors which returns any number of hexadecimal colors in an array 
(six hexadecimal numbers written after #. Hexadecimal numeral system is made out of 16 symbols, 
0-9 and first 6 letters of the alphabet, a-f. Check the task 6 for output examples).
Write a function list_of_rgb_colors which returns any number of RGB colors in an array.
Write a function generate_colors which can generate any number of hexa or rgb colors.
'''

def list_of_hexa_colors(amount_hexa_colors):
    hexa_colors = []
    letters = 'abcdef'
    chars = letters + string.digits

    for i in range(amount_hexa_colors):
        hexa_color = '#' + ''.join(random.choice(chars) for _ in range(6))
        hexa_colors.append(hexa_color)
    
    return hexa_colors

def list_of_rgb_colors(amount_rgb_colors):
    rgb_colors = []
    for i in range(amount_rgb_colors):
        rgb_colors.append(rgb_color_gen())
    return rgb_colors

def generate_colors(amount_colors):
    colors = []
    letters = 'abcdef'
    chars = letters + string.digits

    for i in range(amount_colors):
        number = random.randint(0,1)
        if number == 0:
            colors.append(rgb_color_gen())
        else:
            hexa_color = '#' + ''.join(random.choice(chars) for _ in range(6))
            colors.append(hexa_color)
    
    return colors

'''
Call your function shuffle_list, it takes a list as a parameter and it returns a shuffled list
Write a function which returns an array of seven random numbers in a range of 0-9. All the numbers must be unique.
'''

def shuffle_list(my_list):
    random.shuffle(my_list)
    return my_list

def seven_random():
    numbers = []
    correct = False
    for i in range(7):
        correct = False
        while correct != True:
            number = random.randint(0,9)
            if number not in numbers:
                numbers.append(number)
                correct = True
    return numbers
