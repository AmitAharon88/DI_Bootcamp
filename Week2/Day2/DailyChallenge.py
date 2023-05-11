#1
num = int((input('give me a number: ')))
list_length = int((input('give me a length: ')))
full_list = []

while len(full_list) <  list_length :
    full_list.append(num * (len(full_list) +1))
    
print(full_list)

#2


users_word = input('give me a string: ')  
new_word = ''

for letter_index in range(len(users_word)) :
    if letter_index == 0 or users_word[letter_index] != users_word[letter_index - 1] :
        new_word += users_word[letter_index]
print(new_word)
    
