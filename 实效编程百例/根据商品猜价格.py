list = [['小米手环', 209], ['荣耀手环5', 199], ['智能血压手环', 379], ['华为手环', 849]]
price = 0
print('即将开始猜价格游戏！！！！！！')
print('可以竞猜的物品有:')
print('1', list[0][0], '\n2', list[1][0], '\n3', list[2][0], '\n4', list[3][0])
number = int(input('请输入要猜测的商品:'))
try:
    if 4 >= number > 0:
        print('你选的商品是%s' % list[number - 1][0])
        price = list[number - 1][1]
        guess = -1
        while guess != price:
            guess = int(input('请输入你的猜想:'))
            if guess < price:
                print('很遗憾，你猜小了！！！')
            if guess > price:
                print('很遗憾，你猜大了！！！')
            if guess == price:
                print('恭喜你，你猜对了！！！！！！！！！！！😀')
    elif number > 4:
        print('你输入的数过大，请输入小于或等于4的数！！')
except ValueError:
    print('你输错啦请重新尝试！！！😔')
