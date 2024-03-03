from datetime import datetime, timedelta,  timezone
import re
# now = datetime.now()

# print(now)
# print(type(now))

# dt = datetime(2024, 2, 29, 6, 00)
# dt.timestamp()
# print(dt)

# t = 4546.0
# print(datetime.fromtimestamp(t))
# print(datetime.utcfromtimestamp(t))

# cday = datetime.strptime('2024-02-29 06:00:00', '%Y-%m-%d %H:%M:%S')
# print(cday)

# now = datetime.now()
# print(now.strftime('%a, %b %d %H:%M'))

# >>> now = datetime.now()
# >>> now
# datetime.datetime(2024, 3, 2, 22, 28, 7, 763493)
# >>> now + timedelta(hours = 5)
# datetime.datetime(2024, 3, 3, 3, 28, 7, 763493)
# >>> now
# datetime.datetime(2024, 3, 2, 22, 28, 7, 763493)
# >>> now - timedelta(days = 1)
# datetime.datetime(2024, 3, 1, 22, 28, 7, 763493)
# >>> now - timedelta(days = 1, hours = 2)
# datetime.datetime(2024, 3, 1, 20, 28, 7, 763493)

# tz_utc_8 = timezone(timedelta(hours = 8))
# now = datetime.now()
# now
# dt = now.replace(tzinfo = tz_utc_8)
# dt

# utc_dt = datetime.utcnow().replace(tzinfo = timezone.utc)
# print(utc_dt)
# BJ_dt = utc_dt.astimezone(timezone(timedelta(hours = 8)))
# print(BJ_dt)
# Tokyo_dt = utc_dt.astimezone(timezone(timedelta(hours = 9)))
# print(Tokyo_dt)
# Tokyo_dt2 = BJ_dt.astimezone(timezone(timedelta(hours = 9)))
# print(Tokyo_dt2)


def to_timestamp(dt_str, tz_str):
    dt = datetime.strptime(dt_str, '%Y-%m-%d %H:%M:%S')
    pattern = re.compile(r'^UTC([+-]*\s*\d+):(\d{2})$')
    match = pattern.match(tz_str)
    tz_hours = match.group(1)
    tz_minutes = match.group(2)
    tz = timezone(timedelta(hours = int(tz_hours), minutes = int(tz_minutes)))
    tz_dt = dt.replace(tzinfo = tz)
    test_timestamp = tz_dt.timestamp()
    print(test_timestamp)
    return test_timestamp
    

# 测试:
t1 = to_timestamp('2015-6-1 08:10:30', 'UTC+7:00')
assert t1 == 1433121030.0, t1

t2 = to_timestamp('2015-5-31 16:10:30', 'UTC-09:00')
assert t2 == 1433121030.0, t2

print('ok')