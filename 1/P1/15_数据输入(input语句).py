# print("请输入：")
# str1 = input()
#
# print("输入了：%s" % str1)


# 可直接写成
# 注意： 无论输入什么， 都转为字符串类型
str1 = input("请输入：\n")
print("输入了：%s" % str1)
print("type: ", (str1))

# 转换类型输入
str1 = input("请输入：\n")
str1 = int(str1)    # 转换
print("输入了：%s" % str1)
print("type: ", type(str1))

