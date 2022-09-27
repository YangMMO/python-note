# 导入 json 模块
import json

data = [
    {
        "name": '牛',
        "age": 20,
        "arr": [1, 2, 3]
    }, {
        "name": '猪',
        "age": 22,
        "arr": [4, 5, 6]
    }, {
        "name": '猫',
        "age": 24,
        "arr": [7, 8, 9]
    },
]

# dumps 转 json
# 为解决中文编码问题 ensure_ascii 确保ASCII=False
json_data = json.dumps(data, ensure_ascii=False)

# <class 'str'>
print(type(json_data))
print(json_data)



# loads 转 python
python_data = json.loads(json_data)

# <class 'list'>
print(type(python_data))
print(python_data)
