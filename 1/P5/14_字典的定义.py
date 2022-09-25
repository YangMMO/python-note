dict1 = {"p1": 16, "p2": 19, "p3": 22}
dict2 = {}
dict3 = dict()
print(dict1)
print(type(dict1))
print(dict2)
print(type(dict2))
print(dict3)
print(type(dict3))

# 不允许key重复，键值对
# dict4 = {"p1": 16, "p1": 19}

# 不可以使用下标访问
# 只能通过键查找
# 16
dict1 = {"p1": 16, "p2": 19, "p3": 22}
print(dict1["p1"])

# 嵌套
# 1002
arr = {
    "P1": {
        "a": 12,
        "b": 17,
        "c": 32
    },
    "P2": {
        "a": 102,
        "b": 107,
        "c": 302
    },
    "P3": {
        "a": 1002,
        "b": 1007,
        "c": 3002
    },
}

print(arr["P3"]["a"])
