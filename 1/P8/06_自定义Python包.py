# 文件夹右键 -》 python package（python软件包）
# 自动创建 __init__.py (包必须带有此文件)

# 引入
import my_package.module1
import my_package.module2

# 注意，包需要放在根目录才有智能提示
my_package.module1.info_print1()
my_package.module2.info_print2()


# 第二种引入
from my_package import module1
module1.info_print1()


# 第三种引入
from my_package.module2 import info_print2 as m
m()


# __all__  * 的形式导入
from my_package import *
module1.info_print1()
module2.info_print2()
