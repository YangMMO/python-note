height = int(input("输入身高："))
level = int(input("输入VIP等级："))
day = int(input("今日几号："))

# if height < 120:
#     print("free")
# elif level > 1:
#     print("free")
# elif day == 1:
#     print("free")
# else:
#     print("price $30")


if height < 120 or level > 1 or day == 1:
    print("free")
else:
    print("price $30")