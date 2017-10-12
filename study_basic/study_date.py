import datetime

d = datetime.datetime(1997, 3, 10)
print d

identity = '320322199703106814'

year = int(identity[6:10])
month = int(identity[10:12])
day = int(identity[12:14])
d1 = datetime.date(year, month, day)

print d1
