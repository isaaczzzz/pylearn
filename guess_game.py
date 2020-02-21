import random
num = random.randint(1, 10000)
print("Guess What think.(From 1 to 10000)")
while True:
    print("Input your answer:")
    answer = int(input())
    if answer < num:
        print("Too small")
    if answer > num:
        print("Too big")
    if answer == num:
        print("BINGO!")
        break

