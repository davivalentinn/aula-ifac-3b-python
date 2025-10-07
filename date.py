import datetime

time = datetime.datetime.now()

# print(time)
# print(time.year)
# print(time.month)
# print(time.day)

if time.day == 7 and time.month == 10:
    print('Data é hoje')

else:
    print('Dia nao é hoje')