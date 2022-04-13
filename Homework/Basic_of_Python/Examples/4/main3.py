import datetime

date_1 = datetime.datetime(year=2022, month=4, day=7, hour=22, minute=11)
print(date_1)
delta_t = datetime.timedelta(days=2, hours=1, minutes=33)
print(date_1 - delta_t)
print(date_1.timestamp())
date_2 = datetime.datetime(year=2018, month=9, day=6)
print(date_2 - date_1)
print(date_1.strftime('%d.%m.%Y %H:%M:%S'))
print(datetime.datetime.strptime("21/11/2006 16:30", "%d/%m/%Y %H:%M"))