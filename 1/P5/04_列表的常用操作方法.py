arr1 = [1, 2, 3, 4]

# index
# 1
print(arr1.index(2))
# error 超出最大值
# print(arr1.index(5))


# =
# 1 6 3 4
arr1[1] = 6
print(arr1)


# insert (index, element)
# 99 1 6 3 4
arr1.insert(0, 99)
print(arr1)
# [99, 1, 6, 3, 4, 99] 插入index如果超出列表大小，只会append追加，但不建议这么做
# arr1.insert(100, 99)
# print(arr1)


# append(element)
# [99, 1, 6, 3, 4, 100]
arr1.append(100)
print(arr1)


# extend(list()) 追究一批元素
# [99, 1, 6, 3, 4, 100, 200, 300]
arr1.extend([200, 300])
print(arr1)


# del 删除元素
# [1, 6, 3, 4, 100, 200, 300]
del arr1[0]
print(arr1)


# pop(index)
# [1, 6, 3, 4, 200, 300]
# 可接收pop元素
num = arr1.pop(4)
print(arr1, num)


# remove(element) 从前到后，删除找到的第一个元素
# [1, 6, 3, 4, 300, 200]
arr1.append(200)
arr1.remove(200)
print(arr1)


# remove() 清空
# []
arr1.clear()
print(arr1)


# count(element) 统计元素的个数
# 2
arr1 = [1, 2, 3, 4, 2]
result = arr1.count(2)
print(result)

# len() 长度
# 5
print(len(arr1))
