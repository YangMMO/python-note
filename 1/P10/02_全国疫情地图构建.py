import json
from pyecharts.charts import Map
from pyecharts.options import TitleOpts, VisualMapOpts

f = open("E:/Code/python-note/1/可视化数据/地图数据/疫情.txt", "r", encoding="UTF-8")
data = f.read()
f.close()

data_dict = json.loads(data)

# 取省份数据 列表
province_data_list =  data_dict["areaTree"][0]["children"]

# 绘图需要用的列表
data_list = []
for province_data in province_data_list:
    province_name = province_data["name"]
    province_total = province_data["total"]["confirm"]
    # 组成元组
    data_list.append((province_name, province_total))

print(data_list)

# 绘图
map = Map()
map.add("各省份确诊人数", data_list, "china")

map.set_global_opts(
    title_opts=TitleOpts(title="全国疫情地图"),
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

map.render("02.html")
