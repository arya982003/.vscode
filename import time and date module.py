import time
localtime =time.asctime(time.localtime(time.time()))
print('local time:-')
print(localtime)
from datetime import date
mydate=date(2022,3,15)
print('my date:-')
print(mydate)
a=date.today()
print('today date:-')
print(a)
