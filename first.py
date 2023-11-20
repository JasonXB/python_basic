import random
p1 = input("Enter player 1's name: ")
p2 = input("Enter player 2's name: ")

toothpicks = 13
art = "| "
print("We start with 13 toothpicks: ", art * 13)
while True:
    m1 = input(f"{p1}, how many will you take? ")

    toothpicks -= int(m1)
    if (toothpicks < 1):
        print(p1, " wins!")
        break
    else:
        print(art * toothpicks)
    m2 = input(f"{p2}, how many will you take? ")
    toothpicks -= int(m2)
    if (toothpicks < 1):
        print(p2, " wins!")
        break
    else:
        print(art * toothpicks)
