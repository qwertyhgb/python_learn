profit = int(input("利润是:"))
resualt = 0
a = [100000, 100000, 200000, 400000]
b = [0.1, 0.075, 0.05, 0.03, 0.015, 0.01]
for i in range(len(a)):
    if profit <= a[i]:
        resualt = a[i]*b[1]
        profit = 0
        break
    else:
        resualt += a[i]*b[i]
        profit -= a[i]
resualt += profit*b[-1]
print(resualt)

