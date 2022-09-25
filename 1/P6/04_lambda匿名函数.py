def test01(a, b, callback):
    result = callback(a, b)
    print(type(callback))
    print(result)


# 无法二次使用， 匿名函数
# lambda无法换行，自带return
# <class 'function'>
# -33
test01(33, 66, (lambda a, b: a - b))
