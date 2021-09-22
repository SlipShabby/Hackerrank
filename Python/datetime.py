# calendar

import calendar
m, d, y = map(int,input().split())
print(list(calendar.day_name)[calendar.weekday(y, m, d)].upper())

# time delta

from datetime import datetime
for i in range(int(input())):
    t1=datetime.strptime(input(),'%a %d %b %Y %H:%M:%S %z')
    t2=datetime.strptime(input(),'%a %d %b %Y %H:%M:%S %z')
    print (int(abs((t1-t2).total_seconds())))

