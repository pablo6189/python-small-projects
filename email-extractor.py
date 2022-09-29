email = input('Please, enter your email:   ')
provider = email.split('@')
provider = provider[1].split('.')
provider = provider[0]
if(provider == 'gmail'):
    print('You have a Google account! That looks great!')
elif(provider =='outlook'):
    print('Great! I see you are using a Microsoft account!')
else:
    print('I can see you are using a personalized domain from ' + str(provider) + '!')
