"""创建原形模块"""

import math

PI = math.pi

def girth(r):
    """计算周长"""
    return round(2 * PI * r, 2)

def area(r):
    """计算面积"""
    return round(PI * r * r, 2)

if __name__ == '__main__':
    print(girth(10))