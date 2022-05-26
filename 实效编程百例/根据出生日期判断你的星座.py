sdate = [20, 19, 21, 20, 21, 22, 23, 23, 23, 24, 23, 22]  # 星座判断列表
conts = ['水瓶座', '双鱼座', '白羊座', '金牛座', '双子座', '巨蟹座', '狮子座', '处女座', '天秤座', '天蝎座', '射手座', '摩羯座']
signs = ['♒', '♓', '♈', '♉', '♊', '♋', '♌', '♍', '♎', '♏', '♐', '♑']

# 输入生日，输出星座
birth = input('请输入你的出生年月日(格式为:2001-01-01):\n').strip(' ')
"""Python strip() 方法用于移除字符串头尾指定的字符（默认为空格或换行符）或字符序列。
    注意：该方法只能删除开头或是结尾的字符，不能删除中间部分的字符。
    """
cbir = birth.split('-')
"""
    split() 通过指定分隔符对字符串进行切片，如果参数 num 有指定值，则分隔 num+1 个子字符串
    x = 2001-01-01
    y = x.split('-')
    y = [2001, 01, 01]
    """
cmonth = str(cbir[1])
cdate = str(cbir[2])


def sign(cmonth, cdate):
    if int(cdate) < sdate[int(cmonth) - 1]:
        print(conts[int(cmonth) - 1])
        print(signs[int(cmonth) - 1])
    else:
        print(conts[int(cmonth)])
        print(signs[int(cmonth)])


sign(cmonth, cdate)
