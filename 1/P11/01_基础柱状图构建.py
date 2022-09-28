from pyecharts.charts import Bar
from pyecharts.options import LabelOpts

bar = Bar()

# 数据名称、数据、地图
bar.add_xaxis(["北京", "上海", "广东", "福建"])

# 将数数据数值放置于柱状图右侧
bar.add_yaxis('GDP', [30, 20, 10, 1], label_opts=LabelOpts(
    position="right"
))

# 反转 xy 轴
bar.reversal_axis()

bar.render("01.html")
