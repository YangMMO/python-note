# 注意： open如果过是w模式，则会判断文件是否存在，不存在自动则创建
f = open("E:/Code/python-note/1/P7/write.txt", "w", encoding="UTF-8")

# write 写入只缓冲区
f.write("hello world")

# flush 刷新缓冲区，将缓冲区的内容写入至文件
# f.flush()

# close 内置 flush 功能
f.close()

# 注意：如果重新打开文件，再次write写入，会覆盖原本的文件内容
