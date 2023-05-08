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

for letter in range(len(users_word)) :
    if letter == 0 or users_word[letter] != users_word[letter - 1] :
        new_word += users_word[letter]
        print(new_word)
    
