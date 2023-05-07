#1
sentence = input('Please write a string here: ')
string_length = len(sentence)

if string_length < 10 :
    print('String not long enough')
elif string_length > 10 :
    print('String too long')
    
#2
firstChar = sentence[0]
lastChar = sentence [-1]
print(f'{firstChar}, {lastChar}')

#3

string = sentence

for i in range(len(string)):
    print(string[:i+1])
  
#4
import random
list_sentence = list(sentence)

random.shuffle(list_sentence)

shuffled_string = ''.join(list_sentence)

print(shuffled_string)


 

