# 使用折线图
from pyecharts.charts import Line

# 获取 line 对象
line = Line()

# 添加 X 轴数据
line.add_xaxis(["中国", "美国", "英国"])
# 添加 Y 轴为 GDP 的数据
line.add_yaxis("GDP", [30, 20, 10])


# ————————————————————————————
# 设置全局配置
from pyecharts.options import TitleOpts, LegendOpts, ToolboxOpts, VisualMapOpts
line.set_global_opts(
    # 标题展示
    title_opts=TitleOpts("GDP展示", pos_left="center", pos_bottom="1%"),
    # 图例展示
    legend_opts=LegendOpts(is_show=True),
    # 工具箱
    toolbox_opts=ToolboxOpts(is_show=True),
    # 视觉映射
    visualmap_opts=VisualMapOpts(is_show=True)

)


# ————————————————————————————


# 渲染 生成一个 render.html 的文件
line.render()
