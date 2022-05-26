# from rectangle import *
# from circular import *

# if __name__ == '__main__':
#     print("圆形的周长为:", girth(10))
#     print("矩形的周长为:", girth(10, 20))
import rectangle as r
import circular as c

if __name__ == '__main__':
    print("圆形的周长为:", c.girth(10))
    print("矩形的周长为:", r.girth(10, 20))