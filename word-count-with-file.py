import string

print('Hi! Welcome! I will read your text now... ')
text = open('text-file.txt').read()
translator = text.maketrans('', '', string.punctuation)
text_count = text.translate(translator).split()
print('The text has '+ str(len(text_count)) + ' words.')