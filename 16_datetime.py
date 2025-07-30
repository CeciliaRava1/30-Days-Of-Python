### datetime ###

'''
Get the current day, month, year, hour, minute and timestamp from datetime module
Format the current date using this format: "%m/%d/%Y, %H:%M:%S")

Today is 5 December, 2019. Change this time string to time.
Calculate the time difference between now and new year.
Calculate the time difference between 1 January 1970 and now.
Think, what can you use the datetime module for? 
    - Create a prompt to send messages in social media
    - Calculate birthdays
    - Calculate actual season
    - Save time of an event
🎉 CONGRATULATIONS ! 🎉
'''

from datetime import datetime
from datetime import date

now = datetime.now()
# print(now)                      
day = now.day                   
month = now.month              
year = now.year                
hour = now.hour                 
minute = now.minute             
second = now.second
timestamp = now.timestamp()
# print(day, month, year, hour, minute)
# print('timestamp', timestamp)
# print(f'{month}/{day}/{year}, {hour}:{minute}:{second}')  


date_string = "5 December, 2019"
# print("date_string =", date_string)
date_object = datetime.strptime(date_string, "%d %B, %Y")
# print("date_object =", date_object)


t1 = datetime.now()
t2 = datetime(year = 2026, month = 1, day = 1, hour = 0, minute = 0, second = 0)
diff = t2 - t1
# print('Time left for new year:', diff) 

t1 = datetime(year = 1970, month = 1, day = 1, hour = 0, minute = 00, second = 0)
t2 = datetime.now()
diff = t2 - t1
print('Difference betewwn today and 1/1/1970', diff)