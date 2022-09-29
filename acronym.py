#This small program finds the acronym out of a phrase or set of words
print('*****WELCOME*****')
phrase = input('Please enter a phrase and I will tell you the acronym... ')
words = phrase.split()
acronym = ''
for word in words:
    acronym = str(acronym + word[0].upper())
print(acronym)
