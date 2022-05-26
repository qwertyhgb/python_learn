def dividion():
    """分苹果"""
    print('\n--------分苹果啦--------\n')
    apple = int(input('请输入苹果的数目:'))
    children = int(input('请输入孩子的数目:'))
    if children > apple:
        raise ValueError('苹果太少，不够分！')  # 用raise抛出异常
    result = apple // children  # 计算每个孩子分的几个苹果
    remain = apple - result * children  # 计算还剩几个苹果
    if remain > 0:
        print(str(apple) + '个苹果平均分给了' + str(children) + '个孩子,每人分' + str(result) + '个，还剩下' + str(remain) + '个.')
    else:
        print('苹果刚好平均分完不剩下。')

if __name__ == '__main__':
    try:
        dividion()
    except ZeroDivisionError:
        print('孩子的人数不能时零！')
    except ValueError:
        print('出错啦！')
    