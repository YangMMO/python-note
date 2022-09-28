from pyecharts.charts import Bar, Timeline
from pyecharts.options import LabelOpts, TitleOpts
from pyecharts.globals import ThemeType

# 注意 文件编码为 ANSI 即为跟随系统版本
# 中文编码为 GB2312
f = open("E:/Code/python-note/1/可视化数据/动态柱状图数据/1960-2019全球GDP数据.csv", "r", encoding="GB2312")
data_lines = f.readlines()
f.close()

# 处理数据，删除首行
data_lines.pop(0)

# 封装为字典数据
data_dict = {}
for line in data_lines:
    year = int(line.split(",")[0])      # 年份
    country = line.split(",")[1]   # 国家
    gdp = float(line.split(",")[2])     # gdp ，数值大转为浮点

    # 判断字典有没有指定的key
    # 年份是否在字典中，有则append，无则构建一个新的list
    try:
        data_dict[year].append([country, gdp])
    except KeyError:
        data_dict[year] = []
        data_dict[year].append([country, gdp])


# 构建每年柱状图
# 先排序年份, 因为字段排序可能有误
timeline = Timeline({
    "theme": ThemeType.LIGHT
})
sorted_year_list = sorted(data_dict.keys())
for year in sorted_year_list:
    # 排序下gdp值
    data_dict[year].sort(key=lambda element: element[1], reverse=True)

    # 取前八
    year_data = data_dict[year][0:8]

    # X 国家， Y gdp（亿）
    x_data = []
    y_data = []
    for country_gdp in year_data:
        x_data.append(country_gdp[0])
        y_data.append(country_gdp[1] / 100000000)

    # reverse 数据，否则是反的
    x_data.reverse()
    y_data.reverse()

    # 构建柱状图
    bar = Bar()
    bar.add_xaxis(x_data)
    bar.add_yaxis("GDP(亿)", y_data, label_opts=LabelOpts(position="right"))

    # 反转轴
    bar.reversal_axis()

    # 设置标题
    bar.set_global_opts(
        title_opts=TitleOpts(title=f"{year}年前8GDP数据")
    )

    # 插入时间轴
    timeline.add(bar, str(year))


# 时间轴的设置
timeline.add_schema(
    play_interval=1000,
    is_timeline_show=True,
    is_auto_play=True,
    is_loop_play=True,
)

# 绘图
timeline.render("03.html")
