money = 10000

for i in range(1, 21):
    import random
    score = random.randint(1, 10)

    if score < 5:
        print(f"Person {i}\tscore: {score}\tnext")
        continue

    if money >= 1000:
        money -= 1000
        print(f"Person {i}\tmoney +1000\tmoney: {money}")
    else:
        print(f"no money: {money}")