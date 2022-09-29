from os import system

def check_day(d,m):
    m1 = [1,3,5,7,8,10,12]
    m2 = [4,6,9,11]
    if(d < 1):
        return False
    if m == 2 and d > 29:
        #print('The age you entered is lower than 0, please try again')
        return False
    if m in m1 and d > 31:
        #print('The age you entered is higher than 99, please try again')
        return False
    if m in m2 and d > 30:
        #print('The age you entered is higher than 99, please try again')
        return False
    return True

def convert_mont(m):
    if(m == 1):
        return 'Jan'
    elif(m == 2):
        return 'Feb'
    elif(m == 3):
        return 'Mar'
    elif(m == 4):
        return 'Apr'
    elif(m == 5):
        return 'May'
    elif(m == 6):
        return 'Jun'
    elif(m == 7):
        return 'Jul'
    elif(m == 8):
        return 'Aug'
    elif(m == 9):
        return 'Sep'
    elif(m == 10):
        return 'Oct'
    elif(m == 11):
        return 'Nov'
    elif(m == 12):
        return 'Dec'
    else:
        return 'error!'
    
system('cls')
print('-------------------------------')
name = input('Hello! Please, enter your name: ')
while len(name) < 3:
    print('The name you entered is too short.')
    name = input('Please, try again: ')
print('-------------------------------')    
#Birth date
print('Please, enter your Birth date... ')
    #Check year
year = int(input('Enter the year you were born: '))
while (year < 1920):
    year = int(input('Year cannot be earlier than 1920 '))

    #Check Month
month = int(input('Enter the month (Numbers from 1 to 12): '))
while(month < 1 or month > 12):
    month = int(input('The month you entered is incorrect, please try again... '))
month_name = convert_mont(month)

    #Check Day
day = int(input('Enter the day: '))
while(check_day(day,month) is False):
    day = int(input('The day you entered is incorrect,please try again: '))


system('cls')

#Address
print('---------------------------')
print('Enter your address... ')
street = input('Please enter the Street Name: ')
while len(street) < 3:
    print('The street name you entered is too short.')
    street = input('Please, try again: ')
street_number = input('Please enter the Street number: ')
while len(street_number) < 1:
    print('The street number cannot be empty.')
    street_number = input('Please, try again: ')
city = input('Please enter your City: ')
while len(city) < 1:
    print('The street number cannot be empty.')
    city = input('Please, try again: ')
    
pers_address = street_number +' '+ street + ', ' + city
system('cls')
#Goals
goals = input('Tell me about your personal goals: ')
while len(goals) < 1:
    goals = input('Please, enter at least one personal goal: ')
    
system('cls')

print('--------YOUR DATA--------')
print('-Name: ' + name)
print('-Birth date: '+ str(month_name)+' '+ str(day)+', ' + str(year))
print('-Address: ' + pers_address)
print('-Personal Goals: '+ goals)
print('-------------------------')