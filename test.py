import random
digits = list(range(10))
random.shuffle(digits)
print(digits[:3])

guess = []
tries = 0
while guess != digits[:3]:
    number = input('What is your 3 digit guess?')

    tries += 1
    for elem in number:
        guess.append(int(elem))
        print(guess)

    if guess == digits[:3]:
        print('you win')
    elif guess[0] == digits[:3][0] \
            or guess[1] == digits[:3][1]\
            or guess[2] == digits[:3][2]:
        print('you guessed a correct number in the right position')
        guess.clear()
    elif guess[0] in digits[:3] and guess[0] != digits[:3][0] \
            or guess[1] in digits[:3] and guess[1] != digits[:3][1]\
            or guess[2] in digits[:3] and guess[2] != digits[:3][2]:
        print('you guessed a correct number in the wrong position')
        guess.clear()
    else:
        print("you haven't guessed any of the numbers correctly")
        guess.clear()
    print('number of tries {val} '.format(val=tries))
