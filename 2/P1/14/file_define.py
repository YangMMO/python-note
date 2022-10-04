"""
文件操作的类
"""
from data_define import Record
import json


# 抽象类，顶层设计
class FileReader:
    def read_data(self) -> list[Record]:
        """读取文件的数据，读取的每一条都转为Record对象。将他们封装到list并返回"""
        pass


class TextFileReader(FileReader):

    def __init__(self, path):
        self.path = path        # 定义成员变量记录文件的路径

    # 复写 实现抽象方法
    def read_data(self) -> list[Record]:
        f = open(self.path, "r", encoding="UTF-8")

        record_list: list[Record] = []
        for line in f.readlines():
            line = line.strip()             # 处理换行空格
            data_list = line.split(',')
            record = Record(data_list[0], data_list[1], int(data_list[2]), data_list[3])
            record_list.append(record)

        f.close()

        return record_list


class JsonFileReader(FileReader):
    def __init__(self, path):
        self.path = path

    def read_data(self) -> list[Record]:
        f = open(self.path, "r", encoding="UTF-8")

        record_list: list[Record] = []
        for line in f.readlines():
            data_dict = json.loads(line)
            record = Record(data_dict["date"], data_dict["order_id"], int(data_dict["money"]), data_dict["province"])
            record_list.append(record)

        f.close()

        return record_list


class SQLTupleReader(FileReader):
    def __init__(self, tup):
        self.tuple = tup        # 定义成员变量记录文件的路径

    def read_data(self) -> list[Record]:
        record_list: list[Record] = []
        for line in self.tuple:
            data_dist = dict()

            data_dist['date'] = str(line[0])
            data_dist['order_id'] = str(line[1])
            data_dist['money'] = int(line[2])
            data_dist['province'] = str(line[3])

            json_data = json.dumps(data_dist)
            print(json_data)

            record_list.append(json_data)

        return record_list


if __name__ == '__main__':
    text_file_reader = TextFileReader("E:/Code/python-note/2/P1/14/2011年1月销售数据.txt")
    json_file_reader = JsonFileReader("E:/Code/python-note/2/P1/14/2011年2月销售数据JSON.txt")

    list1 = text_file_reader.read_data()
    list2 = json_file_reader.read_data()

    for l in list1:
        print(l)

    for l in list2:
        print(l)