### exception handling ###

'''
names = ['Finland', 'Sweden', 'Norway','Denmark','Iceland', 'Estonia','Russia']. 
Unpack the first five countries and store them in a variable nordic_countries, store Estonia and Russia in es, and ru respectively.
🎉 CONGRATULATIONS ! 🎉
'''
names = ['Finland', 'Sweden', 'Norway','Denmark','Iceland', 'Estonia','Russia']

try:
    *nordic_countries, es, ru = names
    print("Nordic Countries:", nordic_countries)
    print("Es:", es)
    print("Ru:", ru)
except ValueError as e:
    print(f"Error to unpack the list: {e}. The list must have 7 elements or more")