# end=“” 空字符串 不换行
print("hello", end="")
print("world", end="\n")

# \t 制表符
print("hello", end="\t")
print("world", end="\n")

i = 1
while i <= 9:

    j = 1
    while j <= i:
        print(f"{j}*{i}={j * i}", end="\t")
        j += 1

    i += 1
    print("")

