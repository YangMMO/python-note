from file_define import TextFileReader, JsonFileReader, SQLTupleReader
from data_define import Record

text_file_reader = TextFileReader("E:/Code/python/python-note/2/P1/14/2011年1月销售数据.txt")
json_file_reader = JsonFileReader("E:/Code/python/python-note/2/P1/14/2011年2月销售数据JSON.txt")

# 读取 一月 二月的数据 ，list
jan_data: list[Record] = text_file_reader.read_data()
feb_data: list[Record] = json_file_reader.read_data()

# 两个list合并
all_data: list[Record] = jan_data + feb_data

# ————————分割线，以下为pymysql代码————————
from pymysql import Connection

connect = Connection(
    host="localhost",
    port=3306,
    user='root',
    password='123456',
    autocommit=True
)
connect.select_db('py_sql')
cursor = connect.cursor()

# 写入数据
# for record in all_data:
#     sql = f"insert into orders values('{record.date}', '{record.order_id}', {record.money}, '{record.province}')"
#     cursor.execute(sql)

# 读取数据
cursor.execute('select * from orders')
results = cursor.fetchall()
sql_tuple = SQLTupleReader(results)
print(sql_tuple.read_data())

connect.close()


# ————————分割线，以下为echarts代码————————

# 开始计算数据
# {“date”: money, ...}
# data_dict = {}
# for record in all_data:
#     # 判断日期是否在字典内
#     if record.date in data_dict.keys():
#         # 有记录，和老记录做累加
#         data_dict[record.date] += record.money
#     else:
#         # 新纪录，初始新值
#         data_dict[record.date] = record.money
#

# print(data_dict)

# 可视化开发
# from pyecharts.charts import Bar
# from pyecharts.options import *
# from pyecharts.globals import ThemeType
#
# bar = Bar(init_opts=InitOpts(theme=ThemeType.LIGHT))
#
# bar.add_xaxis(list(data_dict.keys()))   # 因为需要传入list, 此处需要转换
# bar.add_yaxis("销售额", list(data_dict.values()), label_opts=LabelOpts(is_show=False))
#
# bar.set_global_opts(
#     title_opts=TitleOpts(title="每日销售额")
# )
#
# bar.render()