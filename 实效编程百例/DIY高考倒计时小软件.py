import datetime

print("高考倒计时")
now = datetime.datetime.today()
print(now)
print("今天是：", now.strftime("%Y-%m-%d %A "))
time1 = datetime.datetime(2022, 6, 7)
time2 = datetime.datetime(2023, 6, 7)
print("距离2022年高考还有" + str((time1 - now).days) + "天")
print("距离2023年高考还有" + str((time2 - now).days) + "天")
