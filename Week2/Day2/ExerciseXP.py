# 🌟 Exercise 1 : Set
#1
my_fav_numbers = [1,2,4,8,16]

#2
my_fav_numbers.append(88)
my_fav_numbers.append(19)
print(my_fav_numbers)

#3
my_fav_numbers.remove(my_fav_numbers[-1])
print(my_fav_numbers)

#4
friend_fav_numbers = [1,2,5,8,10]

#5
our_fav_numbers = my_fav_numbers + friend_fav_numbers
print(our_fav_numbers)

#remove duplicates
in_my_fav_numbers = set(my_fav_numbers)
in_friend_fav_numbers = set(friend_fav_numbers)
in_friends_but_not_in_mine = in_friend_fav_numbers - in_my_fav_numbers
result = my_fav_numbers + list(in_friends_but_not_in_mine)
print(result)

# 🌟 Exercise 2 : Tuple
# No a tuple cannot be modified

# 🌟 Exercise 3 : List
#1
basket = ["Banana", "Apples", "Oranges", "Blueberries"]
basket.remove('Apples')

print(basket)

#2
basket.remove('Blueberries')

print(basket)

#3
basket.append('Kiwi')

print(basket)

#4
basket.insert(0,'Apples')

print(basket)

#5
print(basket.count('Apples'))

#6
basket.clear()


#7
print(basket)


# 🌟 Exercise 4 : Floats

#1- An integrer is a whole number where as a float is a floating point number. It is a number with a decimal point. You need more memory to store a float than and integer. For both you can use math functions.

#2- To create a sequence of floats you can use a list or a tuple. You can use range and loops together.

#3
list = range(3, 11)
number = [x /2 for x in list]
print(number)


# 🌟 Exercise 5 : For loops
#1
for x in range(1, 21) :
    print(x)

#2
numbers = range(1, 21)
for num in numbers :
    if num %2 == 0 :
        print(num)

# 🌟 Exercise 6 : While loops

name = ''
name = input('What is your name?')

while name != 'Amit' :
    name = input('What is your name?')


# 🌟 Exercise 7 : Favorite Fruits

#1
fav_fruits = input('What are your favorite fruits? Please separate the fruits with a single space.')
print(fav_fruits)

#2
list_fruits = fav_fruits.split(' ')
print(list_fruits)

#3
new_fruit = input('name a fruit: ')

for fruit in list_fruits :
    if new_fruit == fruit :
        print('You chose one of your favorite fruits! Enjoy!')
        break
else :
    print('You chose a new fruit. I hope you enjoy')
    

# 🌟 Exercise 8 : Who ordered a pizza?


topping_list = []

while True :
    toppings = input('What topping would you like? If you would not like any please enter \'quit\': ')
    if toppings != 'quit' :
            print(f'We gave added {toppings} to your pizza')
            topping_list.append(toppings)
            toppings = input('What topping would you like? If you would not like any please enter \'quit\': ')
    else :
        break
    
if topping_list:
    price = float(10 + (len(topping_list) * 2.5))
    print(f'Your pizza will contain the following toppings: {topping_list}. Your total comes out to ${price}')
else :
    print('goodbye')

# 🌟 Exercise 9 : Cinemax

#1-3
cost1 = 0
cost2 = 0
cost3 = 0

while True:
    age = input('How old is the ticket holder? If you\'re done, enter \'quit\': ')
    if age.lower() == 'quit':
        ticket_price = cost1 + cost2 + cost3
        print(f'Total cost: {ticket_price}')
        break
    else:
        age_input = int(age)
        if age_input < 3:
            cost1 += 0
        elif age_input >= 3 and age_input <=12:
            cost2 += 10
        else:
            cost3 += 15

#4
teenagers = ['Alice', 'Bob', 'Charlie', 'David', 'Eve']
allowed = []
for teen in teenagers:
    age = int(input(f"How old is {teen}? "))
    if age >= 16 and age <= 21:
        allowed.append(teen)

print(f"The following teenagers are allowed to watch the movie: {allowed}")

    
    
# 🌟 Exercise 10 : Sandwich orders

#1
sandwich_orders = ["Tuna sandwich", "Avocado sandwich", "Egg sandwich", "Sabih sandwich", "Pastrami sandwich"]

#2
finished_sandwiches = []

#3
while sandwich_orders:
    current_sandwich = sandwich_orders.pop(0)
    print(f'I made your {current_sandwich}')
    finished_sandwiches.append(current_sandwich)

#4
print('All sandwiches have been made: ')
for sandwich in finished_sandwiches :
    print(sandwich)

# 🌟 Exercise 11 : Sandwich orders 2

sandwich_orders = ["Tuna sandwich", "Avocado sandwich", "Egg sandwich", "Sabih sandwich", "Pastrami sandwich"]
sandwich_orders.extend(["Pastrami sandwich"] * 2)
print(sandwich_orders)

finished_sandwiches = []
print('The deli has run out of pastrami')
while "Pastrami sandwich" in sandwich_orders :
    sandwich_orders.remove("Pastrami sandwich")
    finished_sandwiches = sandwich_orders
    print(finished_sandwiches)
    