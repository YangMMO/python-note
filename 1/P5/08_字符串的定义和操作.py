name = "mmoofun"

# 访问
val1 = name[2]
val2 = name[-2]
print(val1, val2)

# 不支持修改 TypeError：“str”对象不支持项目分配
# name[0] = "M"


# index
# 2
index = name.index("o")
print(index)


# replace(需要替换的值，替换的新值)
# 本质不是修改，是得到新的字符串
# MMoofun
newStr = name.replace("m", "M")
print(newStr)


# split(分隔的字符串)
# ['MM', 'OO', 'FUN']
# <class 'list'>
# "MM OO FUN"
str1 = "MM OO FUN"
newList = str1.split(" ")
print(newList)
print(type(newList))
print(str1)


# strip() 去除前后空格
# strip("字符串") 去除指定字符串
# "MM OO FUN"
str2 = " MM OO FUN "
new_str2 = str2.strip()
print(new_str2)
# 注意： 输入的是MM，但规则是划分为两个M，而不是MM一个整体
# OOFUN
str3 = "MMOOFUNM"
print(str3.strip("MM"))


# count(element)
# 2
str4 = "MMOOFUN"
result = str4.count("O")
print(result)


# len()
# 7
print(len(str4))
