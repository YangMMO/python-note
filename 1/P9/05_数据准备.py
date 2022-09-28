import json
from pyecharts.charts import Line
from pyecharts.options import TitleOpts, LabelOpts
# 处理数据
# 并处理头尾问题
f_us = open("E:/Code/python-note/1/可视化数据/折线图数据/美国.txt", "r", encoding="UTF-8")
f_jp = open("E:/Code/python-note/1/可视化数据/折线图数据/日本.txt", "r", encoding="UTF-8")
f_in = open("E:/Code/python-note/1/可视化数据/折线图数据/印度.txt", "r", encoding="UTF-8")

us_data = f_us.read()
jp_data = f_jp.read()
in_data = f_in.read()

us_data = us_data.replace("jsonp_1629344292311_69436(", "")
jp_data = jp_data.replace("jsonp_1629350871167_29498(", "")
in_data = in_data.replace("jsonp_1629350745930_63180(", "")

us_data = us_data[:-2]
jp_data = jp_data[:-2]
in_data = in_data[:-2]

us_dict = json.loads(us_data)
jp_dict = json.loads(jp_data)
in_dict = json.loads(in_data)

# 测试
# <class 'dict'>
# print(type(us_dict))
# print(us_dict)

us_trend_data = us_dict["data"][0]["trend"]
jp_trend_data = jp_dict["data"][0]["trend"]
in_trend_data = in_dict["data"][0]["trend"]
# print(type(trend_data))
# print(trend_data)

# 取到2020年 下标 314
us_x_data = us_trend_data["updateDate"][:314]
jp_x_data = jp_trend_data["updateDate"][:314]
in_x_data = in_trend_data["updateDate"][:314]
# print(x_data)
us_y_data = us_trend_data["list"][0]["data"][:314]
jp_y_data = jp_trend_data["list"][0]["data"][:314]
in_y_data = in_trend_data["list"][0]["data"][:314]
# print(y_data)

# 使用 pyecharts
line = Line()
# X 共用 日期 数据
line.add_xaxis(us_x_data)

line.add_yaxis("美国确诊人数", us_y_data, label_opts=LabelOpts(is_show=False))
line.add_yaxis("日本确诊人数", jp_y_data, label_opts=LabelOpts(is_show=False))
line.add_yaxis("印度确诊人数", in_y_data, label_opts=LabelOpts(is_show=False))

line.set_global_opts(
    title_opts=TitleOpts(title="2020确诊人数对比折线图", pos_left="center", pos_bottom="1%")
)

line.render()


f_us.close()
f_jp.close()
f_in.close()