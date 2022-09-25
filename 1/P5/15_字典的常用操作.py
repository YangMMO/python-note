dict1 = {
    "mmo": 17,
    "tom": 123,
    "jack": 666
}

# 新增
# {'mmo': 17, 'tom': 123, 'jack': 666, 'mike': 13}
dict1["mike"] = 13
print(dict1)


# 更新
# {'mmo': 17, 'tom': 123, 'jack': 666, 'mike': 999}
dict1["mike"] = 999
print(dict1)


# 删除
# {'mmo': 17, 'jack': 666, 'mike': 999}
dict1.pop("tom")
print(dict1)


# clear()
# {}
dict1.clear()
print(dict1)


# 获取全部的key
# dict_keys(['mmo', 'tom', 'jack'])
# <class 'dict_keys'>
dict1 = {
    "mmo": 17,
    "tom": 123,
    "jack": 666
}
keys = dict1.keys()
print(keys)
print(type(keys))


# 遍历字典
# 方式1 循环key
# mmo: 17	tom: 123	jack: 666
for item in keys:
    print(f"{item}: {dict1[item]}", end="\t")

print()

# 方式2
# 循环 dict1
# mmo: 17	tom: 123	jack: 666
for key in dict1:
    print(f"{key}: {dict1[key]}", end="\t")
print()


# len
# 3
print(len(dict1))

