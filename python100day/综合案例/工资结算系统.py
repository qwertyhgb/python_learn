"""
某公司有三种类型的员工 分别是部门经理、程序员和销售员
需要设计一个工资结算系统 根据提供的员工信息来计算月薪
部门经理的月薪是每月固定15000元
程序员的月薪按本月工作时间计算 每小时150元
销售员的月薪是1200元的底薪加上销售额5%的提成
"""
import abc
from abc import ABCMeta


class Employee(object, metaclass=ABCMeta):
    """员工"""

    def __init__(self, name) -> None:
        self._name = name

    @property
    def name(self):
        return self._name

    @abc.abstractmethod  # 抽象方法
    def get_salary(self):
        """获得月薪"""
        pass


class Manager(Employee):
    """部门经理"""

    def get_salary(self):
        return 15000.0


class Programmer(Employee):
    """程序员"""

    def __init__(self, name, working_hour=0) -> None:
        super().__init__(name)
        self._working_hour = working_hour

    @property
    def working_hour(self):
        return self._working_hour

    @working_hour.setter  # 修改器
    def working_hour(self, working_hour):
        self._working_hour = working_hour if working_hour > 0 else 0

    def get_salary(self):
        return 150.0 * self._working_hour


class Salesman(Employee):
    """销售员"""

    def __init__(self, name, sales=0) -> None:
        super().__init__(name)
        self._sales = sales

    @property
    def sales(self):
        return self._sales

    @sales.setter
    def sales(self, sales):
        self._sales = sales if sales > 0 else 0

    def get_salary(self):
        return 1200.0 + self._sales * 0.05


def main():
    emps = [
        Manager('刘备'), Programmer('诸葛亮'), Manager('曹操'), Salesman('荀彧'), Salesman("吕布"), Programmer('张辽'),
        Programmer("赵云")
    ]
    for emp in emps:
        if isinstance(emp, Programmer):  # 在python中，isinstance的意思是“判断类型”；isinstance()是一个内置函数，用于判断一个对象是否是一个已知的类型
            emp.working_hour = int(input('请输入' + emp.name + '本月工作的时间:'))
        elif isinstance(emp, Salesman):
            emp.sales = float(input('请输入' + emp.name + '本月销售额:'))
        print('%s本月工资为: ￥%s元' % (emp.name, emp.get_salary()))


if __name__ == '__main__':
    main()
