import json
from pyecharts.charts import Map
from pyecharts.options import TitleOpts, VisualMapOpts

f = open("E:/Code/python-note/1/可视化数据/地图数据/疫情.txt", "r", encoding="UTF-8")
data = f.read()
f.close()

data_dict = json.loads(data)

# 取城市数据 列表
cities_data = data_dict["areaTree"][0]["children"][3]["children"]

# 绘图需要用的列表
data_list = []
for city_data in cities_data:
    city_name = city_data["name"] + "市"
    city_total = city_data["total"]["confirm"]
    # 组成元组
    data_list.append((city_name, city_total))

# print(data_list)

# 手动添加 济源市 数据
data_list.append(("济源市", 5))

# 绘图
map = Map()
map.add("河南省疫情分布", data_list, "河南")

map.set_global_opts(
    title_opts=TitleOpts(title="河南省各城市疫情分布"),
    visualmap_opts=VisualMapOpts(
        is_show=True,
        is_piecewise=True,
        pieces=[
            {"min": 1, "max": 99, "label": "1-99", "color": "#ffffff"},
            {"min": 100, "max": 999, "label": "100-999", "color": "#e0e0e0"},
            {"min": 1000, "max": 4999, "label": "1000-4999", "color": "#999999"},
            {"min": 5000, "max": 9999, "label": "5000-9999", "color": "#555555"},
            {"min": 10000, "max": 99999, "label": "10000-99999", "color": "#333333"},
            {"min": 100000, "label": "100000+", "color": "#111111"},
        ]
    )
)

map.render("03.html")
