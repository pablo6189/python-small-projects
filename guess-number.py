import random
ran = random.choice(range(1,50))
#print(ran)
attempt = 1
print('*****WELCOME*****')
print('You will have to guess a number between 1 and 50...')
guess = int(input('Please type your guess, You will have 3 attempts...  '))
while(guess < 1 or guess > 50):
    guess = int(input('Your input was incorrect, please type a number between 1 and 50...  '))

while(ran != guess and attempt < 3):
    print('Your guess was wrong, you still have ' + str(int(3 - attempt)) + ' more chance(s)')
    
    guess = int(input('Please type a new guess...  '))
    while(guess < 1 or guess > 50):
        guess = int(input('Your input was incorrect, please type a number between 1 and 50...  '))
    attempt+=1

if ran == guess:
    print('Congrats! You made it! The number was indeed: ' + str(ran))
else:
    print('You used your 3 chances, the number was: ' + str(ran))