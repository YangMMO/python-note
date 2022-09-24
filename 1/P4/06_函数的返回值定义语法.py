def add(num1, num2):
    num1 + num2


def add1(num1, num2):
    return None


# 任何无返回的函数，都睡返回 None 字面量
print(add(6, 6))
# None字面量类型：<class 'NoneType'>
print(type(add(6, 6)))
print(type(add1(6, 6)))


if add(1, 1):
    print("123")

str1 = None
