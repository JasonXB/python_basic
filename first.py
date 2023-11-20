import random


while True:
    roll1 = random.randint(1, 6)
    roll2 = random.randint(1, 6)
    if roll1 == 1 and roll2 == 1:
        print("Snake eyes!", roll1, roll2)
        break
    else:
        print("Try again!", roll1, roll2)

print("Experiment over")
