import random

print ("hello, what is your name?")
name = input ()


print ('hiii! ' + name + ',Lets play a game of guess the number. I am thinking of a number between 1 and 20.')
secretNumber = random.randint(1, 20)

for guessesTaken in range(1, 7):
    print ("take a guess")
    guess = int(input())

    if guess > secretNumber:
        print ('your guesss is too high')
    elif guess < secretNumber:
        print ('Your guess is too low')
    else:
        break

if guess == secretNumber:
    print ('Good job you guessed my number in ' + str(guessesTaken) + ' guesses!')
else:
    print ('Nope, The number I was thinking of was' + str(secretNumber))
    
