# 如对父类成员不满意，则在子类进行定义相同的成员进行复写即可

class Phone:
    IMEI = None
    producer = "Apple"

    def call_by_2g(self):
        print("2g通话")


class MyPhone(Phone):
    producer = "HUAWEI"

    def call_by_2g(self):
        # 继续调用父类的旧成员
        # 方式一 父类名称
        print(Phone.producer)

        # 方式二 Super
        super().call_by_2g()

        print("2.5G")


# 使用复写的成员
# HUAWEI
# 2.5G
mp = MyPhone()
print(mp.producer)
mp.call_by_2g()
