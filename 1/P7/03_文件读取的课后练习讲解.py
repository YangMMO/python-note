f = open("E:/Code/python-note/1/P7/word.txt", "r", encoding="UTF-8")

# 方式一
content = f.read()
count = content.count("itheima")
print(count)

# 方式二
f.seek(0)
count = 0
for line in f:
    # 先剔除换行符
    # strip 可剔除 前后空格 换行符
    line = line.strip()
    words = line.split(" ")
    for word in words:
        if word == "itheima":
            count += 1

print(count)

f.close()