money = 5000000
name = None

name = input("input name: ")


def query(bool):
    if bool:
        print(f"____query____")
    print(f"{name}\tmoney: {money}")


def saving(num):
    global money
    money += num
    print(f"____saving____")
    print(f"save money: {money}")
    query(False)


def get(num):
    global money
    money -= num
    print(f"____get____")
    query(False)


def main():
    print("____Menu____")
    print(f"{name}, hello")
    print("query\t[1]")
    print("saving\t[2]")
    print("get\t\t[3]")
    print("quit\t[4]")

    return int(input("number: "))


while True:
    keyboard_input = main()

    if keyboard_input == 1:
        query(True)
        continue
    elif keyboard_input == 2:
        num = int(input("saving money: "))
        saving(num)
        continue
    elif keyboard_input == 3:
        num = int(input("get money: "))
        get(num)
        continue
    else:
        print("quit")
        break
