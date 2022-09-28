# __两个下划线开头为私有
# 类对象外部无法使用，只可类对象内部使用
class Phone:
    # 电压
    __current_voltage = 0

    def __keep_single_core(self):
        print("单核运行")

    def call_5g(self):
        if self.__current_voltage >= 1:
            print("开启")
        else:
            self.__keep_single_core()
            print("电量不足，无法使用5g")


# error 不可访问私有
phone = Phone()
# phone.__current_voltage = 10
# phone.__keep_single_core()

# 单核运行
# 电量不足，无法使用5g
phone.call_5g()
