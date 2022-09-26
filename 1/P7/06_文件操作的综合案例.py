fr = open("E:/Code/python-note/1/P7/bill.txt", "r", encoding="UTF-8")
fw = open("E:/Code/python-note/1/P7/bill.txt.bak", "w", encoding="UTF-8")

for line in fr:
    # 格式化 \n
    line = line.strip()

    # 跳过测试的数据
    if line.split(",")[4] == "测试":
        continue

    fw.write(line)
    fw.write("\n")  # 补回换行

fr.close()
fw.close()
