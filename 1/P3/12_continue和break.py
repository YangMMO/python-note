# continue
for i in range(1, 6):
    if i == 2:
        print(i, "continue")
        continue
    print(i, "pass")

print("------")

# break
for i in range(1, 6):
    if i == 2:
        print(i, "continue")
        break
    print(i, "pass")
