class Person(object):

    # 限定Person 对象只能绑定_name, _age, _gender属性
    __slots__ = ('_name', '_age', '_gender')

    def __init__(self, name, age) -> None:
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        return self._age

    def play(self):
        if self._age <= 16:
            print(self._name + '正在完飞行器')
        else:
            print(self._name + '正在玩斗地主')


def main():
    person = Person('王大锤', 22)
    person.play()
    person._gender = '男'


if __name__ == '__main__':
    main()