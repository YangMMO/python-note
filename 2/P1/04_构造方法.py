class Student:
    # 可不写声明，因为构造时可直接声明并赋值
    # name = None
    # age = None
    # tel = None

    def __init__(self, name, age, tel):
        """
        构造
        :param name: 姓名
        :param age: 年龄
        :param tel: 电话
        """
        self.name = name
        self.age = age
        self.tel = tel


stu1 = Student("aaa", 18, "1894466")
print(stu1.name, stu1.age, stu1.tel)
