from pyecharts.charts import Bar, Timeline
from pyecharts.options import LabelOpts
from pyecharts.globals import ThemeType

bar1 = Bar()
bar1.add_xaxis(["北京", "上海", "广东", "福建"])
bar1.add_yaxis('GDP', [80, 10, 60, 10], label_opts=LabelOpts(position="right"))
bar1.reversal_axis()

bar2 = Bar()
bar2.add_xaxis(["北京", "上海", "广东", "福建"])
bar2.add_yaxis('GDP', [120, 40, 50, 28], label_opts=LabelOpts(position="right"))
bar2.reversal_axis()

bar3 = Bar()
bar3.add_xaxis(["北京", "上海", "广东", "福建"])
bar3.add_yaxis('GDP', [130, 20, 12, 19], label_opts=LabelOpts(position="right"))
bar3.reversal_axis()

# 时间轴对象, 并选择主题
t = Timeline(
    {"theme": ThemeType.LIGHT}
)

t.add(bar1, 2011)
t.add(bar2, 2012)
t.add(bar3, 2013)

t.render("02.html")

# 设置播放
t.add_schema(
    # 时间间隔
    play_interval=1000,
    # 显示时间轴
    is_timeline_show=True,
    # 自动播放
    is_auto_play=True,
    # 循环
    is_loop_play=True
)


# 设置主题