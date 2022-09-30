"""
订单数据的类
"""


class Record:
    def __init__(self, date, order_id, money, province):
        self.date = date                # 日期
        self.order_id = order_id        # id
        self.money = money              # 金额
        self.province = province        # 地区


    def __str__(self):
        """魔术方法，打印record对象"""
        return f"{self.date}, {self.order_id}, {self.money}, {self.province}"