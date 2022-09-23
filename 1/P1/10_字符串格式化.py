msg = "mmo"
num1 = 9999
num2 = 111

# msg: mmo
str1 = "msg: %s" % msg
print(str1)

str2 = "msg: %s, num 1: %s, num 2 : %s" % (msg, num1, num2)
print(str2)

num3 = 6
num4 = 1.23

# num 3: 6, num 4: 1.230000
print("num 3: %d, num 4: %f" % (num3, num4))

# num 3: 6.000000, num 4: 1
print("num 3: %f, num 4: %d" % (num3, num4))
