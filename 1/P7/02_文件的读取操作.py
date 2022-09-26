# open("文件路径", "访问模式", encoding="编码格式UTF-8")
# 模式 r 读 / w 写 / a 有文件则追加，无则新建
import time

# <_io.TextIOWrapper name='E:/Code/python-note/1/P7/test.txt' mode='r' encoding='UTF-8'>
# <class '_io.TextIOWrapper'>
f = open("E:/Code/python-note/1/P7/test.txt", "r", encoding="UTF-8")
print(f)
print(type(f))


# read(字节数量)
# print 1 人有悲欢离合，
# print 2 月有阴晴圆缺，   注意：因为第一次读了8字节，第二次会在上一次的截止位置继续往下读取
# <class 'str'>
print(f.read(8))
print(f.read())
print(type(f.read()))


# readlines(行数) 读取全部行为列表
# <class 'list'>
# ['\ufeff人有悲欢离合，\n', '月有阴晴圆缺，\n', '此事古难全。\n', '但愿人长久，\n', '千里共婵娟。']
f.seek(0)   # 句柄放在首位
lines = f.readlines()
print(type(lines))
print(lines)


# readline() 读取一行
# <class 'str'>
# ﻿人有悲欢离合，  注意：﻿为空字符，Unicode相关，可通过其他方式去除
# 月有阴晴圆缺，
f.seek(0)
line1 = f.readline()
line2 = f.readline()
print(type(line1))
print(line1)
print(line2)


# for
# 打印所有
f.seek(0)
for line in f:
    print(line)


# 关闭文件  否则一直被python占用
time.sleep(5)   # 指休眠5秒，5秒内该文件一直被占用
f.close()


# with open() as f  可在语句内进行文件操作，操作完成后自动close()关闭
print("_________")
with open("E:/Code/python-note/1/P7/test.txt", "r", encoding="UTF-8") as f:
    for line in f:
        print(line, end="")

