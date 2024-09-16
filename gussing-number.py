import random 

low = 1
high = 100
number = random.randint(low,high)
guesses = 0
max_guesses = 5
while guesses < max_guesses:# print(help(random ))
    guess = input(f"enter a number")
    guess = int(guess)
    guesses += 1
    if number > guess:
        print(f"{guess} is low guess higher")
    elif number < guess:
        print(f"{guess} is high guess lower")
    # elif max_guesses >= guesses:
    #     print("your gussing chance is insuficinet")
    else:
        print(f"{guess} is correct")
        break
print(f"this round it took you {guesses} guesses")