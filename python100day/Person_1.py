class Person(object):
    """人"""

    def __init__(self, name, age):
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
        self._age = age

    def play(self):
        print(self._name + '正在愉快地玩耍.')

    def watch_av(self):
        if self._age >= 18:
            print(self._name + '正在观看av.')
        else:
            print(self._name + '正在看熊出没.')


class Student(Person):
    """学生
    Person的子类"""
    
    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self._grade = grade

    @property
    def grade(self):
        return self._garde

    @grade.setter # 修改器
    def grade(self, grade):
        self._grade = grade

    def study(self, course):
        print(self._grade + '的' + self._name + '正在学习' + course)


class Teacher(Person):
    """老师
    Person的子类"""

    def __init__(self, name, age, title):
        super().__init__(name, age)
        self._title = title

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        self._title = title

    def teach(self, course):
        print(self._name + self._title + '正在讲' + course)


def main():
    stu = Student('王大锤', 15, '初三')
    stu.study('数学')
    stu.watch_av()
    stu.age = 20
    stu.grade = '大一'
    stu.study('C语言')
    stu.watch_av()
    t = Teacher('李鸣', 21, '专家')
    t.teach('Python程序设计')
    t.watch_av()
    t.title = '超级无敌厉害专家'
    t.teach('java程序设计')
    


if __name__ == '__main__':
    main()



