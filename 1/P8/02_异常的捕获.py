# 基本语法 但可以捕获所有异常
# try:
#     可能错误的代码
# except:
#     异常后执行的代码

try:
    f = open("E:/Code/python-note/1/P8/02.txt", "r", encoding="UTF-8")
except:
    print("error, not file, wirte file")
    f = open("E:/Code/python-note/1/P8/02.txt", "w", encoding="UTF-8")
print("__________")

# 捕获指定的异常
# 异常是多类型的
# print(name) # NameError: name 'name' is not defined
try:
    print(name)
    # 1 / 0
except NameError as e:  # e的名字随意填，e则代表error
    print("变量未定义的异常")
    print(e)    # 打印的是异常信息： name 'name' is not defined
print("__________")


# 捕获多个异常
try:
    print(name)
    1 / 0
except (NameError, ZeroDivisionError) as e:  # e的名字随意填，e则代表error
    print("变量未定义，或者 除以 0 的异常")
print("__________")

# 捕获所有异常的另一写法
# Exception
try:
    print(name)
    1 / 0
except Exception as e:  # e的名字随意填，e则代表error
    print("异常")
print("__________")


# 如果没有异常
try:
    print("666")
except:  # e的名字随意填，e则代表error
    print("异常")
else:
    print('good')
print("__________")


# 无论如何 始终执行
try:
    f = open("E:/Code/python-note/1/P8/error.txt", "r", encoding="UTF-8")
except:  # e的名字随意填，e则代表error
    print("异常")
else:
    print('good')
finally:
    print("close file")
    f.close()
print("__________")
