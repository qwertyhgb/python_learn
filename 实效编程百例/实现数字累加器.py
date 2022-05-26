all = 0.0
addall = 0.0
indig = ""
"""设置两个浮点型数据"""

"""叠加算法"""


def add(addin, data):
    """判断是否为浮点数"""
    addone = addin + data
    return addone


def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass

    try:
        import unicodedata

        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass

    return False


while True:
    indig = input('输入:').strip("")
    if indig == 'q' or indig == 'Q':
        break  # 跳出循环
    elif is_number(indig):
        alladd = add(float(all), float(indig))
        all = format(alladd, '.2f')
        print(all)
    else:
        print("输入非法数字，请重新输入!!!!")
