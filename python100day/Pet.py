import abc
from abc import ABCMeta


class Pet(object, metaclass=ABCMeta):  # 抽象类不能创建对象
    """宠物"""

    def __init__(self, nickname) -> None:
        self._nickname = nickname

    @abc.abstractmethod # 抽象方法子类必须继承
    def make_voice(self):
        """发出声音"""
        pass


class Dog(Pet):
    """狗
        Pet的子类"""

    def make_voice(self):
        print(self._nickname + ':汪汪。。。')


class Cat(Pet):
    """猫"""

    def make_voice(self):
        print(self._nickname + ':喵喵。。。')


def main():
    pets = [Dog('旺财'), Cat('凯蒂'), Dog('大黄')]
    for pet in pets:
        pet.make_voice()


if __name__ == '__main__':
    main()
