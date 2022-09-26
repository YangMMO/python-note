def func1():
    print("1 开始执行")
    num = 1 / 0     # /0的异常
    print("1 结束执行")


def func2():
    print("2 开始执行")
    func1()
    print("2 结束执行")


def main():
    # print("main 开始执行")

    # func2()

    try:
        func2()
    except Exception as err:
        print(f"异常信息： {err}")

    print("main 结束执行")


main()

# 最底层传递至最顶层
# Traceback (most recent call last):
#   File "E:\Code\python-note\1\P8\03_异常的传递性.py", line 19, in <module>
#     main()
#   File "E:\Code\python-note\1\P8\03_异常的传递性.py", line 15, in main
#     func2()
#   File "E:\Code\python-note\1\P8\03_异常的传递性.py", line 9, in func2
#     func1()
#   File "E:\Code\python-note\1\P8\03_异常的传递性.py", line 3, in func1
#     num = 1 / 0     # /0的异常
# ZeroDivisionError: division by zero
#
# 进程已结束,退出代码1


# 捕获后
# 异常信息： division by zero