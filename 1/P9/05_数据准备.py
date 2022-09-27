import json

# 处理数据
# 并处理头尾问题
f_us = open("E:/Code/python-note/1/可视化数据/折线图数据/美国.txt", "r", encoding="UTF-8")
us_data = f_us.read()
us_data = us_data.replace("jsonp_1629344292311_69436(", "")
us_data = us_data[:-2]
us_dict = json.loads(us_data)

# <class 'dict'>
print(type(us_dict))
print(us_dict)
