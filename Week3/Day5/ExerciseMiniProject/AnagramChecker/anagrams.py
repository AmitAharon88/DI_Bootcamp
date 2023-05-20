# Exercise 3, 4
from  AnagramChecker import AnagramChecker

new_check = AnagramChecker('DI_Bootcamp/Week3/Day5/ExerciseMiniProject/AnagramChecker/sowpods.txt') 

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
            elif new_check.is_valid_word(trimmed_word) == True :
                print(f'Your word: {trimmed_word}')
                print('You have entered a valid English word')
                word_anagrams = new_check.get_anagrams(trimmed_word)
                if word_anagrams != [] :
                    anagram_str = ' ,'.join(word_anagrams)
                    print(f'Anagrams for your word are: {anagram_str}')
                else :
                    print('There are not anagrams to this word')
            else :
                print('You have entered an invalid English word')
        
    elif user_input == '2' :
        break
    
    else :
        print('Invalid choice. Try again')
   




