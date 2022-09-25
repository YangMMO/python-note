# [开始下标, 结束下标(默认不包含下标自身), 步幅长度默认1]
# 注意： 切片是返回自身相同的类型

# 对list进行切片，从1开始，4结束，步长1
# 1 2 3
list1 = [0, 1, 2, 3, 4, 5, 6, 7, 8]
new_list1 = list1[1: 4]
print(new_list1)
print(type(new_list1))

# 对tuple进行切片，从头开始，到最后结束，步长1
tup1 = (0, 1, 2, 3, 4, 5, 6, 7, 8)
new_tup1 = tup1[:]
print(new_tup1)
print(type(new_tup1))

# 对str进行切片，从头开始，到最后结束，步长2
# MOFN
str1 = "MMOOFUN"
new_str1 = str1[::2]
print(new_str1)
print(type(new_str1))

# 对str进行切片，从头开始，到最后结束，步长-1
# NUFOOMM   注意： 使用-会反序列切
str2 = "MMOOFUN"
new_str2 = str1[::-1]
print(new_str2)
print(type(new_str2))

# 对列表进行切片，从3开始，到1结束，步长-1
# 3 2
list2 = [0, 1, 2, 3, 4, 5, 6, 7, 8]
new_list2 = list1[3: 1: -1]
print(new_list2)
print(type(new_list2))

# 对元组进行切片，从头开始，到尾结束，步长-2
# 8 6 4 2 0
tup2 = (0, 1, 2, 3, 4, 5, 6, 7, 8)
new_tup2 = tup1[::-2]
print(new_tup2)
print(type(new_tup2))

