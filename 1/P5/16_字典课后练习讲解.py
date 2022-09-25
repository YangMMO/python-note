info_dict = {
    "mmo": {
        "department": "design",
        "salary": 3000,
        "level": 1
    },
    "tom": {
        "department": "pm",
        "salary": 1000,
        "level": 2
    },
    "jack": {
        "department": "design",
        "salary": 10000,
        "level": 3
    },
    "mike": {
        "department": "code",
        "salary": 100,
        "level": 1
    }
}

for item in info_dict:
    if info_dict[item]['level'] == 1:
        person = info_dict[item]
        person['level'] = 2
        person['salary'] += 1000

        info_dict[item] = person

# {
# 'mmo': {'department': 'design', 'salary': 4000, 'level': 2},
# 'tom': {'department': 'pm', 'salary': 1000, 'level': 2},
# 'jack': {'department': 'design', 'salary': 10000, 'level': 3},
# 'mike': {'department': 'code', 'salary': 1100, 'level': 2}
# }
print(info_dict)