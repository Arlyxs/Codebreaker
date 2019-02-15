import random
digits = list(range(10))
random.shuffle(digits)
digits_str = str(digits[:3])
print(digits_str)
print(digits[:3])

guess = []
tries = 0
number = input('What is your 3 digit guess? ')
150
tries = tries + 1
for elem in number:
    guess.append(int(elem))
print(guess)

if guess > digits[:3]:
        print("too high")
elif guess < digits[:3]:
        print('too low')
else:
        print('you got it')

print ('number of tries ' + str(tries))