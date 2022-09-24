# 引入随机 1~10
import random
num = random.randint(1, 10)

guess_num = int(input("num: "))

if guess_num == num:
    print("good")
else:
    if guess_num > num:
        print("guess > num")
    else:
        print("guess < num")

    guess_num = int(input("again: "))

    if guess_num == num:
        print("good")
    else:
        if guess_num > num:
            print("guess > num")
        else:
            print("guess < num")

        guess_num = int(input("again: "))

        if guess_num == num:
            print("good")
        else:
            print("end")