
class Phone:
    __is_5g_enable = True

    def __check_5G(self):
        if self.__is_5g_enable:
            print("开启")
        else:
            print("关闭")

    def call_by_5g(self):
        self.__check_5G()
        print("正在通话中")



phone = Phone()
phone.call_by_5g()
