# 魔术方法为内置方法
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # str 魔术方法
    def __str__(self):
        return f"name = {self.age}, age = {self.age}"

    # lt 魔术方法 大小对比
    def __lt__(self, other):
        return self.age < other.age

    # le 魔术方法 大于等于、小于等于
    def __le__(self, other):
        return self.age <= other.age

    # eq 模式方法 ==比较
    def __eq__(self, other):
        return self.age == other.age




# str
# name = 18, age = 18
stu1 = Student("aaa", 18)
print(str(stu1))

# lt
# True
# False
stu1 = Student("aaa", 18)
stu2 = Student("bbb", 20)
print(stu1 < stu2)
print(stu1 > stu2)

# le
# True
# True
stu1 = Student("aaa", 20)
stu2 = Student("bbb", 20)
print(stu1 <= stu2)
print(stu1 >= stu2)

# eq
# True
# True
stu1 = Student("aaa", 20)
stu2 = Student("bbb", 20)
print(stu1 == stu2)
print(stu1 == stu2)
