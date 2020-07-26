import random as r

r = r.randint(0,21)

guess_num = int(input("guess the number between 1 to 20 : "))

if r <= 20:
    print("ok")
else:
    print("game over")
