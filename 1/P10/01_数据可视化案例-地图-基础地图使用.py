from pyecharts.charts import Map
from pyecharts.options import VisualMapOpts

map = Map()

data = [
    ("北京", 99),
    ("上海", 199),
    ("广东", 299),
    ("福建", 399)
]

# 数据名称、数据、地图
map.add("测试map", data, "china")

map.set_global_opts(
    visualmap_opts=VisualMapOpts(
        is_show=True,
        # 手动校准范围 分段
        is_piecewise=True,
        # 信息片段
        pieces=[
            {"min": 1, "max": 9, "label": "1-9", "color": "#CCFFFF"},
            {"min": 10, "max": 99, "label": "10-99", "color": "#FF6666"},
            {"min": 100, "max": 500, "label": "100-500", "color": "#990033"},
        ]
    )
)

map.render("01.html")
