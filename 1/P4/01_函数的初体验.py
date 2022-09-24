str1 = "mmodsao"
str2 = "odsao"
str3 = "sao"


# 函数
def my_len(data):
    count = 0
    for i in data:
        count += 1

    print(count)


# 顺序执行，声明了函数，才能使用，当调用了函数，函数才会去执行内部
my_len(str1)
my_len(str2)
my_len(str3)
