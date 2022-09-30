from file_define import TextFileReader, JsonFileReader
from data_define import Record

text_file_reader = TextFileReader("E:/Code/python-note/2/P1/14/2011年1月销售数据.txt")
json_file_reader = JsonFileReader("E:/Code/python-note/2/P1/14/2011年2月销售数据JSON.txt")

# 读取 一月 二月的数据 ，list
jan_data: list[Record] = text_file_reader.read_data()
feb_data: list[Record] = json_file_reader.read_data()

# 两个list合并
all_data: list[Record] = jan_data + feb_data

# 开始计算数据
# {“date”: money, ...}
data_dict = {}
for record in all_data:
    # 判断日期是否在字典内
    if record.date in data_dict.keys():
        # 有记录，和老记录做累加
        data_dict[record.date] += record.money
    else:
        # 新纪录，初始新值
        data_dict[record.date] = record.money


print(data_dict)


# 可视化开发
from pyecharts.charts import Bar
from pyecharts.options import *
from pyecharts.globals import ThemeType

bar = Bar(init_opts=InitOpts(theme=ThemeType.LIGHT))

bar.add_xaxis(list(data_dict.keys()))   # 因为需要传入list, 此处需要转换
bar.add_yaxis("销售额", list(data_dict.values()), label_opts=LabelOpts(is_show=False))

bar.set_global_opts(
    title_opts=TitleOpts(title="每日销售额")
)

bar.render()