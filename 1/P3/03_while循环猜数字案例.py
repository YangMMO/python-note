import random
num = random.randint(1, 100)

flag = True
count = 0;

while flag:
    guess = int(input("num: "))
    count += 1
    if guess == num:
        print("good")
        flag = False
    elif guess > num:
        print("guess > num")
    else:
        print("guess < num")

print(f"guess: {count}")
