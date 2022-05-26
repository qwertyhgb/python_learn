res = []
for i in range(0, 3):
    x = int(input("请输入整数:"))
    res.append(x)
for x in range(len(res)):
    for y in range(x, len(res)):
        if res[x] > res[y]:
            temp = res[y]
            res[y] = res[x]
            res[x] = temp

print(res)
