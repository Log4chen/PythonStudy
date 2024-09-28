from datetime import date, datetime, time, timezone
'''
类的继承关系
object
    timedelta
    tzinfo
        timezone
    time
    date
        datetime
'''
# 输出 2024-09-26
print(date.today())

d = date.fromisoformat('2024-09-26')

# 输出 2024-09-26 10:38:00.757203
dt = datetime.today()
print(dt)
print(dt.strftime('%Y-%m-%d %H:%M:%S'))
print(f'{dt.year}-{dt.month}-{dt.day}')



t = time(hour=13, minute=30, second=59)
print(t)
print(t.strftime('%H/%M/%S'))
tt = t.replace(hour=15)
print(tt)

print(tt > t)