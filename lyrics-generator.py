from os import system
lyrics = [{'artist': 'Coldplay', 'order': 1, 'song': 'Yellow', 'lyrics': 'Look at the stars\nLook how they shine for you\nAnd everything you do\nYeah, they were all yellow'},
 {'artist': 'Coldplay', 'order': 2,'song': 'Viva la Vida', 'lyrics': 'I used to rule the world\nSeas would rise when I gave the word\nNow in the morning I sleep alone\nSweep the streets I used to ow'},
 {'artist': 'Coldplay', 'order': 3,'song': 'Clocks', 'lyrics': 'The lights go out and I can"t be saved\nTides that I tried to swim against\nHave brought me down upon my knees\nOh, I beg, I beg and plead'},
 {'artist': 'Oasis', 'order': 1,'song': 'Wondewall', 'lyrics': 'Today is gonna be the day that they"'"re gonna throw it back to you\nAnd by now, you should've somehow realised what you gotta do\nI don"'"t believe that anybody feels the way I do about you now'},
 {'artist': 'Oasis', 'order': 2,'song': 'Stand by me', 'lyrics': 'Made a meal and threw it up on Sunday\nI"'"ve got a lot of things to learn\nSaid I would and I"'"ll be leaving one day\nBefore my heart starts to burn'},
 {'artist': 'Eminem', 'order': 1,'song': 'Whithout me', 'lyrics': 'Obie Trice, real name no gimmicks\nTwo trailer park girls go round the outside\nRound the outside, round the outside\nTwo trailer park girls go round the outside\nRound the outside, round the outside'},
 {'artist': 'Eminem', 'order': 2,'song': 'Lose yourself', 'lyrics': 'Look\nIf you had\nOne shot\nOr one opportunity\nTo seize everything you ever wanted\nIn one moment\nWould you capture it\nOr just let it slip?'}]

print('--------------WELCOME--------------')
print('Please select your prefered artist:  ')
print('1 - Coldplay')
print('2 - Oasis')
print('3 - Eminem')
option= int(input('0 - to EXIT   '))

while(option != 0):
    artist = ''
    if(option == 1):
        artist = 'Coldplay'
    elif(option == 2):
        artist = 'Oasis'
    elif(option == 3):
        artist = 'Eminem'
    else:
        print('Incorrect Option!')
        print('Please select your prefered artist:  ')
        print('1 - Coldplay')
        print('2 - Oasis')
        print('3 - Eminem')
        int(input('0 - to EXIT  '))
    if(option in (1,2,3)):
        print('This are the songs I have for you: ')
        orders = []
        for lyric in lyrics:
            if(lyric['artist'].upper() == artist.upper()):
                print(str(lyric['order']) +' - ' + lyric['song'])
                orders.append(int(lyric['order']))
        opt = int(input('Select the song you want to read...  '))
        
        while(opt not in orders):
            print('Incorrect option... ')
            opt = int(input('Select the song you want to read...  '))
        if(opt in orders):
            for l in lyrics:
                if((l['artist'].upper() == artist.upper()) and opt == int(l['order'])):
                    system('cls')
                    print('---'+l['song']+' by '+ l['artist']+'---')
                    print(l['lyrics'])
                    print()
                    print('-------------------------')
            
            
    input('Press a key to continue...')
    
    print('Would you like to read another lyric?  ')
    print('1 - Coldplay')
    print('2 - Oasis')
    print('3 - Eminem')
    option= int(input('0 - to EXIT   '))
    system('cls')
            
    