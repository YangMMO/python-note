num1 = 11
num2 = 65.456

print("%1d" % num1)
print("%2d" % num1)
print("%4d" % num1) # 前面加2空格

# 浮点数使用%f，因为使用%.1d其实是没作用的
# 65.46
print("%2.2f" % num2)

# 65.5
print("%.1f" % num2)

# 64
print("%.0f" % 64.5)

# 64 改为d无效，不会有四舍五入
print("%.0d" % 64.6)

#  65.46 这是 5位，前面 + 2 空格
print("%7.2f" % num2)
