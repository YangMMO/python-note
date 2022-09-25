str1 = "WWW MMOO FUN"
num = str1.count("M")
# 2
print(num)

# WWW.MMOO.FUN
newStr = str1.replace(" ", ".")
print(newStr)

# ['WWW', 'MMOO', 'FUN']
list = newStr.split(".")
print(list)
