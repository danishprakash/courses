import random
print('Guess a number from 1-20, youll get 7 chances')
secretNum = random.randint(1,20)

for i in range(1,7):
    print('Take a guess')
    guess = int(input())

    if guess < secretNum:
        print('You are a little low')
    elif guess > secretNum:
        print('You are a little high')
    else:
        break

if guess == secretNum:
    if i == 1:
        print('Hey you guessed it right in',i,'guess')
    else:
        print('Hey you guessed it right in',i,'guesses')
else:
    print('Aw, you might wanna try again, i was thinking about', secretNum) 
