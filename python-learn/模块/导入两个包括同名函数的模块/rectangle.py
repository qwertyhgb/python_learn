"""创建矩形模块"""

def girth(width, height):
    """计算周长"""
    return (width + height) * 2

def area(width, height):
    """计算面积"""
    return width * height

if __name__ == '__main__':
    print(area(10, 20))