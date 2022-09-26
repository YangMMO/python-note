# [] 代表可选
# [from 模块名] import [模块 | 变量 | 函数 | *] [as 别名]

# 基础使用
# ctrl + 左键 查看相关代码
import time
# 使用sleep函数
time.sleep(0)


# 导入模块内的某个函数
from time import sleep
sleep(5)


# * 所有
from time import *
sleep(10)


# as 给个别名
import time as t
t.sleep(15)
from time import sleep as s
s(20)
