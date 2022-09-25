tup1 = (1, 2, 3, 4, 5)

tup2 = ()

tup3 = (1, 2, 3, 4, 5)

print(tup1)
print(type(tup1))
print(tup2)
print(type(tup2))
print(tup3)
print(type(tup3))

# int error
# tup4 = (1)
# print(tup4)
# print(type(tup4))

# tuple yes
tup4 = (1,)
print(tup4)
print(type(tup4))

# 嵌套
tup5 = ((1, 2), (3, 4))
print(tup5)


# _______________________________


# []
# 3
num = tup5[1][0]
print(num)


# index
# 1
tup6 = (1, 2, 3, 4, 5, 2)
index = tup6.index(2)
print(index)


# count(element)
# 2
tup7 = (1, 2, 3, 4, 5, 2)
num = tup7.count(2)
print(num)


# len(tuple)
# 6
tup7 = (1, 2, 3, 4, 5, 2)
num = len(tup7)
print(num)


# while
print("while")
tup8 = (1, 2, 3, 4, 5, 2)
index = 0
while index < len(tup8):
    print(tup8[index])
    index += 1


# for
print("for")
for e in tup8:
    print(e)


# error
# TypeError：“元组”对象不支持项目分配
# tup8[0] = 99
# print(tup8)


# tuple 嵌套 list ,list 可修改
# (1, 2, [3, 4, 5, 2])
tup9 = (1, 2, [3, 4, 5, 2])
print(tup9)

# (1, 2, [99, 4, 5, 2])
tup9[2][0] = 99
print(tup9)
