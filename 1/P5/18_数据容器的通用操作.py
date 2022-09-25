"""
演示数据容器的通用功能
"""
my_list = [1, 2, 3, 4, 5]
my_tuple = (1, 2, 3, 4, 5)
my_str = "abcdefg"
my_set = {1, 2, 3, 4, 5}
my_dict = {"key1": 1, "key2": 2, "key3": 3, "key4": 4, "key5": 5}


# len元素个数
# 列表元素个数有: 5
# 元组元素个数有: 5
# 字符串元素个数有: 7
# 集合元素个数有: 5
# 字典元素个数有: 5
print(f"列表元素个数有: {len(my_list)}")
print(f"元组元素个数有: {len(my_tuple)}")
print(f"字符串元素个数有: {len(my_str)}")
print(f"集合元素个数有: {len(my_set)}")
print(f"字典元素个数有: {len(my_dict)}")
print("________")

# max最大元素
# 列表 最大元素是: 5
# 元组 最大元素是: 5
# 字符串 最大元素是: g
# 集合 最大元素是: 5
# 字典 最大元素是: key5
print(f"列表 最大元素是: {max(my_list)}")
print(f"元组 最大元素是: {max(my_tuple)}")
print(f"字符串 最大元素是: {max(my_str)}")
print(f"集合 最大元素是: {max(my_set)}")
print(f"字典 最大元素是: {max(my_dict)}")
print("________")

# min最小元素
# 列表 最小元素是: 1
# 元组 最小元素是: 1
# 字符串 最小元素是: a
# 集合 最小元素是: 1
# 字典 最小元素是: key1
print(f"列表 最小元素是: {min(my_list)}")
print(f"元组 最小元素是: {min(my_tuple)}")
print(f"字符串 最小元素是: {min(my_str)}")
print(f"集合 最小元素是: {min(my_set)}")
print(f"字典 最小元素是: {min(my_dict)}")
print("________")

# 类型转换:容器转列表
# 列表转列表的结果是: [1, 2, 3, 4, 5]
# 元组转列表的结果是: [1, 2, 3, 4, 5]
# 字符串转列表结果是: ['a', 'b', 'c', 'd', 'e', 'f', 'g']
# 集合转列表的结果是: [1, 2, 3, 4, 5]
# 字典转列表的结果是: ['key1', 'key2', 'key3', 'key4', 'key5']
print(f"列表转列表的结果是: {list(my_list)}")
print(f"元组转列表的结果是: {list(my_tuple)}")
print(f"字符串转列表结果是: {list(my_str)}")
print(f"集合转列表的结果是: {list(my_set)}")
print(f"字典转列表的结果是: {list(my_dict)}")
print("________")

# 类型转换:容器转元组
# 列表转元组的结果是: (1, 2, 3, 4, 5)
# 元组转元组的结果是: (1, 2, 3, 4, 5)
# 字符串转元组结果是: ('a', 'b', 'c', 'd', 'e', 'f', 'g')
# 集合转元组的结果是: (1, 2, 3, 4, 5)
# 字典转元组的结果是: ('key1', 'key2', 'key3', 'key4', 'key5')
print(f"列表转元组的结果是: {tuple(my_list)}")
print(f"元组转元组的结果是: {tuple(my_tuple)}")
print(f"字符串转元组结果是: {tuple(my_str)}")
print(f"集合转元组的结果是: {tuple(my_set)}")
print(f"字典转元组的结果是: {tuple(my_dict)}")
print("________")

# 类型转换:容器转字符串
# 列表转字符串的结果是: "[1, 2, 3, 4, 5]"
# 元组转字符串的结果是: "(1, 2, 3, 4, 5)"
# 字符串转字符串结果是: "abcdefg"
# 集合转字符串的结果是: "{1, 2, 3, 4, 5}"
# 字典转字符串的结果是: "{'key1': 1, 'key2': 2, 'key3': 3, 'key4': 4, 'key5': 5}"
print(f"列表转字符串的结果是: {str(my_list)}")
print(f"元组转字符串的结果是: {str(my_tuple)}")
print(f"字符串转字符串结果是: {str(my_str)}")
print(f"集合转字符串的结果是: {str(my_set)}")
print(f"字典转字符串的结果是: {str(my_dict)}")
print("________")

# 类型转换:容器转集合
# 列表转集合的结果是: {1, 2, 3, 4, 5}
# 元组转集合的结果是: {1, 2, 3, 4, 5}
# 字符串转集合结果是: {'a', 'c', 'b', 'g', 'd', 'e', 'f'}
# 集合转集合的结果是: {1, 2, 3, 4, 5}
# 字典转集合的结果是: {'key1', 'key2', 'key5', 'key3', 'key4'}
print(f"列表转集合的结果是: {set(my_list)}")
print(f"元组转集合的结果是: {set(my_tuple)}")
print(f"字符串转集合结果是: {set(my_str)}")
print(f"集合转集合的结果是: {set(my_set)}")
print(f"字典转集合的结果是: {set(my_dict)}")
print("________")

# 进行容器排序
# sorted() 会返回 列表
my_list = [3, 1, 2, 5, 4]
my_tuple = (3, 1, 2, 5, 4)
my_str = "gscsdavdb"
my_set = {3, 1, 2, 5, 4}
my_dict = {"key3": 3, "key1": 1, "key2": 2, "key5": 5, "key4": 4}
# 列表对象的排序结果: [1, 2, 3, 4, 5]
# 元组对象的排序结果: [1, 2, 3, 4, 5]
# 字符串对象的排序结果: ['a', 'b', 'c', 'd', 'd', 'g', 's', 's', 'v']
# 集合对象的排序结果: [1, 2, 3, 4, 5]
# 字典对象的排序结果: ['key1', 'key2', 'key3', 'key4', 'key5']
print(f"列表对象的排序结果: {sorted(my_list)}")
print(f"元组对象的排序结果: {sorted(my_tuple)}")
print(f"字符串对象的排序结果: {sorted(my_str)}")
print(f"集合对象的排序结果: {sorted(my_set)}")
print(f"字典对象的排序结果: {sorted(my_dict)}")
print("________")

# 反向排序，加 reverse=True
# 列表对象的排序结果: [5, 4, 3, 2, 1]
# 元组对象的排序结果: [5, 4, 3, 2, 1]
# 字符串对象的排序结果: ['v', 's', 's', 'g', 'd', 'd', 'c', 'b', 'a']
# 集合对象的排序结果: [5, 4, 3, 2, 1]
# 字典对象的排序结果: ['key5', 'key4', 'key3', 'key2', 'key1']
print(f"列表对象的排序结果: {sorted(my_list, reverse=True)}")
print(f"元组对象的排序结果: {sorted(my_tuple, reverse=True)}")
print(f"字符串对象的排序结果: {sorted(my_str, reverse=True)}")
print(f"集合对象的排序结果: {sorted(my_set, reverse=True)}")
print(f"字典对象的排序结果: {sorted(my_dict, reverse=True)}")
print("________")
