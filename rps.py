#ROCK, PAPER, SCISSORS GAME
import random
import getpass
from os import system

def scr_print_choice(key, player):
    if key.upper() == 'A':
        print(player + "'s Choice: ROCK")
        print("""
            _______
        ---'   ____)
              (_____)
              (_____)
              (____)
        ---.__(___)
        """)
        return 'ROCK'
    if key.upper() == 'S':
        print(player + "'s Choice: PAPER")
        print("""
             _______
        ---'    ____)____
                   ______)
                  _______)
                 _______)
        ---.__________)
        """)
        return 'PAPER'
    if key.upper() == 'D':
        print(player + "'s Choice: SCISSORS")
        print("""
            _______
        ---'   ____)____
                  ______)
               __________)
              (____)
        ---.__(___)
        """)
        return 'SCISSORS'
    
def check_result(c,mc):
    if(c == mc):
        return 'TIE'
    elif(c == 'PAPER'):
        if(mc == 'ROCK'):
            return 'User Wins!'
        else:
            return 'Computer Wins!'
    elif(c == 'ROCK'):
        if(mc == 'SCISSORS'):
            return 'User Wins!'
        else:
            return 'Computer Wins!'
    elif(c == 'SCISSORS'):
        if(mc == 'PAPER'):
            return 'User Wins!'
        else:
            return 'Computer Wins!'
        
    
system('cls')    
print('----------------WELCOME TO ROCK, PAPER, SCISSORS----------------')
username = input('Please enter your name: ')
bo = int(input('Select the game duration: *Best of* 1, 3 or 5... '))
while(bo not in [1,3,5]):
    system('cls')
    print('----------------------------------------------------------------')
    bo = int(input('WRONG value entered! Please select a valid game duration: *Best of* 1, 3 or 5... '))
    print('----------------------------------------------------------------')
user_score = 0
computer_score = 0
system('cls')
limit = int((bo/2)+ 1)
print(limit)
while ((user_score < limit) and (computer_score < limit)) or (user_score == computer_score):
    system('cls')
    print('*****INSTRUCTIONS*****')
    print('You will play aginst the computer now, select an option (key) and press ENTER:')
    print('ROCK --> A')
    print('PAPER --> S')
    print('SCISSORS --> D')
    print('----------------------------------------------------------------')
    choice = scr_print_choice(getpass.getpass(prompt='Choose your destiny: '), username)
    #print('User Choice: ' + choice)
    options_list = ['a','s','d']

    machine_choice = scr_print_choice(random.choice(options_list), 'Computer')
    #print('Computer Choice: ' + machine_choice)

    result = check_result(choice, machine_choice)
    print('Result: '+ result)
    if result == 'User Wins!':
        user_score+=1
    elif result == 'Computer Wins!':
        computer_score+=1
    elif result == 'TIE':
        user_score+=1
        computer_score+=1
    print('User Score: '+ str(user_score))
    print('Computer Score: '+ str(computer_score))
    input('Press a KEY to continue... ')
print()   
print('*************-FINAL RESULT-*************')
if(user_score > computer_score):
    print(username + ' Wins!')
    print('WOW! Computer reaction is -->')
    print('(╯°□°）╯︵ ┻━┻')
else:
    print('Computer Wins!')
    print('How do you feel ' + username + '?')
    reaction = int(input('Press 1 if you are fine or press 2 if you are angry with this result!  '))
    while reaction not in [1,2]:
        reaction = int(input('Press 1 if you are fine or press 2 if you are angry with this result!  '))    
    if reaction == 2:
        print('Wow!!! ' + username + ' is mad and rects with...')
        print()
        print('(╬ ಠ益ಠ)')
        print()
        print('┻━┻ ︵ヽ(`Д´)ﾉ︵ ┻━┻')
        print()
        print('Computer just says...     {•̃_•̃} ')
        print()
    else:
        print()
        print(username + "'s reaction is...  ")
        print('◔_◔')
        print()