class Person(object):

    def __init__(self, name, age) -> None:
        self._name = name
        self._age = age

    # 访问器 - getter方法
    @property
    def name(self):
        return self._name

    # 访问器 - getter方法
    @property
    def age(self):
        return self._age

    # 修改器 - setter方法
    @age.setter
    def age(self, age):
        self._age = age

    # 修改器 -setter方法
    @name.setter
    def name(self, name):
        self._name = name
        
    def play(self):
        if self._age <= 16:
            print(self._name + "正在玩飞行棋.")
        else:
            print(self._name + '正在玩斗地主.')


def main():
    person = Person('王大锤', 12)
    person.play()
    person.name = '李鸣'
    person.age = 22
    person.play()


if __name__ == '__main__':
    main()
