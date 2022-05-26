class Friut:
    """创建一个水果类"""

    color = None

    def __init__(self, color='绿色') -> None:
        Friut.color = color  # 定义一个类属性
        print("你好!")

    def harvest(self):
        print("水果原来是" + str(Friut.color) + "的！")


class Apple(Friut):
    """创建Friut的子类Apple"""

    def __init__(self, color) -> None:
        self._color = color
        print("我是苹果")
        super().__init__(color=self._color)  # 子类要调用父类的__init__方法要使用super()来调用


class Orange(Friut):
    """"""

    def __init__(self, color) -> None:
        print("我是橘子")
        super().__init__(color)

    def harvest(self, tast):
        print("橘子的味道是" + str(tast) + "的！")
        return super().harvest()


apple = Apple("红色")
apple.harvest()
orange = Orange("黄色")
orange.harvest("酸")
