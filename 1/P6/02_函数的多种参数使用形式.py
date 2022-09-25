def test01(name, age, gender):
    print(f"name: {name}, age: {age}, gender: {gender}")


# 关键字参数
test01("mmo", 16, "男")

test01(name="111", gender="男", age=11)

test01("222", age=44, gender="M")


# 缺省参数(默认值)
# 第一个写默认，后面都需要写默认
def test02(name=None, age=18, gender="M"):
    print(f"name: {name}, age: {age}, gender: {gender}")


test02()


# 不定长 位置传递 * 规范写法args
# 以元组存在
# (1, 2, 3)
# <class 'tuple'>
def test03(*args):
    print(f"{args}")
    print(type(args))


test03(1, 2, 3)


# 不定长 关键字传递 ** 规范写法kwargs
# 以字典存在
# {'a': 10, 'b': 20, 'c': 30}
# <class 'dict'>
def test04(**kwargs):
    print(f"{kwargs}")
    print(type(kwargs))


test04(a=10, b=20, c=30)

