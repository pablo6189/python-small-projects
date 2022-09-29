print('------------Welcome------------')
bill = float(input('Hello! What\'s today\'s bill? '))
#DEFAULT TIP
tip = round(float((bill * 18) / 100),2)
total = round(float(bill + tip),2)
print('The tip (applying 18%) would be ' + str(tip))

print('The Total is: ' + str(total))
#---------------------------------
#SELECT ANOTHER TIP PERCENTAGE
other_percent = input('Would you like to apply another percentage for th tip ? (Y/N)  ').upper()
while(other_percent not in ('Y','N')):
    print('Incorrect Option, please type Y or N...')
    other_percent = input('Would you like to apply another percentage for th tip ? (Y/N)  ').upper()
if(other_percent == 'Y'):
    percentage = float(input('Please, type the desired percentage... '))
tip = round(float((bill * percentage) / 100),2)
new_total = round(float(bill + tip),2)
print('The tip (applying ' + str(percentage) +'%) would be ' + str(tip))

print('The Total is: ' + str(new_total))
print()
print('--------------------')

#DIVIDE THE TIP AMONG PRESENT PEOPLE
divide = input('Would you like to divide the tip among the present people? (Y/N)  ').upper()
while(other_percent not in ('Y','N')):
    print('Incorrect Option, please type Y or N...')
    divide = input('Would you like to divide the tip among the present people? (Y/N)  ').upper()
if(divide == 'Y'):
    people_num = int(input('Please, type the number of people... '))
    
    #THIS PART ALLOWS YOU TO SPLIT THE TIP IN AN UNEVEN WAY
    if(people_num == 2):
        uneven= input('Would you like to divide the tip in uneven percentage? (Y/N)  ').upper()
        while(uneven not in ('Y','N')):
            print('Incorrect Option, please type Y or N...')
            uneven = input('Would you like to divide the tip in uneven percentage? (Y/N)  ').upper()
        if(uneven =='Y'):
            greater_percentage = int(input('Please enter the higher percentage:  '))
            greater_tip = int(((tip*greater_percentage)/100))
            print()
            print('--------------------')
            print('Person 1 will pay the higher tip: ' + str(greater_tip))
            print('The Total is: ' + str((bill/2) + greater_tip))
            print('Person 2 will pay the smallest tip: ' + str(tip - greater_tip))
            print('The divided Total is: ' + str((bill/2) + (tip - greater_tip)))
        else:
            #THIS PART ALLOWS YOU TO DIVIDE THE TIP EVENLY AMONG 
            divided_tip = int(tip / people_num)
            print()
            print('--------------------')
            print('The divided tip would be ' + str(divided_tip))

            print('The divided Total is: ' + str(int(new_total / people_num)))
    else:
        #THIS PART ALLOWS YOU TO DIVIDE THE TIP EVENLY AMONG 
        divided_tip = int(tip / people_num)
        print()
        print('--------------------')
        print('The divided tip would be ' + str(divided_tip))

        print('The divided Total is: ' + str(int(new_total / people_num)))