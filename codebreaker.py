import random
digits = list(range(10))
random.shuffle(digits)
digits_str = str(digits[:3])
print(digits_str)
print(digits[:3])

guess = []
tries = 0
while str(guess) != digits_str:
    number = input('What is your 3 digit guess?')
    
    tries +=1
    for elem in number:
        guess.append(int(elem))
        guess_str=str(guess)
        print(guess_str)

    if guess_str not in digits_str:
        print("wrong guess")
        guess.clear()
    #elif guess_str in digits_str:
      #  print('you win')
    else:
        print('you got it')
    
    print ('number of tries {val} '.format(val=tries))
