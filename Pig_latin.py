import os

vowels = ['a','e','i','o','u']
choice = 1

while choice==1:
    os.system("cls")
    word = input('\n\n\t\tEnter a word:')

    i = 0

    for w in word:
        if w in vowels:
            break
        i = i+1



    if i==0:
        print('\n\nPIG LATIN: '+ word[:] + 'ay')
    else:
        print('\n\nPIG LATIN: '+word[i:] + word[:i] + 'ay')



    choice = int(input('\n\nPress 1 to enter a word again...'))
    
