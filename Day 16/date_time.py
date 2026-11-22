from datetime import date, datetime, timedelta
print(f'{datetime.now()} - Timestamp: {datetime.now().timestamp()}')
now = datetime.now()
print(now.strftime("%m/%d/%Y, %H:%M:%S"))

T = date(2019, 12, 5)
print(T)


t1 = datetime.now()
t2 =datetime(2027,1,1)
diff = t2 - t1
print(f'The amount of time between now and new year is: {diff.days} days, {diff.seconds} seconds, {diff.microseconds} microseconds')
t3 = datetime(1970, 1, 1)
diff2= t1-t3
print(f'The amount of time between now and 1970 is: {diff2.days} days, {diff2.seconds} seconds, {diff2.microseconds} microseconds')