# Exercise 3

3 <= 3 < 9
3 == 3 == 3
bool(0)
bool(5 == "5")
bool(4 == 4) == bool("4" == "4")
bool(bool(None))
x = (1 == True)
y = (1 == False)
a = True + 4
b = False + 10

print("x is", x)
print("y is", y)
print("a:", a)
print("b:", b)

# Exerciuse 4

my_text = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'
print(len(my_text))

# Exercise 5
substring = 'a'

while True :
    long_sentence = input('Please input the longest sentence you can without using the letter A:')

    if long_sentence.find(substring) :
        print('Try again')
    
    else :
        print('Congrats! You created your longest sentence yet!')

        