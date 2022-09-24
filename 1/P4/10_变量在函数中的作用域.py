def test01():
    num = 0;
    print(num)

# print(num)    // error


num = 20


def test02():
    num = 200
    print(num)


def test03():
    global num
    num = 3000
    print(num)


test02()    # 40    内部重新定义了一个新的num属性，并非修改了全局的num
print(num)  # 20    全局变量值并未被修改
test03()    # 3000  因为global会使用全局的变量
