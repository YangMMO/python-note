import test_module as tm

print(tm.add(1, 5))


# import test_module1 as tm
# import test_module2 as tm
# tm.add(1, 5)      # 使用的tm是第二个，因为覆盖了


# __main__
# 在 __main__ 内都不会被执行
# 因为在 test_module 内部 name 会判断 是否 == main
from test_module import add


# __all__
# 只会引入 __all__内的, 内部并未包含 add2
# 只会作用于 * 上，如果直接 import add()还是能引入的
from test_module import *
add()
# add2()    error