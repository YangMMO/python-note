def test01(a, b, callback):
    result = callback(a, b)
    print(type(callback))
    print(result)


def add(a, b):
    return a + b


# <class 'function'>
# 99
test01(33, 66, add)
