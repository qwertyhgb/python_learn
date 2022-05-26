def way():
    number = int(input('请输入一个三位数:'))
    a = int(number/100)
    b = int(number % 100 / 10)
    c = int(number % 10)
    return c * 100 + b * 10 + a


class Solution:
    """反转一个三位数"""


if __name__ == '__main__':
    solution = Solution()
    result = way()
    print(result)
