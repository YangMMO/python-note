set1 = {1, 2, 3, 4, 5, 6}
# set2 = {} # error 这不是创建空集合，这是字典dict{}
set3 = set()
print(set1)
print(type(set1))
# print(set2)
# print(type(set2))
print(set3)
print(type(set3))

# set 是无须的。所以不支持下标访问

# add(element) 添加新元素
# {1, 2, 3, 4, 5, 6, 666, 123}
set1.add(123)
set1.add(666)
# set1.add(1)   # 因为已经有了1 所以无法添加，但不报错
print(set1)


# remove(element)
# {1, 2, 3, 4, 5, 6, 666}
set1.remove(123)
print(set1)


# pop() 随机取，不是取最后
# 1
# {2, 3, 4, 5, 6, 666}
result = set1.pop()
print(result)
print(set1)


# clear()
# print -> set()
set1.clear()
print(set1)


# 取第两集合的差集
# 取集合1有，集合2没有
# {2, 3}
set1 = {1, 2, 3}
set2 = {1, 4, 6}
result = set1.difference(set2)
print(result)


# 消除差集 与上方区别，上方返回结果，这个直接修改
# 集合1 内部 消除与 集合2相同的元素
# {2, 3}
set1.difference_update(set2)
print(set1)


# 两集合 合并 并返回新集合
# {1, 2, 3, 4, 6}
set1 = {1, 2, 3}
set2 = {1, 4, 6}
newSet = set1.union(set2)
print(newSet)


# len()
# 3
print(len(set1))


# 遍历
# 因为不支持下标方式访问，所以无法用while，但可以用for
for e in set1:
    print(e)
