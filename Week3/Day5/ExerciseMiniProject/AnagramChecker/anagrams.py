# Exercise 3, 4
from  MiniProjectAnagramChecker import AnagramChecker

while True :
    user_input = input('1. Input a word\n2. Exit\nEnter your action: ')
    if user_input == '1' :
        user_word = input('Enter a word: ')
        trimmed_word = user_word.strip()
        try :
            if len(trimmed_word.split(' ')) != 1 :
                raise ValueError ('Invalid input. You entered more then 1 word.')
            if not trimmed_word.isalpha() :
                raise ValueError ('Invalid input. Only alphabetic characters allowed.')
        except ValueError as error :
            print(ValueError)
            print(error)
        else :
            len(trimmed_word.split(' ')) == 1
            if not trimmed_word.isalpha() :
                raise ValueError ('Invalid input. Only alphabetic characters allowed.')
            elif AnagramChecker.is_valid_word(trimmed_word) == True :
                print(f'Your word: {trimmed_word}')
                print('You have entered a valid English word')
                print(AnagramChecker.get_anagrams(trimmed_word))
            else :
                print('You have entered an invalid English word')
        
    elif user_input == '2' :
        break
    
    else :
        print('Invalid choice. Try again')
   
user = AnagramChecker() 



