### regular expressions ###

'''
Exercises: Level 1
What is the most frequent word in the following paragraph?
'''

import re
from operator import itemgetter

paragraph = 'I love teaching. If you do not love teaching what else can you love. I love Python if you do not love ' \
'something which can give you all the capabilities to develop an application what else can you love.'
lowerParagraph = paragraph.lower()

words = re.findall(r'\b\w+\b', paragraph)
newDict = {}

for word in words:
    counter = words.count(word)
    newDict[word] = counter
sorted_dict = dict(sorted(newDict.items(), key=itemgetter(1), reverse=True))
list_keys = list(sorted_dict.keys())
# print(f'The most frequent word is: {list_keys[0]}')


'''
The position of some particles on the horizontal x-axis are -12, -4, -3 and -1 in the negative direction, 0 at origin, 
4 and 8 in the positive direction. Extract these numbers from this whole text and find the distance between the two furthest particles.
'''

points = ['-12', '-4', '-3', '-1', '0', '4', '8']