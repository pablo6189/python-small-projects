print('Welcome ')
option ='Y'

while option.upper() == 'Y':
    number = int(input('Please think about number and type it... '))
    if number%2 == 0:
        option = input('Your number is even! Would you like to try another? (Y/N) ')
    else:
        option = input('Your number is odd! Would you like to try another? (Y/N) ')

print('Thanks for playing!')