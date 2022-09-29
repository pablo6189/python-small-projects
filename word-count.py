import string

text = input('Hi! Welcome! How are you feeling today? Do you have any plans? ')
translator = text.maketrans('', '', string.punctuation)
text_count = text.translate(translator).split()
print('You have expressed your feelings in '+ str(len(text_count)) + ' words.')