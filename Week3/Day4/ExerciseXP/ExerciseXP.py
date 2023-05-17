import random

def get_words_from_file() :
    with open("DI_Bootcamp/Week3/Day4/sowpods.txt", "r") as words:
        words_lst = words.read().splitlines()     # .splitlines() used to split str into list
        # print(words_lst)
        return words_lst

def get_random_sentence(length) :
        words_lst = get_words_from_file()
        random_sentence = ' '.join(random.choices(words_lst, k=length))
        print(random_sentence.lower())
        return random_sentence.lower()

def main() :
    s_length = int(input('How long do you want to sentence to be (between 2-20)? '))
    try :
        if s_length > 2 and s_length < 20 :
            get_random_sentence(s_length)
        else :
            raise ValueError('You have chose a number outside of the range.')
    except ValueError as error:
        print('VALUE ERROR')
        print(error)
        
        
get_words_from_file()
get_random_sentence(5)
main()

    
    