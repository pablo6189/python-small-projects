#This small program finds out if the words typed by the user are palindromes
print('*****WELCOME*****')
#phrase = input('Please enter 5 words and I will tell you if they are palindromes... ')
words =[]
words.append(input('Please enter a word and I will tell you if it is a palindrome... '))
option = input("Would you like to enter another word? (Y/N)  ").upper()
while(option not in ['Y','N']):
    option = input("Incorrect value. Would you like to enter another word? (Y/N)  ").upper()
while(option == 'Y'):
    words.append(input('Enter a new word: '))
    option = input("Would you like to enter another word? (Y/N)  ").upper()
for word in words:
    print()
    print('-------------------')
    reverseword = ''
    wordlength = len(word)
    while(wordlength > 0):
        reverseword = str(reverseword + word[int(wordlength-1)])
        wordlength = int(wordlength-1)
    if(word == reverseword):
        print('word = '+ word + ' -> reverse = '+reverseword)
        print('PALINDROME!!!')
    else:
        print('word = '+ word + ' -> reverse = '+reverseword)
        print('This is not a palindrome!')
    print('-------------------')
    #print(reverseword)