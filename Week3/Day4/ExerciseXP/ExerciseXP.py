# Exercuse 1

import random

def get_words_from_file() :
    with open("DI_Bootcamp/Week3/Day4/ExerciseXP/sowpods.txt", mode='r') as words:
        words_lst = words.read().splitlines()     # .splitlines() used to split str into list
        # print(words_lst)
        return words_lst

def get_random_sentence(length) :
        words_lst = get_words_from_file()
        random_sentence = ' '.join(random.choices(words_lst, k=length))
        print(random_sentence.lower())
        return random_sentence.lower()

def main() :
    print('This program will create a sentance for you. The length of that sentence will be based on the length you provide it.')
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
# print(get_words_from_file()) 
get_random_sentence(5)
main()


# Exercise 2

import json

sampleJson = """{ 
   "company":{ 
      "employee":{ 
         "name":"emma",
         "payable":{ 
            "salary":7000,
            "bonus":800
         }
      }
   }
}"""

person_dict = json.loads(sampleJson)
print(person_dict['company']['employee']['payable']['salary'])

person_dict['company']['employee']['birth_date'] ='1988/01/08'
print(person_dict)

person_json = json.dumps(person_dict)
print(person_json)

