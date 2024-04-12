import random
n = random.randrange(10)
guess = int(input('number guess enter:'))
while guess != n:
    if guess > n:
        print("Too High")
    elif guess < n:
        print("Too low")
    else:
        break
    guess = int(input('number guess enter:'))
print("you guessed it right!!!")