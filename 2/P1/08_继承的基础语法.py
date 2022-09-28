# ()写继承的类名称
class Phone:
    IMEI = None
    producer = "Apple"

    def __call_by_2g(self):
        print("2g通话")

    def call_by_4g(self):
        print("4g通话")


# 单继承 只继承一个
class Phone2022(Phone):
    face_id = "10001"

    def call_by_5g(self):
        print("5g通话")


p = Phone2022()
print(p.IMEI)
# p.call_by_2g()    # error 无法访问父类私有
p.call_by_4g()
p.call_by_5g()


# 多继承 继承多个
class NFCReader:
    nfc_type = "5.0.1"
    producer = "HUAWEI"

    def read_card(self):
        print("NFC读卡")


# pass 关键字补全语法，代表跳过
# 同名 producer 左边的类优先
class MyPhone(Phone, NFCReader):
    pass


mp = MyPhone()
print(mp.producer)
