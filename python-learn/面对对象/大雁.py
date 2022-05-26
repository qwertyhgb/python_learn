class Geese:
    """创建一个大雁类"""
    neck = "脖子较长"
    wing = "振翅频率高"
    leg = "退位于身体的中心支点，行走自如"

    def __init__(self):
        print("我是一只大雁")
        print(self.neck)
        print(Geese.wing)
        print(self.leg)


A = Geese()
