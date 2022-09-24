def func2():
    print("2")


def func():
    print("1")

    func2()

    print("3")


func()