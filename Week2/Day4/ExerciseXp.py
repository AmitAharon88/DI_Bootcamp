# Exercise 1 : What Are You Learning ?

def display_message() :
    print('I am learning how to become a full stack developer with tools such as HTML, CSS, and Python')

display_message()

# 🌟 Exercise 2: What’s Your Favorite Book ?

def favorite_book(title) :
    print(f'One of my favorite books is {title}')  
favorite_book('Harry Potter') 

# 🌟 Exercise 3 : Some Geography

def describe_city(city, country = 'USA') :
    print(f'{city} is in {country}')
describe_city('New York')

# Exercise 4 : Random

def number(your_num) :
    num_range = range(1, 101)
    if your_num in num_range :
        import random
        random_num = random.choice(num_range)
        print(random_num)
        if your_num == random_num :
            print('Success!')
        else :
            print(f'Maybe next time: {your_num} does not equal {random_num}')
    else :
        print('Your number is not in the range of 1-100. Try again: ')

number(100)
        
# 🌟 Exercise 5 : Let’s Create Some Personalized Shirts!

def make_shirt(size = 'large', text = 'I love Python') :
    print(f'The size of the shirt is {size} and the text is {text}')

make_shirt('small', 'This is my first shirt')
make_shirt()                #because large is the default so i don't need to define it
make_shirt('medium')
make_shirt('Any size')
make_shirt(text = 'I UNDERSTAND THIS!', size = 'small')


# 🌟 Exercise 6 : Magicians …

def show_magicians() :
    magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel']
    for name in magician_names :
        print(name)
    return magician_names

show_magicians()


magician_names = show_magicians()
def make_great(magician_names) :
    for i in range(len(magician_names)) :
        great_names = 'The Great ' + magician_names[i]
        print(great_names)
        
make_great(magician_names)

show_magicians()

# 🌟 Exercise 7 : Temperature Advice
#1
def get_random_temp() :
    import random
    return random.randint(-10, 40)
    
print(get_random_temp())

#2 & 3

temp = get_random_temp()
new_temp = []
def main(temp) :
    new_temp = temp
    print(f'The temperature right now is {new_temp} degrees Celsius')
    if new_temp < 0 :
        print('It\'s freezing. bundle up!')
    elif new_temp <= 16 :
        print('It\'s cold. don\'t forget your mittens!')
    elif new_temp <= 23 :
        print('It\'s  a bit nippy, make sure to wear a scarf')
    elif new_temp <= 32 :
        print('It\'s perfect skiing weather!')
    elif new_temp <= 40 :
        print('Spring is around the corner')
    #Sorry my temps were in F.   
main(temp)

#4
temp = ''
def get_random_temp(season) :
    if season == 'winter' :
        temp == '-10 and 14'
    elif season == 'fall':
        temp == '-15 and 20'
    elif season == 'spring' :
        temp == '-21 and 25'
    elif season == 'summer' :
        temp == '25 and more'
    print(f'You\'re currently in {season}. Temperature should fall between {temp}.')
    return season
        
    
get_random_temp('fall')


user_season = input('type in a season (winter, spring, summer, fall: ')
get_random_temp(user_season)




