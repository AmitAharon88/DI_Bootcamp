# Exercise 1: Hello World written on 1 line

print ('Hello World Hello World Hello World')

long_string = '''
Hello World
Hello World
Hello World'''

print(long_string)

print ('Hello World\n' * 3)

#Exercise 2: Write code that calculates the result of: (99^3)*8 (meaning 99 to the power of 3, times 8).

print((99 ** 3) * 8)

#Exercise 3: 
# Predict the output of the following code snippets:
# You will receive booleans
# 5 < 3                 output: False
# 3 == 3                output: True
# 3 == "3"              output: False
# "3" > 3               output: False
# "Hello" == "hello"    output: False

#🌟 Exercise 4 : Your Computer Brand

computer_brand = 'Apple'
print(f'I have a {computer_brand} computer.')

#🌟 Exercise 5 : Your Information

name = 'Amit'
age = '35'
shoe_size = '38'
info = 'Hello, my name is ' + name + ' and my age and shoe size is as follows respectivly ' + age + " ," + shoe_size
print(info)

#🌟 Exercise 6 : A & B

a = 5
b = 2

if a > b :
    print('Hello World')

# Exercise 7 : Odd or Even

number = int(input('Pick a number from 1-10:'))
if (number % 2) == 0 :
    print('this number is even')
else :
    print('this number is odd')

#🌟 Exercise 8 : What's your name?

your_name = (input('What\'s your name?'))
my_name = 'Amit'
if my_name == your_name :
    print('OMG, I CAN\'T BELEIVE IT. WE HAVE THE SAME NAME!')
else :
    print('Oh, well that\'s not my name, but I guess it\'s a nice name too.')
    
#🌟 Exercise 9 : Tall enought to ride a roller coaster

height_in = int(input('What is your height in inches?'))
if height_in > 145 :
    print('Congrats! You are tall enought to ride!')
else :
    print('Grad yourself some protein and come back when your tall enough!')